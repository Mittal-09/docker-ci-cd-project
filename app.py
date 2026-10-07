from flask import Flask
import mysql.connector
import os
import time

app = Flask(__name__)


def get_db_connection():
    return mysql.connector.connect(
        host=os.getenv("MYSQL_HOST", "mysql"),
        database=os.getenv("MYSQL_DATABASE", "taskdb"),
        user=os.getenv("MYSQL_USER", "appuser"),
        password=os.getenv("MYSQL_PASSWORD", "apppassword")
    )


@app.route("/")
def home():
    return "Hello! Docker CI/CD Project is Running."


@app.route("/health")
def health():
    return "OK"


@app.route("/db")
def database():
    try:
        connection = get_db_connection()
        cursor = connection.cursor()

        cursor.execute("SELECT 1")
        result = cursor.fetchone()

        cursor.close()
        connection.close()

        return f"MySQL Connected Successfully! Result: {result[0]}"

    except Exception as e:
        return f"MySQL Connection Failed: {e}", 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)