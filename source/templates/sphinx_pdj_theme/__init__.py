import os

VERSION = '0.2.1'


def get_html_theme_path():
    """Return list of HTML theme paths."""
    cur_dir = os.path.abspath(os.path.dirname(__file__))
    return cur_dir


def setup(app):
    #app.add_html_theme('sphinx_pdj_theme', get_html_theme_path())
    rtd_locale_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'locale')
    app.add_message_catalog('sphinx', rtd_locale_path)
