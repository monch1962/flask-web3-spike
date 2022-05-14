from flask import Flask, jsonify
#from flask_web3 import current_web3, FlaskWeb3
from web3 import Web3#, EthereumTesterProvider

# Declare Flask application
app = Flask(__name__)

w3 = Web3(Web3.HTTPProvider('http://127.0.0.1:8545'))

# Set Flask-Web3 configuration
app.config.update({'ETHEREUM_PROVIDER': 'http', 'ETHEREUM_ENDPOINT_URI': 'http://127.0.0.1:8545'})

# Declare Flask-Web3 extension
#web3 = FlaskWeb3(app=app)
class MyApp():
    def __init__(self):
        app = Flask(app=app)
        return app

    # Declare route
    @app.route('/blockNumber')
    def block_number():
        return jsonify({'data': current_web3.eth.blockNumber})
    
    @app.route('/version', methods=['GET'])
    def version():
        return jsonify({'version': 0.001})