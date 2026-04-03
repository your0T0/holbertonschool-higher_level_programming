#!/usr/bin/python3
"""
Task 3: Displaying Data from JSON or CSV Files in Flask
"""

from flask import Flask, render_template, request
import json
import csv

app = Flask(__name__)


def read_json_file():
    """Read products from JSON file"""
    with open('products.json', 'r', encoding='utf-8') as file:
        return json.load(file)


def read_csv_file():
    """Read products from CSV file"""
    products = []
    with open('products.csv', 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            products.append({
                "id": int(row["id"]),
                "name": row["name"],
                "category": row["category"],
                "price": float(row["price"])
            })
    return products


@app.route('/products')
def products():
    source = request.args.get('source')
    product_id = request.args.get('id')

    if source not in ['json', 'csv']:
        return render_template(
            'product_display.html',
            error="Wrong source"
        )

    try:
        if source == 'json':
            products_data = read_json_file()
        else:
            products_data = read_csv_file()
    except Exception:
        return render_template(
            'product_display.html',
            error="Error reading data file"
        )

    if product_id:
        try:
            product_id = int(product_id)
            filtered_products = [p for p in products_data if int(p["id"]) == product_id]

            if not filtered_products:
                return render_template(
                    'product_display.html',
                    error="Product not found"
                )

            products_data = filtered_products
        except ValueError:
            return render_template(
                'product_display.html',
                error="Invalid id"
            )

    return render_template(
        'product_display.html',
        products=products_data,
        source=source
    )


if __name__ == '__main__':
    app.run(debug=True, port=5000)
