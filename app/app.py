from flask import Flask, jsonify, request
import jwt
import datetime

app = Flask(__name__)

app.config['SECRET_KEY'] = 'devopskey'


@app.route('/login', methods=['POST'])
def login():

    token = jwt.encode(
        {
            'user': 'admin',
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
        },
        app.config['SECRET_KEY'],
        algorithm='HS256'
    )

    with open("/logs/access.log", "a") as f:
        f.write("TOKEN GENERATED\n")

    return jsonify({'token': token})


@app.route('/secure', methods=['GET'])
def secure():

    auth = request.headers.get('Authorization')

    with open("/logs/access.log", "a") as f:
        f.write("SECURE API HIT\n")

    return jsonify({'message': 'Secure API Accessed'})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
