from flask import Flask, jsonify
from flask_web3 import current_web3, FlaskWeb3

# Declare Flask application
app = Flask(__name__)

# Set Flask-Web3 configuration
app.config.update({'ETHEREUM_PROVIDER': 'http', 'ETHEREUM_ENDPOINT_URI': 'http://127.0.0.1:8545'})

# Declare Flask-Web3 extension
web3 = FlaskWeb3(app=app)

# Declare route
@app.route('/blockNumber')
def block_number():
    return jsonify({'data': current_web3.eth.blockNumber})