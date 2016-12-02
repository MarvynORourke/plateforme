import base64
import sqlite3
import hashlib

DB_LOG_NAME = "db.db"

def init_db():
    """This method init the database schema..."""
    conn = sqlite3.connect(DB_LOG_NAME)
    c = conn.cursor()
    #table user
    c.execute("""CREATE TABLE IF NOT EXISTS users
                (ID INTEGER PRIMARY KEY AUTOINCREMENT,
                 USER   TEXT    NOT NULL,
                 PASS   TEXT    NOT NULL
                 );""")
    #table courses
    c.execute("""CREATE TABLE IF NOT EXISTS courses
                (ID INTEGER PRIMARY KEY AUTOINCREMENT,
                 USER_ID    INTEGER     NOT NULL
                 );""")
    conn.commit()
    conn.close()

def add_user(user_name, password):
    """Add new user to the database...
    """
    #hasshinbg password for secure...
    m = hashlib.md5()
    m.update(password)
    digest = m.hexdigest()

    conn = sqlite3.connect(DB_LOG_NAME)
    c = conn.cursor()
    c.execute("""INSERT INTO users
                (USER, PASS) VALUES ('{}', '{}');""".format(
                    base64(b64encode(user_name)), digest))

    conn.commit()
    conn.close()


def check_user_connection(user_name, password):
    """Get username from password..."""
    m = hashlib.md5()
    m.update(password)
    digest = m.hexdigest()
    
    conn = sqlite3.connect(DB_LOG_NAME)
    c = conn.cursor()
    c.execute("""SELECT COUNT(*) FROM users
                 WHERE USER = '{}' AND PASS = '{}';""".format(
                     base64(b64encode(user_name), digest)))
    conn.commit()

    try:
        for row in enumerate(c):
            tmp = float(tuple(row)[1][0])
            return tmp >= 0
    except:
        return False




    
                
