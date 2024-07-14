# """
# Flask configuration variables.
# """
from flask_sqlalchemy import SQLAlchemy


from os import environ, path
#
basedir = path.abspath(path.dirname(__file__))
# load_dotenv(path.join(basedir, '.env'))

class Config:
    """Set Flask configuration from .env file."""
    # General Config
    SECRET_KEY = 'kristofer'
    FLASK_APP = 'flask_blog.app'
    #engine = create_engine("mysql+mysqldb://chrism:lesson@localhost/data5zero")
    # Database
    #SQLALCHEMY_DATABASE_URI = 'sqlite:///lsk.db'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://lydia:celeste@localhost/lsk'
    #SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://lydia:celeste@localhost/lsk' # 'sqlite:///circuscircus.db'
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False



import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="lydia",
    passwd="celeste",
)

my_cursor = mydb.cursor()

#my_cursor.execute("CREATE DATABASE lsk")
#my_cursor.execute("DROP DATABASE lsk")
my_cursor.execute("SHOW DATABASES")
for db in my_cursor:
    print(db)

my_cursor.execute('use lsk')
#my_cursor.execute('DROP TABLE IF EXISTS blogposts;')

#my_cursor.execute( 'CREATE TABLE blogposts ( id INTEGER PRIMARY KEY AUTO_INCREMENT, created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,title TEXT NOT NULL, content TEXT NOT NULL);')






import sqlite3
import pymysql

#connection = sqlite3.connect('../database.db')


# with open('schema.sql') as f:
#     connection.executescript(f.read())
#
# cur = connection.cursor()

my_cursor.execute("INSERT INTO blogposts (title, content) VALUES (%s, %s)",
            ('First Post', 'Content for the first post')
                  )

mydb.commit()
# connection.commit()
# connection.close()
