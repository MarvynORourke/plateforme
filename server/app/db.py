import base64
import sqlite3
import hashlib

DB_LOG_NAME = "db.db"

def init_db(): #tested
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
                 USER_ID    INTEGER     NOT NULL,
                 NAME       TEXTE       NOT NULL
                 );""")
    conn.commit()
    conn.close()

def add_user(user_name, password): #tested
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
                    base64.b64encode(user_name), digest))

    conn.commit()
    conn.close()


def check_user_connection(user_name, password): #tested
    """Get username from password..."""
    m = hashlib.md5()
    m.update(password)
    digest = m.hexdigest()
    
    conn = sqlite3.connect(DB_LOG_NAME)
    c = conn.cursor()
    c.execute("""SELECT COUNT(*) FROM users
                 WHERE USER = '{}' AND PASS = '{}';""".format(
                     base64.b64encode(user_name), digest))
    conn.commit()

    try:
        for row in enumerate(c):
            tmp = float(tuple(row)[1][0])
            return tmp > 0
    except:
        return False

def add_course(id_user, name): #tested
    """Add course in DB"""
    conn = sqlite3.connect(DB_LOG_NAME)
    c = conn.cursor()
    c.execute("""INSERT INTO courses
                 (USER_ID, NAME) VALUES ('{}', '{}');""".format(id_user, base64.b64encode(name)))
    conn.commit()
    last = c.lastrowid
    c.close()
    conn.close()
    return last



def get_courses(id_user): #tested
    """Get course from db"""
    conn = sqlite3.connect(DB_LOG_NAME)
    c = conn.cursor()
    c.execute("""SELECT ID FROM courses WHERE USER_ID = ('{}')""".format(id_user))                
    conn.commit()


    out = []
    try:
        for row in enumerate(c):
            out.append(row)
    except:
        pass

    c.close()
    conn.close()

    return out


init_db()
add_user("olivier", "moi")
add_user("toi", "moche")

print "test connection..."
print check_user_connection("olivier", "moi")
print check_user_connection("", "ty")
print check_user_connection("olivier", "toi")

print "adding courses id..."
print add_course(1, "mon_cours")
print add_course(2, "a")
print add_course(2, "b")

print "get courses for id 2..."
print get_courses(2)
