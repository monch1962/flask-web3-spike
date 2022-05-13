# flask-web3-spike
Spike to play with Flask &amp; web3

## To use
First start a local blockchain running

`$ cd blockchain && npm install ganache && ganache-cli`

Then test Python connectivity to the blockchain

`$ python test_web3.py`

Then start the app server running

`$ FLASK_APP=app.py flask run`

Then hit a URL

`$ curl http://localhost:8545/blockNumber`