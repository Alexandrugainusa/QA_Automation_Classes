from flask import Flask, jsonify

server_port = 5000
app = Flask(__name__)

app.config['DEBUG'] = True

list_users = [
    {
        'name': 'Jon',
        'email': 'Jon@xml.ro'
    },
    {
        'name': 'Alex',
        'email': 'Alex@alex.ro'
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


if __name__ == '__main__':
    app.run('localhost', port=server_port, debug=True)
