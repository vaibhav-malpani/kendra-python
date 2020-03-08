from flask import Flask, request
from flask_cors import CORS
from kendra import Kendra
app = Flask(__name__)
cors = CORS(app)


@app.route('/', methods=['POST'])
def response():
    query = request.get_json()['query']
    query_response = Kendra().query(query)
    return query_response


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)