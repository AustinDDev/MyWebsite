// Project detail pages retain the shared navigation while selecting Projects.
if (document.body.classList.contains('lww-detail')) {
  const projectLink = document.querySelector('nav[aria-label="Main navigation"] a[href="projects.html"]');
  if (projectLink) projectLink.setAttribute('aria-current', 'page');
}
