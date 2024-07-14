"""
Flask configuration variables.
"""
from os import environ, path

basedir = path.abspath(path.dirname(__file__))
# load_dotenv(path.join(basedir, '.env'))

class Config:
    """Set Flask configuration from .env file."""
    # General Config
    SECRET_KEY = 'lydia'
    FLASK_APP = 'forum.app'
    #engine = create_engine("mysql+mysqldb://lydia:celeste@localhost/lsk")
    # Database
    #SQLALCHEMY_DATABASE_URI = 'sqlite:///lsk.db'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://lydia:celeste@localhost/lsk'
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False