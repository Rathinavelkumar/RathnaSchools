from flask import render_template, send_from_directory, current_app
import os
from . import main

@main.route('/')
def index():
    return render_template('main/index.html', title='Home', carousel=True)

@main.route('/about')
def about():
    return render_template('main/about.html', title='About Us', carousel=False)

@main.route('/terms')
def terms():
    return render_template('main/terms.html', title='Terms of Use', carousel=False)

@main.route('/privacy')
def privacy():
    return render_template('main/privacy.html', title='Privacy Policy', contact_email='contact@rathnashools.com', carousel=False)

@main.route('/sitemap.xml')
def sitemap():
    return send_from_directory(os.path.join(current_app.root_path, '..'), 'sitemap.xml', mimetype='application/xml')

@main.route('/ads.txt')
def ads_txt():
    return send_from_directory(os.path.join(current_app.root_path, '..'), 'ads.txt', mimetype='text/plain')

@main.route('/robots.txt')
def robots_txt():
    return send_from_directory(os.path.join(current_app.root_path, '..'), 'robots.txt', mimetype='text/plain')
