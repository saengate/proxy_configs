from flask import Flask, jsonify, make_response

app = Flask(__name__)


@app.route('/test_api/', methods=['GET'])
def test_api():
    data = {'message': 'Done', 'code': 'SUCCESS'}
    return make_response(jsonify(data), 201)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=9000)
