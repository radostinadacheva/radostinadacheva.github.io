from pathlib import Path
import os,re
owner=os.environ['GITHUB_REPOSITORY_OWNER'].lower()
repo=os.environ['GITHUB_REPOSITORY'].split('/',1)[1].lower()
if repo != owner+'.github.io':
 raise SystemExit('Name this repository '+owner+'.github.io to publish at your free profile address.')
origin='https://'+owner+'.github.io'
old='https://radostina-dacheva-portfolio.zippybetta24.chatgpt.site'
for p in Path('dist').rglob('*'):
 if p.is_file() and p.suffix in {'.html','.xml','.txt'}:
  p.write_text(p.read_text().replace(old,origin))
(Path('dist')/'.nojekyll').touch()
print('Publishing '+origin)
