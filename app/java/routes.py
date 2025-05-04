import os
from flask import render_template, abort, current_app, redirect, url_for
from . import java
from app.utils_markdown import render_aligned_markdown

@java.route('/')
def java_index():
    content_dir = os.path.join(current_app.root_path, '..', 'content', 'java')
    files = [f for f in os.listdir(content_dir) if f.endswith('.md')]
    files = sorted(files)
    if files:
        first_slug = files[0][:-3]
        return redirect(url_for('java.java_detail', java_slug=first_slug))
    return render_template('shared_index.html', files=files, title='Java Lessons', section='java', carousel=False)

@java.route('/<java_slug>')
def java_detail(java_slug):
    content_dir = os.path.join(current_app.root_path, '..', 'content', 'java')
    files = [f for f in os.listdir(content_dir) if f.endswith('.md')]
    files = sorted(files)
    md_path = os.path.join(content_dir, f'{java_slug}.md')
    try:
        with open(md_path, encoding='utf-8') as f:
            content = render_aligned_markdown(f.read())
    except FileNotFoundError:
        abort(404)
    return render_template(
        'shared_detail.html',
        content=content,
        title=java_slug.replace('-', ' ').title(),
        files=files,
        active_slug=java_slug,
        section='java',
        section_title='Java Lessons',
        carousel=False
    )
