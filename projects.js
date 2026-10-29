/* Progressive enhancement: all grouped content remains readable without JS. */
(() => {
  const filters = document.querySelector('.project-filters');
  const results = document.getElementById('project-results');
  if (!filters || !results) return;

  const buttons = [...filters.querySelectorAll('button[data-filter]')];
  const cards = [...document.querySelectorAll('[data-project-category]')];
  const groups = [...results.querySelectorAll('[data-project-group]')];
  const roadmap = document.querySelector('[data-roadmap-group]');
  const announcement = document.querySelector('[data-filter-announcement]');
  const valid = new Set(buttons.map(button => button.dataset.filter));
  const names = Object.fromEntries(buttons.map(button => [button.dataset.filter, button.textContent.trim()]));

  function requestedFilter() {
    const url = new URL(window.location.href);
    const requested = url.searchParams.get('category') || 'all';
    const category = valid.has(requested) ? requested : 'all';
    // A legacy roadmap deep link takes precedence over a conflicting filter.
    let target;
    try { target = document.getElementById(decodeURIComponent(url.hash.slice(1))); }
    catch { target = null; }
    const linkedCard = target && target.closest('[data-project-category]');
    if (linkedCard && category !== 'all' && linkedCard.dataset.projectCategory !== category) return 'all';
    if (roadmap && target === roadmap && category === 'delivery') return 'all';
    return category;
  }

  function applyFilter(category, updateUrl = false) {
    if (!valid.has(category)) category = 'all';
    buttons.forEach(button => button.setAttribute('aria-pressed', String(button.dataset.filter === category)));
    cards.forEach(card => { card.hidden = category !== 'all' && card.dataset.projectCategory !== category; });
    groups.forEach(group => { group.hidden = category !== 'all' && group.dataset.projectGroup !== category; });
    if (roadmap) roadmap.hidden = !cards.some(card => roadmap.contains(card) && !card.hidden);
    if (announcement) {
      const shown = cards.filter(card => !card.hidden);
      const cases = shown.filter(card => card.dataset.projectKey).length;
      const other = shown.filter(card => !card.dataset.projectKey && results.contains(card)).length;
      const planned = shown.length - cases - other;
      announcement.textContent = `${names[category]}: ${cases} case-study cards${other ? `, ${other} additional projects` : ''}${planned ? `, ${planned} roadmap concepts` : ''}.`;
    }
    if (updateUrl) {
      const url = new URL(window.location.href);
      if (category === 'all') url.searchParams.delete('category');
      else url.searchParams.set('category', category);
      // Avoid retaining an anchor to content hidden by a deliberate filter change.
      url.hash = '';
      try { window.history.replaceState(null, '', url); } catch { /* Filtering works even if URL updates are unavailable. */ }
    }
  }

  filters.addEventListener('click', event => {
    const button = event.target.closest('button[data-filter]');
    if (!button || !filters.contains(button)) return;
    applyFilter(button.dataset.filter, true);
  });
  // Native buttons provide Tab, Enter and Space behavior without custom key handlers.
  window.addEventListener('popstate', () => applyFilter(requestedFilter()));
  window.addEventListener('hashchange', () => applyFilter(requestedFilter()));
  const controlledIds = ['project-results', roadmap && roadmap.id].filter(Boolean).join(' ');
  buttons.forEach(button => button.setAttribute('aria-controls', controlledIds));
  applyFilter(requestedFilter());
  filters.hidden = false;
})();
