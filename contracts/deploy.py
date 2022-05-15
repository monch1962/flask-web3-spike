import json
from web3 import Web3
from solc import compile_files, link_code, compile_source
# web3.py instance
w3 = Web3(Web3.HTTPProvider('http://127.0.0.1:8545'))

def deploy_contract(contract_interface):
    tx_hash = w3.eth.contract(
        abi=contract_interface['abi'],
        bytecode=contract_interface['bin']).constructor().transact()

    address = w3.eth.get_transaction_receipt(tx_hash)['contractAddress']
    return address

# compile all contract files
contracts = compile_files(['user.sol', 'stringUtils.sol'])

# separate main file and link file
main_contract = contracts.pop('user.sol:userRecords')
library_link = contracts.pop('stringUtils.sol:StringUtils')

# print bin part in console you will see ‘stringUtils’ in that we need to link library address in that bin code.
# to that we have to deploy library code first then link it
library_address = {
    'stringUtils.sol:StringUtils': deploy_contract(library_link)
}
main_contract['bin'] = link_code(
    main_contract['bin'], library_address)

# add abi(application binary interface) and transaction reciept in json file
with open('data.json', 'w') as outfile:
    data = {
        'abi': main_contract['abi'],
        'contract_address': deploy_contract(main_contract)
    }
json.dump(data, outfile, indent=4, sort_keys=True)
