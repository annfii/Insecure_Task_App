const input = document.querySelector('#input-box')
const tasks = document.querySelector('.task__list')
const add__button = document.querySelector('.add__btn')


async function getTasks() {
    const response = await fetch('/tasks',)
    const taskData = await response.json()
    tasks.innerHTML = ''
    taskData.forEach(task => {
        let li = document.createElement("li")
        li.dataset.id = task.id
        li.textContent = task.description
        if (task.completed) {
            li.classList.add('checked')
        }
        let span = document.createElement("span")
        span.innerHTML = "\u00d7"
        li.appendChild(span)
        tasks.appendChild(li)
    })
}

async function addTask(task) {

    const response = await fetch('/tasks', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ task: task })
    })
    return response.json()
}

async function updateTask(taskId, isDone) {
    await fetch(`/tasks/${taskId}`, {
        method: 'PUT',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ is_done: isDone })
    })
}

async function deleteTaskInDb(taskId) {
    await fetch(`/tasks/${taskId}`, {
        method: 'DELETE'
    })
}

add__button.addEventListener('click', async function() {
    if (input.value === '') {
        alert('Task is empty!')
    } else {
        const newTask = await addTask(input.value)
        let li = document.createElement("li")
        li.dataset.id = newTask.id
        li.textContent = newTask.task
        let span = document.createElement("span")
        span.innerHTML = "\u00d7"
        li.appendChild(span)
        tasks.appendChild(li)
        input.value = ""
    }
})

tasks.addEventListener('click', async function(e) {
  if (e.target.tagName === "LI") {
      checkTask(e)
  } else if (e.target.tagName === "SPAN") {
      deleteTask(e)
  }
})

function deleteTask(e) {
  const taskId = e.target.parentElement.dataset.id
  e.target.parentElement.remove()
  deleteTaskInDb(taskId)
}

function checkTask(e) {
  const taskId = e.target.dataset.id
  const isDone = !e.target.classList.contains("checked")
  e.target.classList.toggle("checked")
  updateTask(taskId, isDone)
}

getTasks()
