import sqlite3
import json
from flask import Flask, jsonify, request, render_template

DATABASE = "db name"

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

@app.route("/", methods=['GET','POST'])
def show_index():
    conn = get_db_connection()
    booking = conn.execute('SELECT A.name FROM DB_TABLE_NAME1 AS A LEFT JOIN DB_TABLE_NAME2 AS B ON A.type = B.id').fetchall()
    return render_template('dashboard/index.html', bookings=booking)

if __name__ == '__main__':
   app.run('0.0.0.0', 3003, True)