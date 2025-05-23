"""
This function converts hex private key generated by hdwallet into Phantom
    wallet compatible keypair.

Can be used if something goes wrong and manually need to send transaction 
"""

import base58
from solders.keypair import Keypair
from solathon.keypair import Keypair as solkeypair

def hex_to_keypair(hex_key):
    temp_keypair = solkeypair.from_private_key(base58.b58encode(bytes.fromhex(hex_key)).decode('utf-8'))
    public_key_bytes = bytes(temp_keypair.public_key)
    hex_key = bytes.fromhex(hex_key) + public_key_bytes
    hex_key = base58.b58encode(hex_key).decode('utf-8')
    return Keypair.from_base58_string(hex_key)

hex_secret_key = '067623f74a9f60722205faa45bfe00a88a6b'

# Convert and print the Keypair for Phantom Wallet
keypair = hex_to_keypair(hex_secret_key)
print(f'Phantom Compatible private key: {keypair}')
