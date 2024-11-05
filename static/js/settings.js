const input = document.querySelector('#input-box')
const users = document.querySelector('.user__list')
const add__button = document.querySelector('.add__btn')


async function getUsers() {

    const response = await fetch('/users')
    const usersData = await response.json()
    users.innerHTML = ''
    usersData.forEach(user => {
      if(user.id != '1'){
        let li = document.createElement("li")
        li.dataset.id = user.id
        li.innerHTML = `Name: ${user.name} E-Mail: ${user.email}`
        let span = document.createElement("span")
        span.innerHTML = "\u00d7"
        li.appendChild(span)
        users.appendChild(li)
      }
    })
}

async function deleteUserInDb(userId) {
  await fetch(`/users/${userId}`, {
      method: 'DELETE'
  })
}

users.addEventListener('click', async function(e) {
    if (e.target.tagName === "SPAN") {
      deleteUser(e)
  }
})

function deleteUser(e) {
  const userId = e.target.parentElement.dataset.id
  e.target.parentElement.remove()
  deleteUserInDb(userId)
}

getUsers()