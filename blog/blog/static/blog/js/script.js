const menuBtn = document.querySelector('.menu-btn');
const footer = document.querySelector('footer');
const nav = document.querySelector('.navbar');
const dropdown = document.querySelector('.dropdown');

menuBtn.addEventListener('click', () => {
	menuBtn.classList.toggle('close');
	nav.classList.toggle('close');
});

dropdown.addEventListener('click', () => {
	dropdown.classList.toggle('clicked');
});

year = new Date().getFullYear();
footer.innerHTML += `${year}`;

