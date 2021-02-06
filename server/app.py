from flask import Flask, jsonify

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret-key-goes-here'


@app.route('/health')
def health():
    return jsonify(message='Up and running', code=200)


if __name__ == '__main__':
    app.run()
