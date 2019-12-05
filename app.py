from flask import Flask, request, jsonify

app = Flask(__name__)

current_price = float(1)
current_reservations = 0


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
