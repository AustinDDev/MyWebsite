"""Render the buildless Projects index from separate live-project and roadmap data.

Run: python scripts/render_projects.py
Use --check to verify the checked-in HTML without modifying it.
Roadmap status never promotes an initiative; verified work must be added explicitly
in data/projects.json. No third-party packages or browser JavaScript are required.
"""
from pathlib import Path
from html import escape
import argparse,json,re
ROOT=Path(__file__).resolve().parents[1]
CATEGORIES={'Project Management & Delivery','IT Operations & Leadership','Technical Engineering & Solutions'}
def esc(value):return escape(str(value),quote=True)
def load(name):return json.loads((ROOT/'data'/name).read_text(encoding='utf-8'))
def project_card(p):
 if p['category'] not in CATEGORIES or not isinstance(p['featured'],bool):raise ValueError('Invalid live-project category or featured flag')
 if not all(p.get(k) for k in ['title','slug','subtitle','description','status','technologies','liveUrl','githubUrl','detailRoute']):raise ValueError('Missing live-project field')
 if not (ROOT/p['detailRoute']).is_file():raise ValueError('Missing project detail page')
 slug=esc(p['slug']);featured=' lww-featured' if p['featured'] else ''
 tags=''.join('<li>'+esc(t)+'</li>' for t in p['technologies'])
 note='<p class="caption">'+esc(p['note'])+'</p>' if p.get('note') else ''
 return f'''<article class="card deliverable-card{featured}" id="{slug}-project" data-featured="{str(p['featured']).lower()}" aria-labelledby="{slug}-title">
<p class="deliverable-status">{esc(p['status'])}</p><h3 id="{slug}-title">{esc(p['title'])}</h3><p class="project-subtitle">{esc(p['subtitle'])}</p><p>{esc(p['description'])}</p><p class="project-category">{esc(p['category'])}</p>
<dl class="project-role"><dt>My role</dt><dd>{esc(p['role'])}</dd><dt>Type</dt><dd>{esc(p['projectType'])}</dd></dl><ul class="skill-tags" aria-label="Technologies and tools">{tags}</ul>{note}
<div class="deliverable-links"><a class="card-arrow" href="{esc(p['detailRoute'])}">View Project <span aria-hidden="true">↗</span></a><a class="text-link" href="{esc(p['liveUrl'])}">Live Website ↗</a><a class="text-link" href="{esc(p['githubUrl'])}">GitHub source code ↗</a></div></article>'''
def roadmap_card(p):
 if p['status'] not in {'Concept','Planning','In Development'}:raise ValueError('Invalid roadmap status')
 if any(k in p for k in ['liveUrl','githubUrl','detailRoute','featured']):raise ValueError('Roadmap entries must not carry live-project links or featured flags')
 notes=''.join('<li>'+esc(n)+'</li>' for n in p.get('notes',[]))
 extra='<p class="roadmap-note">'+esc(p['note'])+'</p>' if p.get('note') else ''
 details=f'<details><summary>{esc(p.get("notesLabel","Future development notes"))}</summary><ul>{notes}</ul>{extra}<p class="roadmap-note">Proposed areas of exploration, not completed features.</p></details>' if notes else ''
 return f'''<article class="card roadmap-initiative" id="{esc(p['slug'])}" aria-labelledby="{esc(p['slug'])}-title"><p class="roadmap-category">{esc(p['category'])}</p><p class="roadmap-status">{esc(p['status'])}</p><h3 id="{esc(p['slug'])}-title">{esc(p['title'])}</h3><p>{esc(p['description'])}</p>{details}</article>'''
def aliases(ids):return '<div class="legacy-project-anchors" aria-hidden="true">'+''.join(f'<span id="{i}"></span>' for i in ids)+'</div>'
def render(source):
 projects=load('projects.json');roadmap=load('development-roadmap.json')
 for entries in [projects,roadmap]:
  if len({p['slug'] for p in entries})!=len(entries):raise ValueError('Duplicate slug')
 featured=[p for p in projects if p['featured']];standard=[p for p in projects if not p['featured']]
 intro='''<section class="wrap selected-work-intro"><p class="section-kicker">Portfolio / Live work &amp; future development</p><h1>Projects &amp; Development</h1><p class="work-subheading">A collection of applications, technical solutions, and ongoing initiatives reflecting my approach to engineering, problem-solving, and continuous improvement.</p>'''+aliases(['technical-projects-heading','additional-work-heading','printer-monitoring-project','employee-onboarding-project','photohut-network-project','windows-migration-project'])+'''<p class="work-introduction">For professional project context, operational contributions, and lessons learned, explore the separate <a class="text-link" href="case-studies.html">Case Studies</a>.</p></section>'''
 live=''
 for title,id,items in [('Featured Project','featured-project-heading',featured),('Other Projects','other-projects-heading',standard)]:
  if items:live+=f'<section class="wrap project-selection live-project-group" aria-labelledby="{id}"><div class="filter-heading"><h2 id="{id}">{title}</h2></div><div class="cards deliverables-grid">'+''.join(project_card(p) for p in items)+'</div></section>'
 future='''<section class="section technical-roadmap development-roadmap" id="upcoming-projects" aria-labelledby="upcoming-heading"><div class="wrap"><p class="section-kicker">Development roadmap / Future initiatives</p><h2 id="upcoming-heading">What's Next</h2><p class="upcoming-intro">Exploring software engineering, artificial intelligence, and game development through new ideas, technical experimentation, and long-term projects.</p><p class="roadmap-disclaimer">These initiatives describe future directions. Planning and Concept entries are not operational systems or completed implementations.</p>'''+aliases(['enterprise-infrastructure','security-monitoring','it-operations-dashboard','enterprise-network','ai-it-assistant','asset-management'])+'<div class="cards roadmap-grid">'+''.join(roadmap_card(p) for p in roadmap)+'</div></div></section>'
 result=re.sub(r'(<main id="main">).*?(</main>)',lambda m:m[1]+'\n'+intro+live+future+m[2],source,flags=re.S)
 if 'development-roadmap.css' not in result:result=result.replace('</head>','<link rel="stylesheet" href="development-roadmap.css">\n</head>')
 result=re.sub(r'<meta name="description" content="[^"]*">','<meta name="description" content="Live development projects by Austin Dalton and a separate roadmap for future software, AI, and game development initiatives.">',result)
 result=result.replace('<title>Projects | Austin Dalton</title>','<title>Projects &amp; Development | Austin Dalton</title>')
 return result
if __name__=='__main__':
 parser=argparse.ArgumentParser();parser.add_argument('--check',action='store_true');args=parser.parse_args()
 path=ROOT/'projects.html';original=path.read_text(encoding='utf-8');updated=render(original)
 if args.check:
  if original!=updated:raise SystemExit('Projects HTML is out of sync. Run python scripts/render_projects.py')
  print('PASS: Projects HTML matches data.')
 else:path.write_text(updated,encoding='utf-8');print('Rendered projects.html from live-project and roadmap data.')
