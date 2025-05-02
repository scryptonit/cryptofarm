from web3 import Web3

wallet_address = ""
wallet_address = Web3.to_checksum_address(wallet_address)

with open("rpc.txt", "r") as f:
    lines = [line.strip() for line in f if line.strip()]

for line in lines:
    chain_name, rpc_url = line.split(",")
    w3 = Web3(Web3.HTTPProvider(rpc_url))

    balance_wei = w3.eth.get_balance(wallet_address)
    balance_eth = w3.from_wei(balance_wei, 'ether')

    print(f"[] {chain_name}: {balance_eth} ETH")
