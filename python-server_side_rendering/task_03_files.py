#!/usr/bin/python3
from flask import Flask, render_template, request
import json
import csv

app = Flask(__name__)

def read_json():
    with open('products.json', 'r') as f:
        return json.load(f)

def read_csv():
    products = []
    with open('products.csv', 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            row['id'] = int(row['id'])
            row['price'] = float(row['price'])
            products.append(row)
    return products

@app.route('/products')
def products():
    source = request.args.get('source')
    product_id = request.args.get('id')
    error_message = None
    products = []

    if source == 'json':
        try:
            products = read_json()
        except Exception:
            error_message = "Unable to read JSON file"
    elif source == 'csv':
        try:
            products = read_csv()
        except Exception:
            error_message = "Unable to read CSV file"
    else:
        error_message = "Wrong source"

    if not error_message and product_id:
        try:
            product_id = int(product_id)
            products = [p for p in products if p['id'] == product_id]
            if not products:
                error_message = "Product not found"
        except ValueError:
            error_message = "Product not found"

    return render_template('product_display.html', products=products, error_message=error_message)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
