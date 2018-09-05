from flask import Flask

app = Flask(__name__)


orders = [
    {
        'id': '01',
        'category': 'Chicken',
        'food_type': 'Chicken Biryani',
        'price': '$99',
        'delivery_time': '30/10/2018/14:30',
        'done': False
    },
    {
        'id': '01',
        'category': 'Chicken',
        'food_type': 'Chicken Biryani',
        'price': '$99',
        'delivery_time': '30/10/2018/14:30',
        'done': False
    },
    {
        'id': '01',
        'category': 'Chicken',
        'food_type': 'Chicken Biryani',
        'price': '$99',
        'delivery_time': '30/10/2018/14:30',
        'done': False
    },
    {
        'id': '01',
        'category': 'Chicken',
        'food_type': 'Chicken Biryani',
        'price': '$99',
        'delivery_time': '30/10/2018/14:30',
        'done': False
    }
]



if __name__ == '__main__':
    app.run(debug=True)