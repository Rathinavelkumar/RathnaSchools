import os
from flask import Flask
from flask_bootstrap import Bootstrap

def create_app():
    app = Flask(__name__)
    app.config.from_pyfile(os.path.join(os.path.dirname(__file__), 'config.py'), silent=True)
    Bootstrap(app)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .python import python as python_blueprint
    app.register_blueprint(python_blueprint, url_prefix='/python')

    from .java import java as java_blueprint
    app.register_blueprint(java_blueprint, url_prefix='/java')

    from .fairy_tales import fairy_tales as fairy_tales_blueprint
    app.register_blueprint(fairy_tales_blueprint, url_prefix='/fairy_tales')

    return app
