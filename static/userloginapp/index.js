const modal = document.getElementsByClassName('modal')[0];
const loginModalBtn = document.getElementById('loginModalBtn');
const registerModalBtn = document.getElementById('registerModalBtn');
const loginForm = document.getElementById('loginForm');
const registerForm = document.getElementById('registerForm');
const closeSpan = document.querySelector('.modal-content span');
const cancelBtn = document.getElementById('cancelBtn');
const cancelBtn2 = document.getElementById('cancelBtn2');
const registerFormSwitch = document.getElementById('regSwitch');
const loginSwitch = document.getElementById('loginSwitch');

loginModalBtn.addEventListener('click', displayLoginForm);
loginSwitch.addEventListener('click', displayLoginForm);
registerFormSwitch.addEventListener('click', displayRegisterForm);
registerModalBtn.addEventListener('click', displayRegisterForm);
closeSpan.addEventListener('click', closeModal);
cancelBtn.addEventListener('click', closeModal);
cancelBtn2.addEventListener('click', closeModal);

function closeModal() {
    modal.classList.remove('modal-active');
}

function displayRegisterForm() {
    loginSwitch.classList.remove('active-btn');
    registerFormSwitch.classList.add('active-btn');
    registerForm.classList.add('form-active');
    loginForm.classList.remove('form-active');
    modal.classList.add('modal-active');
}

function displayLoginForm() {
    loginSwitch.classList.add('active-btn');
    registerFormSwitch.classList.remove('active-btn');
    registerForm.classList.remove('form-active');
    loginForm.classList.add('form-active');
    modal.classList.add('modal-active');
}
