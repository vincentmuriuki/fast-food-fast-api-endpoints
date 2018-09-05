from flask import Flask, jsonify, abort, url_for, request

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

@app.route('/api/v1/orders', methods = ['POST'])
def create_order():
    if not request.json or not 'category' in request.json:
        abort(400)
    order = {
        'id': orders[-1]['id'] + 1,
        'category': request.json['category'],
        'food_type': request.json.get('food_type', ""),
        'price': request.json.get['price'],
        'delivery_time': request.json.get('delivery_time'),
        'done': False
    }
    orders.append(order)
    return jsonify({ 'order': make_public_order(order) }), 201



@app.route('/api/v1/orders/<int:order_id>', methods = ['PUT'])
def update_order(order_id):
    order = filter(lambda t: t['id'] == order_id, orders)
    if len(order) == 0:
        abort(404)
    if not request.json:
        abort(400)
    if 'category' in request.json and type(request.json['category']) != unicode:
        abort(400)
    if 'food_type' in request.json and type (request.json['food_type']) is not unicode:
        abort(400)

    if 'done' in request.json and type(request.json['done']) is not bool:
        abort(400)

    order[0]['category'] = request.json.get('category', order[0]['category'])
    order[0]['food_type'] = request.json.get('food_type', order[0]['food_type'])
    order[0]['price'] = request.json.get('price', order[0]['price'])
    order[0]['delivery_time'] = request.json.get('delivery_time', order[0]['delivery_time'])
    order[0]['done'] = request.json.get('done', order[0]['done'])
    return jsonify( { 'order': make_public_order(order[0]) })



@app.route('/api/v1/orders/<int:order_id>', methods = ['DELETE'])
def delete_order(order_id):
    order = filter(lambda t: t['id'] == order_id, orders)
    if len(order) == 0:
        abort(404)
    orders.remove(order[0])
    return jsonify( { 'result': True } )


if __name__ == '__main__':
    app.run(debug=True)