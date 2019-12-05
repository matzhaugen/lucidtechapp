from flask import Flask, request, jsonify
import uuid
from random import choice, randrange
from string import ascii_uppercase


app = Flask(__name__)

current_price = float(1)
current_reservations = 0
reservations = {}
products = {}
n_products = 999


@app.route('/reserve/<customer_id>', methods=['POST', 'GET'])
def reserve(customer_id):
    """Summary
    Usage: curl  http://127.0.0.1:5000/reserve/kdash -X GET
    curl http://127.0.0.1:5000/reserve/kdash -X POST -d product_ids='123,213'
    Args:
        customer_id (str): 

    Returns:
        reservations: json-object
    """
    if request.method == 'POST':
        product_ids = request.form.get('product_ids').split(',')
        reservations[customer_id] = product_ids

    return jsonify(reservations.get(customer_id, None))


@app.route('/product/<product_id>', methods=['POST', 'GET'])
def product(product_id):
    """Summary
    Usage: curl  http://127.0.0.1:5000/product/ -X POST -d product_id=bar -d name=foo
    Returns:
        TYPE: Description
    """
    if request.method == 'POST':
        description = request.form.get('description', None)
        name = request.form.get('name', None)
        print(name)
        price = request.form.get('price', None)
        products[product_id] = {
            'name': name,
            'description': description,
            'price': price}
        result = products[product_id]
    elif request.method == 'GET':
        result = products.get(product_id, None)

    return jsonify(data=result)


@app.route('/batch/', methods=['POST'])
def add_batch():

    global n_products
    for i in range(n_products):
        description = ''.join(choice(ascii_uppercase) for i in range(12))
        name = f'Bosch-{i}'
        product_id = uuid.uuid4()
        price = randrange(4000) + 1000
        products[product_id] = {
            'name': name,
            'description': description,
            'price': price}

    return jsonify(data=0)


@app.route('/price/', methods=['GET', 'POST'])
def price():
    """Get and update price
    POST: curl -d new_price=1 http://127.0.0.1:5000/price/
    GET: curl http://127.0.0.1:5000/price/

    Returns:
        str: json dict with 'data' key
    """
    if request.method == 'GET':
        global current_price
        return jsonify(data=current_price)
    elif request.method == 'POST':
        new_price = float(request.form.get('new_price'))
        current_price = new_price
        return jsonify(data=current_price)


@app.route('/register/', methods=['GET', 'POST'])
def register():
    """Get and update reservations
    POST: curl -d reservations=1 http://127.0.0.1:5000/register/
    GET: curl http://127.0.0.1:5000/register/

    Returns:
        str: json dict with 'data' key
    """
    if request.method == 'GET':
        global current_reservations
        return jsonify(data=current_reservations)
    elif request.method == 'POST':
        new_reservations = int(request.form.get('reservations'))
        current_reservations += new_reservations
        return jsonify(data=current_reservations)
