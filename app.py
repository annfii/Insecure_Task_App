import sqlite3, uuid, os, re
from flask import Flask, session, render_template, request, g, redirect, url_for, flash, jsonify, make_response, send_file
from markupsafe import escape

app = Flask(__name__)

# Key is not a part of the challange !!!
app.secret_key = uuid.uuid4().hex 

app.config.update(
    SESSION_COOKIE_SECURE=True,
    SESSION_COOKIE_SAMESITE='Lax',
)

@app.route("/")
def home():
    page = request.args.get('page')
    return render_template('home.html', page=page)

@app.route('/page')
def input():
    return render_template('/components/page.html')

@app.route("/blog")
def blog():
    return render_template('blog.html')

@app.route("/settings")
def settings():
    if 'user_id' not in session or is_authorized_adm() == False:
        return jsonify({'error': 'Unauthorized'}), 401
    return render_template('settings.html')

@app.route('/blog-svg', methods=['GET'])
def blog_svg():
    requested_file = request.args.get('jpg')
    sanitized_file = re.sub(r'\.\./', '', requested_file)
    image_path = os.path.join(os.getcwd(), "static", "img", sanitized_file)
    return send_file(image_path)

@app.route("/register", methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        user_count = query_db("SELECT COUNT(*) FROM users", one=True)
        username = request.form['username']
        email = request.form['email']
        password = request.form['password'] 
        exists_email = query_db("SELECT 1 FROM users WHERE email = ?", [email], one=True) 
        print(exists_email)
        if exists_email is None and user_count[0] <= 100:
            db = get_db()
            cursor = db.cursor()
            cursor.execute("INSERT INTO users (username, email, password) VALUES (?, ?, ?)", (username, email, password))
            db.commit()
            flash('Registration successful! Please log in.', 'success')
            return redirect(url_for('login'))
        else:
            flash('Registration not possible!!', 'danger')
    return render_template('register.html')

@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        user = query_db("SELECT * FROM users WHERE email = '{}' AND password = '{}'".format(email, password), one=True) 
        if user:
            session['user_id'] = user[0]
            response = make_response(redirect(url_for('taskmanager')))
            response.set_cookie('logged_in', 'true')
            response.set_cookie('user_id', str(user[0]))
            return response
        flash('Invalid email or password !!!', 'danger')
    return render_template('login.html')

@app.route("/logout")
def logout():
    session.pop('user_id', None)
    response = make_response(redirect(url_for('login')))
    response.set_cookie('logged_in', 'false')
    response.set_cookie('user_id', '', expires=0)
    return response

@app.route('/taskmanager')
def taskmanager():
    if 'user_id' not in session:
        flash('Login to see your tasks !!!', 'danger')
        return redirect(url_for('login'))
    return render_template('taskmanager.html')

@app.route('/tasks', methods=['GET'])
def get_tasks():
    if 'user_id' not in session:
        return jsonify({'error': 'Unauthorized'}), 401
    user_id = session['user_id']
    tasks = query_db("SELECT * FROM tasks WHERE user_id = ?", [user_id])
    tasks_list = [{'id': task[0], 'title': task[1], 'description': task[2], 'completed': task[3]} for task in tasks]
    return jsonify(tasks_list)

@app.route('/tasks', methods=['POST'])
def add_task():
    if 'user_id' not in session:
        return jsonify({'error': 'Unauthorized'}), 401
    user_id = session['user_id']
    task_count = query_db("SELECT COUNT(*) FROM tasks WHERE user_id = ?",[user_id], one=True)
    if task_count[0] >= 50:
        return jsonify({'error': 'Task limit reached. You cannot have more than 50 tasks.'}), 403
    task = request.json.get('task')
    db = get_db()
    cursor = db.cursor()
    cursor.execute("INSERT INTO tasks (user_id, task, is_done) VALUES (?, ?, ?)", (user_id, escape(task), False))
    db.commit()
    return jsonify({'id': cursor.lastrowid, 'task': task, 'is_done': False})

@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    if 'user_id' not in session:
        return jsonify({'error': 'Unauthorized'}), 401
    user_id = session['user_id']
    task_data = request.json
    is_done = task_data.get('is_done')
    db = get_db()
    cursor = db.cursor()
    task = query_db("SELECT user_id FROM tasks WHERE id = ?", [task_id], one=True)
    if task and task[0] == user_id:
        cursor.execute("UPDATE tasks SET is_done = ? WHERE id = ?", (is_done, task_id))
        db.commit()
        return jsonify({'id': task_id, 'is_done': is_done})
    return jsonify({'error': 'Unauthorized'}), 401

@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    if 'user_id' not in session:
        return jsonify({'error': 'Unauthorized'}), 401
    user_id = session['user_id']
    db = get_db()
    cursor = db.cursor()
    task = query_db("SELECT user_id FROM tasks WHERE id = ?", [task_id], one=True)
    if task and task[0] == user_id:
        cursor.execute("DELETE FROM tasks WHERE id = ?", [task_id])
        db.commit()
        return jsonify({'result': 'success'})
    return jsonify({'error': 'Unauthorized'}), 401

@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    if 'user_id' not in session or is_authorized_adm() == False:
        return jsonify({'error': 'Unauthorized'}), 401
    db = get_db()
    cursor = db.cursor()
    user = query_db("SELECT * FROM users WHERE id = ?", [user_id], one=True)
    if user and user[0] == user_id:
        cursor.execute("DELETE FROM tasks WHERE user_id = ?", [user_id])
        cursor.execute("DELETE FROM users WHERE id = ?", [user_id])
        db.commit()
        return jsonify({'result': 'success'})
    return jsonify({'error': 'Unauthorized'}), 401

@app.route('/users', methods=['GET'])
def get_users():
    if 'user_id' not in session or is_authorized_adm() == False:
        return jsonify({'error': 'Unauthorized'}), 401
    users = query_db("SELECT id, username, email FROM users")
    user_list = []
    for user in users:
        print(user)
        user_list.append({'id': user[0], 'name': user[1], 'email': user[2]})
    return jsonify(user_list)

def is_authorized_adm():
    user_id = request.cookies.get('user_id')
    if not user_id:
        return False
    return int(user_id) == 1

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect('application_data.db')
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

def query_db(query, args=(), one=False):
    cursor = get_db().execute(query, args)
    data = cursor.fetchall()
    cursor.close()
    return (data[0] if data else None) if one else data