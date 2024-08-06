#!/usr/bin/python3
"""roor file for the api"""
from flask import Flask
from models import storage
from api.v1.views import app_views
import os

app = Flask(__name__)
app.register_blueprint(app_views)

def create_database():
    """Create the MySQL database if it doesn't exist."""
    db_user = os.getenv("HBNB_MYSQL_USER")
    db_pwd = os.getenv("HBNB_MYSQL_PWD")
    db_host = os.getenv("HBNB_MYSQL_HOST")
    db_name = os.getenv("HBNB_MYSQL_DB")

    try:
        db = MySQLdb.connect(
            host=db_host,
            user=db_user,
            passwd=db_pwd
        )
        cursor = db.cursor()
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {db_name};")
        cursor.close()
        db.close()
        print(f"Database {db_name} created or already exists.")
    except MySQLdb.Error as err:
        print(f"Error: {err}")



@app.teardown_appcontext
def teardown_db(exception):
    """Closes the storage on teardown"""
    storage.close()

if __name__ == "__main__":
    host = os.getenv("HBNB_API_HOST", "0.0.0.0")
    port = int(os.getenv("HBNB_API_PORT", "5000"))
    app.run(host=host, port=port, threaded=True)
