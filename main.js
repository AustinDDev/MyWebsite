// DARK MODE TOGGLE
const toggle = document.getElementById('darkToggle');
const icon = document.getElementById('theme-icon');

// Update button icon
function updateIcon(isDark) {
  icon.textContent = isDark ? '☀️' : '🌙';
}

// Toggle dark mode
toggle.addEventListener('click', () => {
  document.body.classList.toggle('dark');
  const isDark = document.body.classList.contains('dark');
  updateIcon(isDark);
  localStorage.setItem('dark-mode', isDark);
});

// Apply saved preference or system preference
window.addEventListener('DOMContentLoaded', () => {
  const saved = localStorage.getItem('dark-mode');
  const prefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches;

  const shouldUseDark = saved === 'true' || (!saved && prefersDark);
  if (shouldUseDark) {
    document.body.classList.add('dark');
  }

  updateIcon(document.body.classList.contains('dark'));
});


// SCROLL FADE-IN ANIMATION
const fadeInElements = document.querySelectorAll('.fade-in');

const observer = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      entry.target.classList.add('visible');
    }
  });
}, {
  threshold: 0.1
});

fadeInElements.forEach(el => observer.observe(el));


// NAV LINK HOVER COLOR (Optional if not handled by CSS alone)
const navLinks = document.querySelectorAll('.nav-links a');

navLinks.forEach(link => {
  link.addEventListener('mouseenter', () => {
    link.style.color = '#007acc';
  });
  link.addEventListener('mouseleave', () => {
    link.style.color = document.body.classList.contains('dark') ? '#f1f1f1' : '#111';
  });
});
