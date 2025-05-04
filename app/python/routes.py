import os
from flask import render_template, abort, current_app, redirect, url_for
from . import python
from app.utils_markdown import render_aligned_markdown

@python.route('/')
def python_index():
    content_dir = os.path.join(current_app.root_path, '..', 'content', 'python')
    files = [f for f in os.listdir(content_dir) if f.endswith('.md')]
    files = sorted(files)
    if files:
        first_slug = files[0][:-3]
        return redirect(url_for('python.python_detail', python_slug=first_slug))
    return render_template('shared_index.html', files=files, title='Python Lessons', section='python', carousel=False)

@python.route('/<python_slug>')
def python_detail(python_slug):
    content_dir = os.path.join(current_app.root_path, '..', 'content', 'python')
    files = [f for f in os.listdir(content_dir) if f.endswith('.md')]
    files = sorted(files)
    md_path = os.path.join(content_dir, f'{python_slug}.md')
    try:
        with open(md_path, encoding='utf-8') as f:
            content = render_aligned_markdown(f.read())
    except FileNotFoundError:
        abort(404)
    return render_template(
        'shared_detail.html',
        content=content,
        title=python_slug.replace('-', ' ').title(),
        files=files,
        active_slug=python_slug,
        section='python',
        section_title='Python Lessons',
        carousel=False
    )
