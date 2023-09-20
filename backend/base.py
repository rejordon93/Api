from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app, origins="http://localhost:3000")


@app.route('/profile')
def my_profile():
    response_body = {
        "name": "Ethan",
        "about": "Hello! I'm a full stack developer who enjoys working with Python and Flask."
    }

    return response_body


if __name__ == '__main__':
    app.run(debug=True)
