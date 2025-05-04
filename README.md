# RathnaSchools

Welcome to **RathnaSchools** – a modern, production-level Flask web application designed to teach and entertain with Python, Java, and Fairy Tales content.

## Features
- Clean, modular, and maintainable Flask codebase
- Python, Java, and Fairy Tales sections
- SEO-optimized and Adsense-ready templates
- Markdown-powered content management
- Responsive, Bootstrap-based UI
- Production-ready with Gunicorn (Linux)
- Easy to extend and deploy

## Project Structure
```
RathnaSchools/
├── app/
│   ├── __init__.py
│   ├── config.py
│   ├── utils_markdown.py
│   ├── main/
│   ├── python/
│   ├── java/
│   ├── fairy_tales/
│   ├── static/
│   └── templates/
├── content/
│   ├── python/
│   ├── java/
│   └── fairy_tales/
├── requirements.txt
├── README.md
├── .gitignore
├── wsgi.py
```

## Running Locally
1. Create a virtual environment:
   ```
   python3 -m venv venv
   source venv/bin/activate
   ```
2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Run with Flask (dev):
   ```
   export FLASK_APP=app
   flask run
   ```
4. Run with Gunicorn (production):
   ```
   gunicorn --bind 0.0.0.0:8000 "wsgi:app"
   ```

## SEO & Adsense
- Meta tags and SEO keywords are included in templates.
- Adsense-ready ad blocks are present in the base template.

## Content Management
- Add markdown files to `content/python/`, `content/java/`, or `content/fairy_tales/`.
- Each file becomes a lesson or story.

## Contributing
PRs and suggestions welcome! Clean code and docstrings required.

## License
MIT
