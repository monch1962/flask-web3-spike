# flask-web3-spike
Spike to play with Flask &amp; web3

## To use

Update everything, including Python 3

`$ sudo apt-get update && sudo apt-get upgrade && sudo apt-get install python3`

Then start a local blockchain running

`$ cd blockchain && npm install -g ganache && ganache-cli`

Now start a new terminal, and install the Python libraries

`$ pip install -r requirements.txt`

Then test Python connectivity to the blockchain

`$ python test_web3.py`

Then start the app server running

`$ FLASK_APP=app.py flask run`

Then hit a URL

`$ curl http://localhost:8545/blockNumber`