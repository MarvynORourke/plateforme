#!flask/bin/python
from app import app

app.run(host="0.0.0.0", port=85, debug=True, threaded=True)


import db


db.init_db()

