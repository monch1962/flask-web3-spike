from web3 import Web3, EthereumTesterProvider
w3 = Web3(Web3.HTTPProvider('http://127.0.0.1:8545'))
print('Connected?: %s ' % w3.isConnected())
print('Latest block: %s' % w3.eth.get_block('latest'))
print('Accounts: %s' % w3.eth.accounts)

first_account = w3.eth.accounts[0]
second_account = w3.eth.accounts[1]
transfer_amount = 12345

print('Balance of account %s is %d' % (first_account, w3.eth.get_balance(first_account)))
print('Balance of account %s is %d' % (second_account, w3.eth.get_balance(second_account)))


print('Transferring %d from %s to %s' % (transfer_amount, first_account, second_account))
w3.eth.send_transaction({
    'from': first_account,
    'to': second_account,
    'value': 12345
})

print('Balance of account %s is %d' % (first_account, w3.eth.get_balance(first_account)))
print('Balance of account %s is %d' % (second_account, w3.eth.get_balance(second_account)))