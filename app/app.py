import os
from flask import Flask, request, jsonify
import mysql.connector

app = Flask(__name__)

def get_db():
    return mysql.connector.connect(
        host=os.getenv("DB_HOST", "db"),
        user=os.getenv("DB_USER", "orders_user"),
        password=os.getenv("DB_PASSWORD", "orders_pass"),
        database=os.getenv("DB_NAME", "orders_db"),
        port=int(os.getenv("DB_PORT", "3306")),
    )

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/orders")
def create_order():
    data = request.get_json(force=True)
    product = data.get("product_name")
    quantity = data.get("quantity")
    price = data.get("price")

    if not product or quantity is None or price is None:
        return {"error": "product_name, quantity, price are required"}, 400

    conn = get_db()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO orders (product_name, quantity, price) VALUES (%s, %s, %s)",
        (product, quantity, price),
    )
    conn.commit()
    order_id = cur.lastrowid
    cur.close()
    conn.close()

    return {"order_id": order_id, "message": "created"}, 201

@app.get("/orders")
def list_orders():
    conn = get_db()
    cur = conn.cursor(dictionary=True)
    cur.execute("SELECT id, product_name, quantity, price, created_at FROM orders ORDER BY id DESC")
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return jsonify(rows)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
