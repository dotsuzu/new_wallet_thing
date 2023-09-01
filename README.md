# New Wallet Scanner for Ethereum

## Overview

This Python script scans the Ethereum blockchain for new wallet addresses that have been funded in the last 24 hours. It uses the Web3.py library for interacting with the Ethereum blockchain and Infura as the Ethereum node provider. The identified new wallets, along with various associated metadata, are saved to a CSV file.

## Features

- Scans Ethereum blocks for newly funded wallets
- Writes details to a CSV file, including wallet address, block number, timestamp, readable timestamp, amount in ETH, and transaction hash
- Displays progress with a tqdm progress bar

## Requirements

- Python 3.x
- Web3.py (`pip install web3`)
- tqdm (`pip install tqdm`)

## Setup

1. **Infura Project ID**: Sign up for an [Infura account](https://www.infura.io/) and create a new project in the dashboard. Replace `'CHANGE_ME'` in `INFURA_PROJECT_ID` with your actual project ID.
2. **CSV File**: Data will be saved in a file named `new_wallets.csv`. You can change the name in the script if you wish.
3. **Blocks Per Day**: The variable `BLOCKS_PER_DAY` is set to 7146 as an approximation. Adjust this number as needed based on current actual Ethereum block times.

## Usage

1. Initialize your Python environment and install the required packages.
    ```bash
    pip install web3 tqdm
    ```
2. Run the script.
    ```bash
    python new_wallet.py
    ```

## Code Structure

- `write_csv(data)`: Writes a row to the CSV file.
- `initialize_csv()`: Initializes the CSV file by writing the header.
- `scan_block(block_num)`: Scans a given block for newly funded wallets.

## Notes

- The script keeps track of the wallets it has already seen to avoid duplicate entries.
- The script sleeps for 1 second between each block scan by default. You can uncomment the sleep line if you wish.

## Example Output

The script outputs information about new wallets to the terminal as well as to the CSV file. Here's an example line from the CSV:

```
PositionInBlock,Wallet,Block,Timestamp,ReadableTimestamp,AmountETH,TransactionHash
1,0x1234...,1234567,1632163230,2023-09-21 00:00:30,0.5,0xdeadbeef...
```

## License

Feel free to use, modify, and distribute this code as you see fit. Attribution is appreciated but not required.
