import csv
from web3 import Web3
from twilio.rest import Client

# Infura and Web3 setup
INFURA_URL = "https://mainnet.infura.io/v3/xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
web3 = Web3(Web3.HTTPProvider(INFURA_URL))

# Twilio credentials
ACCOUNT_SID = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
AUTH_TOKEN = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
TWILIO_PHONE = "xxxxxxxxxxxx"
TO_PHONE = "xxxxxxxxxxxx"  # Your phone number

client = Client(ACCOUNT_SID, AUTH_TOKEN)

# Function to check suspicious transactions
def is_suspicious(tx):
    if tx["to"] is None:  # Contract creation (potential scam)
        return True
    if web3.from_wei(tx["value"], "ether") == 0:  # Zero value transactions
        return True
    return False

if web3.is_connected():
    latest_block = web3.eth.block_number
    block = web3.eth.get_block(latest_block, full_transactions=True)
    transactions = block.transactions

    print(f"Checking {len(transactions)} transactions for fraud...")

    suspicious_data = []

    for tx in transactions[:10]:  # Check first 10 transactions
        if is_suspicious(tx):
            tx_hash = tx.hash.hex()
            from_addr = tx["from"]
            to_addr = tx["to"]
            value_eth = web3.from_wei(tx["value"], "ether")

            print(f"\n🚨 Suspicious Transaction 🚨")
            print(f"Hash: {tx_hash}")
            print(f"From: {from_addr}")
            print(f"To: {to_addr}")
            print(f"Value: {value_eth} ETH")

            suspicious_data.append([tx_hash, from_addr, to_addr, value_eth])

            # Send SMS alert
            message = f"🚨 Suspicious Transaction Detected! 🚨\nHash: {tx_hash}\nFrom: {from_addr}\nTo: {to_addr}\nValue: {value_eth} ETH"
            client.messages.create(body=message, from_=TWILIO_PHONE, to=TO_PHONE)

    if suspicious_data:
        with open("suspicious_transactions.csv", "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Transaction Hash", "From", "To", "Value (ETH)"])
            writer.writerows(suspicious_data)
        print("\n✅ Suspicious transactions saved to suspicious_transactions.csv")
else:
    print("Connection failed!")
