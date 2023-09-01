from web3 import Web3
import csv
from tqdm import tqdm
from datetime import datetime
import time

INFURA_PROJECT_ID = 'CHANGE_ME'  # Replace with your Infura Project ID
CSV_FILE_NAME = 'new_wallets.csv'
FIELD_NAMES = ['PositionInBlock', 'Wallet', 'Block', 'Timestamp', 'ReadableTimestamp', 'AmountETH', 'TransactionHash']
BLOCKS_PER_DAY = 7146  # Approximate number of Ethereum blocks generated per day, adjust as needed

w3 = Web3(Web3.HTTPProvider(f'https://mainnet.infura.io/v3/{INFURA_PROJECT_ID}'))
seen_addresses = set()

def write_csv(data):
    with open(CSV_FILE_NAME, 'a', newline='') as csvfile:
        csv.DictWriter(csvfile, fieldnames=FIELD_NAMES).writerow(data)

def initialize_csv():
    with open(CSV_FILE_NAME, 'w', newline='') as csvfile:
        csv.DictWriter(csvfile, fieldnames=FIELD_NAMES).writeheader()

def scan_block(block_num):
    block = w3.eth.get_block(block_num, True)
    
    for position_in_block, tx in enumerate(block['transactions']):
        to_address = tx['to']
        if to_address is None or to_address in seen_addresses:
            continue
        
        seen_addresses.add(to_address)
        nonce = w3.eth.get_transaction_count(to_address, block_num)
        
        if nonce == 0:
            timestamp_readable = datetime.utcfromtimestamp(block['timestamp']).strftime('%Y-%m-%d %H:%M:%S')
            amount_eth = w3.from_wei(tx['value'], 'ether')
            
            tqdm.write(f"New Wallet: {to_address}, Position in Block: {position_in_block}, Block: {block['number']}, Timestamp: {block['timestamp']}, AmountETH: {amount_eth}, ReadableTimestamp: {timestamp_readable}, Transaction Hash: {tx['hash'].hex()}")
            
            write_csv({
                'PositionInBlock': position_in_block,
                'Wallet': to_address,
                'Block': block['number'],
                'Timestamp': block['timestamp'],
                'ReadableTimestamp': timestamp_readable,
                'AmountETH': amount_eth,
                'TransactionHash': tx['hash'].hex()
            })

if __name__ == '__main__':
    initialize_csv()
    latest_block = w3.eth.get_block('latest')['number']
    with tqdm(total=BLOCKS_PER_DAY, desc='Scanning blocks') as pbar:
        for block_number in range(latest_block - BLOCKS_PER_DAY, latest_block + 1):
            scan_block(block_number)
            pbar.update(1)
            #time.sleep(1) # You can uncomment this if you want to be nice!
