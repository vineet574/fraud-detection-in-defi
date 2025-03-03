from web3 import Web3  

INFURA_URL = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"  
web3 = Web3(Web3.HTTPProvider(INFURA_URL))  

if web3.is_connected():  
    latest_block = web3.eth.block_number  
    print(f"Latest Block: {latest_block}")  

    block = web3.eth.get_block(latest_block, full_transactions=True)  
    transactions = block.transactions  

    print(f"Number of Transactions: {len(transactions)}")  

    for tx in transactions[:5]:  # Fetch first 5 transactions  
        print(f"\nTransaction Hash: {tx.hash.hex()}")  
        print(f"From: {tx['from']}")  
        print(f"To: {tx['to']}")  
        print(f"Value: {web3.from_wei(tx['value'], 'ether')} ETH")  
else:  
    print("Connection failed!")  
