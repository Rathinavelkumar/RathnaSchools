import markdown
from markupsafe import Markup

def render_aligned_markdown(text):
    html = markdown.markdown(text, extensions=['fenced_code', 'tables'])
    return Markup(html)
