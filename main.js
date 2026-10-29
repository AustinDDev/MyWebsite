const year = document.getElementById('year');
if (year) year.textContent = new Date().getFullYear();

// Experience reuses About's existing section rather than duplicating its content.
function updateMainNavigation() {
  const links = [...document.querySelectorAll('nav[aria-label="Main navigation"] a')];
  const current = new URL(window.location.href);
  const path = current.pathname.endsWith('/') ? current.pathname + 'index.html' : current.pathname;
  links.forEach(link => link.removeAttribute('aria-current'));
  const matching = links.filter(link => {
    const destination = new URL(link.getAttribute('href'), current);
    return destination.pathname === path;
  });
  const section = matching.find(link => {
    const destination = new URL(link.getAttribute('href'), current);
    return destination.hash && destination.hash === current.hash;
  });
  const page = matching.find(link => !new URL(link.getAttribute('href'), current).hash);
  const caseIndex = path.endsWith('-case-study.html')
    ? links.find(link => new URL(link.getAttribute('href'), current).pathname.endsWith('/case-studies.html'))
    : null;
  const active = section || page || caseIndex;
  if (active) active.setAttribute('aria-current', section ? 'location' : 'page');
}
updateMainNavigation();
window.addEventListener('hashchange', updateMainNavigation);
