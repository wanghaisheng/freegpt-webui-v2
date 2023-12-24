import os,sys
import subprocess
from flask import request, session, jsonify
from flask_babel import Babel

if getattr(sys, 'frozen', False):
    # The application is frozen
    datadir = os.path.dirname(sys.executable)
else:
    # The application is not frozen
    datadir = os.path.dirname(__file__)
    datadir=os.path.dirname(datadir)

# https://stackoverflow.com/questions/56733085/how-to-know-the-current-file-path-after-being-frozen-into-an-executable-using-cx
ROOT_DIR = datadir
print(f"ROOT_DIR{ROOT_DIR}")
def get_languages_from_dir(directory):
    """Return a list of directory names in the given directory."""
    return [name for name in os.listdir(directory)
            if os.path.isdir(os.path.join(directory, name))]


BABEL_DEFAULT_LOCALE = 'en_US'

BABEL_LANGUAGES = get_languages_from_dir(os.path.join(ROOT_DIR,'translations'))
print(f"BABEL_LANGUAGES{BABEL_LANGUAGES}")

def create_babel(app):
    """Create and initialize a Babel instance with the given Flask app."""
    babel = Babel(app)
    app.config['BABEL_DEFAULT_LOCALE'] = BABEL_DEFAULT_LOCALE
    app.config['BABEL_LANGUAGES'] = BABEL_LANGUAGES

    babel.init_app(app, locale_selector=get_locale)
    compile_translations()


def get_locale():
    """Get the user's locale from the session or the request's accepted languages."""
    return session.get('language') or request.accept_languages.best_match(BABEL_LANGUAGES)


def get_languages():
    """Return a list of available languages in JSON format."""
    return jsonify(BABEL_LANGUAGES)


def compile_translations():
    """Compile the translation files."""
    result = subprocess.run(
        ['pybabel', 'compile', '-d', os.path.join(ROOT_DIR,'translations')],
        stdout=subprocess.PIPE,
    )

    if result.returncode != 0:
        raise Exception(
            f'Compiling translations failed:\n{result.stdout.decode()}')

    print('Translations compiled successfully')
