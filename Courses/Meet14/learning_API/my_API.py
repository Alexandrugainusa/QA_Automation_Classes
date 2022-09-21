from flask import Flask, jsonify, request

server_port = 5000
app = Flask(__name__)

app.config['DEBUG'] = True

list_users = [
    {
        'name': 'Jon',
        'email': 'Jon@xml.ro',
        'salary': 4000
    },
    {
        'name': 'Alex',
        'email': 'Alex@alex.ro',
        'salary': 5000
    }
]


@app.route('/')
def get_users():
    return list_users[0]


@app.route('/users')
def get_all_users():
    return jsonify(
        {
            'users': list_users
        }
    )


@app.route('/users', methods=['POST'])
def add_user():
    usr = request.get_json()
    for u in list_users:
        if u['email'] == usr['email']:
            return f'{usr["email"]} is taken', 200
    else:
        list_users.append(usr)
        return f'{usr} is added', 201


@app.route('/users', methods=['DELETE'])
def delete_user():
    usr = request.get_json()
    for u in list_users:
        if u['email'] == usr['email']:
            list_users.remove(u)
    return f'{usr["email"]} is deleted', 410


@app.route('/users', methods=['PUT'])
def update_user():
    usr = request.get_json()
    for u in list_users:
        if u['email'] == usr['email']:
            u['salary'] = usr['salary']
            return f'{usr["salary"]} is updated', 201
    else:
        return f'{usr} not found', 200


if __name__ == '__main__':
    app.run('localhost', port=server_port, debug=True)
