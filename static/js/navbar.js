document.addEventListener('DOMContentLoaded', async () => {
  const menu = document.querySelector('#mobile-menu')
  const menuLinks = document.querySelector('.navbar__menu')
  const authLink = document.querySelector('#auth-link')

  const getCookie = (name) => {
    const cookie = document.cookie.split('; ').find(row => row.startsWith(`${name}=`));
    return cookie ? cookie.split('=')[1] : null;
  };

  const loggedIn = getCookie('logged_in') === 'true';
  const userIdAdm = getCookie('user_id') === '1';

  menu.addEventListener('click', function() {
    menu.classList.toggle('is-active')
    menuLinks.classList.toggle('active')
  })

  if (loggedIn) {
    authLink.href = '/logout'
    authLink.innerHTML = 'Logout'
  } else {
    authLink.href = '/login'
    authLink.innerHTML = 'Login'
  }

  if (userIdAdm) {
     const settings = document.createElement('a')
     settings.href = '/settings'
     settings.className = 'navbar__links'
     settings.innerHTML = 'Settings'
     menuLinks.appendChild(settings)
   }


});