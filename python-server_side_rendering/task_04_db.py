#!/usr/bin/python3
"""
Task 4: SQLite Integration with Flask
"""

from flask import Flask, render_template, request
import json
import csv
import sqlite3

app = Flask(__name__)


# ---------- JSON ----------
def read_json():
    with open('products.json', 'r') as f:
        return json.load(f)


# ---------- CSV ----------
def read_csv():
    products = []
    with open('products.csv', 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            products.append({
                "id": int(row["id"]),
                "name": row["name"],
                "category": row["category"],
                "price": float(row["price"])
            })
    return products


# ---------- SQLITE ----------
def read_sql():
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()

    cursor.execute("SELECT id, name, category, price FROM Products")
    rows = cursor.fetchall()

    conn.close()

    products = []
    for row in rows:
        products.append({
            "id": row[0],
            "name": row[1],
            "category": row[2],
            "price": row[3]
        })

    return products


# ---------- ROUTE ----------
@app.route('/products')
def products():
    source = request.args.get('source')
    product_id = request.args.get('id')

    # ❌ Wrong source
    if source not in ['json', 'csv', 'sql']:
        return render_template('product_display.html', error="Wrong source")

    # 📦 load data
    try:
        if source == 'json':
            data = read_json()
        elif source == 'csv':
            data = read_csv()
        else:
            data = read_sql()
    except Exception:
        return render_template('product_display.html', error="Error loading data")

    # 🔍 filter by id
    if product_id:
        try:
            product_id = int(product_id)
            data = [p for p in data if p["id"] == product_id]

            if not data:
                return render_template('product_display.html', error="Product not found")

        except ValueError:
            return render_template('product_display.html', error="Invalid id")

    return render_template('product_display.html', products=data)


# ---------- DATABASE SETUP ----------
def create_database():
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Products (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            category TEXT NOT NULL,
            price REAL NOT NULL
        )
    """)

    cursor.execute("""
        INSERT OR IGNORE INTO Products (id, name, category, price)
        VALUES
        (1, 'Laptop', 'Electronics', 799.99),
        (2, 'Coffee Mug', 'Home Goods', 15.99)
    """)

    conn.commit()
    conn.close()


if __name__ == '__main__':
    create_database()
    app.run(debug=True, port=5000)
