import os
from flask import render_template, abort, current_app, redirect, url_for
from . import fairy_tales
from app.utils_markdown import render_aligned_markdown

@fairy_tales.route('/')
def fairy_tales_index():
    content_dir = os.path.join(current_app.root_path, '..', 'content', 'fairy_tales')
    files = [f for f in os.listdir(content_dir) if f.endswith('.md')]
    files = sorted(files)
    if files:
        first_slug = files[0][:-3]
        return redirect(url_for('fairy_tales.fairy_tales_detail', fairy_tales_slug=first_slug))
    return render_template('shared_index.html', files=files, title='Fairy Tales', section='fairy_tales', carousel=False)

@fairy_tales.route('/<fairy_tales_slug>')
def fairy_tales_detail(fairy_tales_slug):
    content_dir = os.path.join(current_app.root_path, '..', 'content', 'fairy_tales')
    files = [f for f in os.listdir(content_dir) if f.endswith('.md')]
    files = sorted(files)
    md_path = os.path.join(content_dir, f'{fairy_tales_slug}.md')
    try:
        with open(md_path, encoding='utf-8') as f:
            content = render_aligned_markdown(f.read())
    except FileNotFoundError:
        abort(404)
    return render_template(
        'shared_detail.html',
        content=content,
        title=fairy_tales_slug.replace('-', ' ').title(),
        files=files,
        active_slug=fairy_tales_slug,
        section='fairy_tales',
        section_title='Fairy Tales',
        carousel=False
    )
