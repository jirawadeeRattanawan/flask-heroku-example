"""Flask App Project."""

from flask import Flask, jsonify
app = Flask(__name__)


@app.route('/')
def index():
    """Return homepage."""
    json_data = {'Hello': 'World!'}
    return จิราวดี เลขที่21 ห้องม4/1


if __name__ == '__main__':
    app.run()
