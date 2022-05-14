import pytest
from web3 import Web3, EthereumTesterProvider

w3 = Web3(Web3.HTTPProvider('http://127.0.0.1:8545'))

def test_blockchain_connected():
    assert(w3.isConnected())

def test_check_latest_block_exists():
    assert(w3.eth.get_block('latest'))
    print(w3.eth.get_block('latest'))

def test_blockchain_accounts_exist():
    assert len(w3.eth.accounts) > 0

def test_transfer_ether_works():
    account0 = w3.eth.accounts[0]
    account1 = w3.eth.accounts[1]
    assert account0
    assert account1
    balance0_before = w3.eth.get_balance(account0)
    balance1_before = w3.eth.get_balance(account1)
    TRANSFER_AMOUNT = 1
    assert balance0_before > TRANSFER_AMOUNT

    # Send some ether from one account to another
    w3.eth.send_transaction({
        'from': account0,
        'to': account1,
        'value': TRANSFER_AMOUNT
    })
    balance0_after = w3.eth.get_balance(account0)
    balance1_after = w3.eth.get_balance(account1)

    # Confirm the balances of both accounts have changed. Note that the values aren't necessarily
    # predictable due to the cost of gas for the transaction
    assert balance0_before != balance0_after
    assert balance1_before != balance1_after

