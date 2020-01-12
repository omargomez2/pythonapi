from flask import Flask, jsonify
from flask_cors import CORS, cross_origin
import requests

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/api/v1/btcusd', methods=['GET'])
@cross_origin()
def ticker():

    url = "https://api.gdax.com/products/BTC-USD/ticker"
    data = requests.get(url).json()

    price = data['price']
    volume= data['volume']

    return jsonify(price=price, volume=volume)

if __name__ == '__main__':
    app.run()
