from flask import render_template

from app import app
from app.models.order_list import orders

@app.route('/orders')
def index():
    return render_template(
        'index.html',
        title="orders",
        orders=orders
    )

@app.route('/orders/<index>')
def show(index):
    return render_template(
        'order.html',
        title='Show order',
        order=orders[int(index)]
    )