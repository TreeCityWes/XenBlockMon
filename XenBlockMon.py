import json
import requests
import time
import sys
from datetime import datetime

# THERE IS NO NEED TO EDIT THE SCRIPT. RUN THE SCRIPT AS IS! 

# Function to display banner
def display_banner():
    banner = """

██╗░░██╗███████╗███╗░░██╗  ██████╗░██╗░░░░░░█████╗░░█████╗░██╗░░██╗░██████╗
╚██╗██╔╝██╔════╝████╗░██║  ██╔══██╗██║░░░░░██╔══██╗██╔══██╗██║░██╔╝██╔════╝
░╚███╔╝░█████╗░░██╔██╗██║  ██████╦╝██║░░░░░██║░░██║██║░░╚═╝█████═╝░╚█████╗░
░██╔██╗░██╔══╝░░██║╚████║  ██╔══██╗██║░░░░░██║░░██║██║░░██╗██╔═██╗░░╚═══██╗
██╔╝╚██╗███████╗██║░╚███║  ██████╦╝███████╗╚█████╔╝╚█████╔╝██║░╚██╗██████╔╝
╚═╝░░╚═╝╚══════╝╚═╝░░╚══╝  ╚═════╝░╚══════╝░╚════╝░░╚════╝░╚═╝░░╚═╝╚═════╝░
    """
    print(banner)

# Function to query RPC
def send_rpc_request(method, params=None, request_id=1):
    headers = {'Content-Type': 'application/json'}
    payload = {
        "jsonrpc": "2.0",
        "id": request_id,
        "method": method,
        "params": params if params is not None else []
    }
    
    response = requests.post(RPC_URL, headers=headers, json=payload)
    if response.status_code == 200:
        return response.json()
    else:
        return None

# Constants for RPC and Custom Server URLs
RPC_URL = "http://xenminer.mooo.com:5555"
CUSTOM_SERVER_URL = "http://xenminer.mooo.com"

# Function to query custom server
def send_custom_request(endpoint, params=None):
    url = f"{CUSTOM_SERVER_URL}/{endpoint}"
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        return None

# Display banner
display_banner()

# Get account address from user
print(f"Enter ENS or wallet address.")
account = input("Please enter your XenBlocks account address: ").lower()

while True:
    # Initialize variables
    total_network_blocks = 0
    total_account_blocks = 0
    balance_xblk = 0

    # Query total number of blocks in the network
    response = send_rpc_request("eth_blockNumber")
    if response:
        total_network_blocks = int(response.get('result'), 16)  # Convert from hex to decimal

    # Query total number of blocks for the account
    response = send_custom_request("total_blocks2", {"account": account})
    if response:
        total_account_blocks = response.get('total_blocks')

    # Query balance of the account
    response = send_rpc_request("eth_getBalance", [account])
    if response:
        balance_wei = int(response.get('result'), 16)  # Convert from hex to decimal
        balance_xblk = balance_wei / 10**18  # Convert from Wei to X.BLK

    # Display all information
    print("\n🔥🔥🔥 XENBlock Mon 🔥🔥🔥")
    print(f"🌐 Network Name: XenBLOCKs")
    print(f"💻 RPC URL: {RPC_URL}")
    print(f"🕒 Current Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"🔗 Chain ID: 108016")
    print(f"💰 Currency: X.BLK")
    print(f"\n👤 Account Address: {account}")
    print(f"📊 Total number of blocks in the network: \033[93m{total_network_blocks}\033[0m")
    print(f"📈 Total number of blocks for account {account}: \033[93m{total_account_blocks}\033[0m")
    print(f"💸 Balance of account {account}: \033[93m{balance_xblk} X.BLK\033[0m")
    print("◼️" * 30)
    
    # Wait for 30 seconds before the next update
    print("Created by TreeCityWes.eth. Press CTRL+C to Exit.")

    # Countdown for next update on the same line
    sys.stdout.write("Next update in: ")
    for i in range(30, 0, -1):
        sys.stdout.write(f"\rNext update in: {i} seconds")
        sys.stdout.flush()
        time.sleep(1)
    print("\rRefreshing now... ")
