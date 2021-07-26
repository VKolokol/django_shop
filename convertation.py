import json

obj = {'product': [
    {'id': 1, 'category': 1, 'title': 'Led Zeppelin 2', 'price': 2000},
    {'id': 2, 'category': 1, 'title': 'Led Zeppelin 3', 'price': 4000},
    {'id': 3, 'category': 3, 'title': 'Korn Issues', 'price': 500},
    {'id': 4, 'category': 3, 'title': 'Korn Follow the Leader', 'price': 600},
    {'id': 5, 'category': 2, 'title': 'Audio-Technica AT-LPW30', 'price': 29000},
    {'id': 6, 'category': 2, 'title': 'LSony PS-HX500', 'price': 36000}]}


with open('mainapp/db.json', 'w') as data:
    json.dump(obj, data)
