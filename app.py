from flask import Flask, jsonify, abort, url_for

app = Flask(__name__, static_url_path = "")


orders = [
    {
        'id': '1',
        'category': 'Chicken',
        'food_type': 'Chicken Biryani',
        'price': '$99',
        'delivery_time': '30/10/2018/14:30',
        'done': False
    },
    {
        'id': '2',
        'category': 'Chicken',
        'food_type': 'Chicken Biryani',
        'price': '$99',
        'delivery_time': '30/10/2018/14:30',
        'done': False
    },
    {
        'id': '3',
        'category': 'Chicken',
        'food_type': 'Chicken Biryani',
        'price': '$99',
        'delivery_time': '30/10/2018/14:30',
        'done': False
    },
    {
        'id': '4',
        'category': 'Chicken',
        'food_type': 'Chicken Biryani',
        'price': '$99',
        'delivery_time': '30/10/2018/14:30',
        'done': False
    }
]

def make_public_order(order):
    new_order = {}
    for field in order:
        if field == 'id':
            new_order['uri'] = url_for('get_order', order_id = order['id'], _external = True)
        else:
            new_order[field] = order[field]
    return new_order


@app.route('/api/v1/orders', methods = ['GET'])
def get_orders():
    return jsonify({'orders': list(map(make_public_order, orders))})

@app.route('/api/v1/orders/<int:order_id>', methods = ['GET'])
def get_order(order_id):
    order = filter(lambda t: t['id'] == order_id, orders)
    if len(order) == 0:
        abort(404)

    return jsonify( { 'order': make_public_order(order[0]) })


if __name__ == '__main__':
    app.run(debug=True)