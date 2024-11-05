import sqlite3

db = sqlite3.connect("application_data.db")

def init_db(db):
    cursor = db.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            task TEXT NOT NULL,
            is_done BOOLEAN NOT NULL CHECK (is_done IN (0, 1)),
            FOREIGN KEY (user_id) REFERENCES users (id)
        )
    ''')
    
    # Predefined users
    user_list = [
        ("admin", "admin@admin.com", "qwertz"),
        ("user1", "user1@user1.com", "securePassword")
    ]
    cursor.executemany("INSERT INTO users (username, email, password) VALUES (?, ?, ?)", user_list)

    # Predefined tasks
    tasks = [
        (1, "Admin Task 1", False),
        (1, "Admin Task 2", False),
        (2, "User1 Task 1", False),
        (2, "User1 Task 2", False)
    ]
    
    cursor.executemany("INSERT INTO tasks (user_id, task, is_done) VALUES (?, ?, ?)", tasks)
    db.commit()

init_db(db)

db.close()