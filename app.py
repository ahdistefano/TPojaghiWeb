from flask import Flask, render_template, g, request, session, redirect, url_for, \
                         abort
from flask_babel import Babel
from urllib.parse import urlparse, urljoin
from data import ALBUMS

app = Flask(__name__)
babel = Babel(app)
app.config['BABEL_DEFAULT_LOCALE'] = 'en'
app.secret_key = '123456'

##############
# Babel init #
##############

def is_safe_url(target):
    ref_url = urlparse(request.host_url)
    test_url = urlparse(urljoin(request.host_url, target))
    return test_url.scheme in ('http', 'https') and ref_url.netloc == test_url.netloc

@app.route('/language/<language>')
def set_language(language=None):
    session['language'] = language
    next_page = request.args.get('next') or url_for('home')
    if not is_safe_url(next_page):
        return abort(400)
    return redirect(next_page)

def get_locale():
    """ Try to use the locale from the user settings,
    otherwise guess the language from the user accept header"""
    g.current_locale = 'en'
    user = getattr(g, 'user', None)
    if user is not None:
        g.current_locale = user.locale
    else:
        g.current_locale = session.get('language') or request.accept_languages.best_match(['en', 'es'])
    return g.current_locale

babel.init_app(app, locale_selector=get_locale)

############
# Routings #
############

@app.route('/')
@app.route('/home')
@app.route('/index')
def home():
    return render_template('index.html')

@app.route('/projects')
def projects():
    return render_template('projects.html', albums=ALBUMS)

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)


# pybabel extract -F babel.cfg -o messages.pot .
# pybabel init -i messages.pot -d translations -l es
# pybabel update -i messages.pot -d translations
# pybabel compile -d translations