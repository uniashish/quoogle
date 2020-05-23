const modal = document.getElementsByClassName('modal')[0];
const loginModalBtn = document.getElementById('loginModalBtn');
const closeSpan = document.querySelector('.modal-content span');
const cancelBtn = document.getElementById('cancelBtn');

loginModalBtn.addEventListener('click', () => {
    modal.classList.add('modal-active');
});

closeSpan.addEventListener('click', closeModal);

cancelBtn.addEventListener('click', closeModal);

function closeModal() {
    modal.classList.remove('modal-active');
}
