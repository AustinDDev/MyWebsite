# Projects content

Edit `projects.json` for verified live work and `development-roadmap.json` for future initiatives, then run:

```text
python scripts/render_projects.py
python scripts/render_projects.py --check
```

The generated Projects page stays usable without JavaScript or a framework build. Run these commands from the repository root. Python's standard library is sufficient; no packages are required.

Live projects support title, slug, subtitle, description, category, status, featured (boolean), projectType, role, technologies, liveUrl, githubUrl, detailRoute, and optional note. Categories are Project Management & Delivery, IT Operations & Leadership, and Technical Engineering & Solutions. Featured projects render separately from standard entries; empty groups do not render.

Roadmap entries support title, slug, description, category, status, and optional notesLabel, notes and note. Valid statuses are Concept, Planning and In Development. Live URLs, repositories, detail routes and featured flags are deliberately excluded. Moving an initiative to live work requires a reviewed entry in projects.json and an existing detail page; status alone never promotes it.

Detail pages remain maintained in their existing HTML files. The portfolio's actual implementation uses HTML, CSS and JavaScript; do not substitute an unimplemented framework stack in its technology list.

Legacy Projects/roadmap anchors remain at their relevant index introductions to preserve incoming URLs. Existing homepage roadmap labels still describe the previous roadmap; changing that page requires a separate scoped update.
