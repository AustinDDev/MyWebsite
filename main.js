const year = document.getElementById('year');
if (year) year.textContent = new Date().getFullYear();
const current = location.pathname.split('/').pop() || 'index.html';
document.querySelectorAll('nav a').forEach(link => {
 if (link.getAttribute('href') === current) link.setAttribute('aria-current', 'page');
});
