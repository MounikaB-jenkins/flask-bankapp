from flask import Flask
import psycopg2
from config import get_database_config

app = Flask(__name__)


def get_connection():

    config = get_database_config()

    return psycopg2.connect(
        host=config["host"],
        database=config["database"],
        user=config["user"],
        password=config["password"],
        port=config["port"]
    )


@app.route("/")
def home():

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT * FROM customers")

    rows = cur.fetchall()

    cur.close()
    conn.close()

    return str(rows)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
