
from flask import Flask, render_template, request
import pymysql
import config

app = Flask(__name__)

connection = pymysql.connect(
    host=config.DB_HOST,
    user=config.DB_USER,
    password=config.DB_PASSWORD,
    database=config.DB_NAME
)

@app.route("/")
def home():
    return render_template("login.html")

@app.route("/login", methods=["POST"])
def login():
    username = request.form["username"]
    password = request.form["password"]

    cursor = connection.cursor()

    sql = "SELECT * FROM employees WHERE username=%s AND password=%s"

    cursor.execute(sql, (username, password))

    user = cursor.fetchone()

    if user:
        return render_template("dashboard.html", username=username)

    return render_template("login.html", error="Invalid Username or Password")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
