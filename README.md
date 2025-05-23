# Crypto TG Bot
 This Python bot acts as a mediator between product sellers and buyers on Telegram. It securely holds cryptocurrency in a wallet (stored in a database) and releases payment to the seller upon mutual approval from both parties.
 
Try the bot at: [Here](https://t.me/Escrow_shield_bot)

![License](https://img.shields.io/badge/license-MIT-blue) 

![Python](https://img.shields.io/badge/Python-v3.9.8-blue)

## Features

- **Escrow Service:** Users can start escrow service and the bot will generate a wallet to receive funds for the transaction. The funds are held until both parties confirm they are satisfied with the exchange. No manual intervention is required to release or hold the funds.

- **Shop Setup:** Sellers can set up shop items with either automatic or manual key/product delivery system. Funds are automatically released to the seller upon successful delivery.

- **Broker Service:** Brokers can start a trade which will give them the agreed portion of the trade. In this process identity of seller and buyer remain anonymous to one another and only broker knows them.

- **Wallet Security:** Crypto wallets are generated and stored in a MySQL database in an encrypted state. No external services are used to manage the wallets.

- **Supported Networks:**
   - Solana
   - Litecoin
   - Dogecoin
   - BSC (BEP-20)

- **Planned Networks:**

   - Tron (TRC-20)
   - TON

- **Excluded Networks:**

   - Bitcoin (due to high fees and slow transaction times)

I’m open to discussions on which networks to add and how to make this bot better and easier to use.

## Installation
Needs [Python version 3.9.8](https://www.python.org/downloads/release/python-398/) to be installed

1. Clone the repository:
   ```bash
   git clone https://github.com/vladashistory/TGBot.git
   ```
2. Navigate to the project directory:
   ```bash
   cd Crypto-Escrow-Telegram-Bot
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Install a extra library
   ```bash
   pip install solathon==1.0.7
   ```

5. edit `example.env`:

   - Get bot token from [Botfather](https://t.me/BotFather)
   
   - Get Blockcypher API key from [here](https://accounts.blockcypher.com/)
   
   **Note:** PRIVATE_KEY, SOLANA_FEE_PAYER_SECRET and BSC_FEE_PAYER_SECRET will be generated upon the first run. Be sure to save these values securely.

   ```python
   BOT_TOKEN = '73777777:jFc4Tvs0bM' # Get this from Bot Father
   BLOCK_CYPHER_API_TOKEN = '' # Free one works just fine | Will be used to push DOGE and LTC transactions
   PRIVATE_KEY = 'not_set'
   SOLANA_FEE_PAYER_SECRET = 'not_set' #used to pay tx fee for USDT on SOLANA network
   BSC_FEE_PAYER_SECRET = 'not_set' #used to pay tx fee for USDT on BSC network
   ```
   Add Mysql Database Credentials
   ```Python
   #MYSQL credential below 
   ENABLEDB = True
   HOST = "192.168.29.69"
   PORT = 33042
   USER = "root"
   PASSWORD = "cnOlZnSgv"
   DATABASE = "cryptoescrow"
   ```

6. Mysql Setup

   Use phpmyadmin or mysql terminal to run the commands in `db.sql` to create tables

7. edit `admin.config`

   Add information about bot like: owner id, fee wallet details in this file

8. Start the bot

   Rename `example.env` to `.env` and you are good to go for starting the bot
   ```bash
   python escrowBot.py
   ```
## Donation Section?! Damnn

Feel free to support development:

- **BTC:** bc1q2zlqujfvrauvge8t33wtm6xp4akuw5u0l9jn34

- **BSC:** 0xFB96DA72ecF2382b562219545CC8329823e119fA

- **SOL:** 54QdnQKAY1QbPZAfAn3YCnYLNuJVTgyArLvPGUB8X7Ag
