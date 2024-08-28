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
   git clone https://github.com/glazybyte/Crypto-Escrow-Telegram-Bot.git
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
2024-07-14T04:04:53 Commit 1 of 2024-07-14
2024-07-15T16:03:10 Commit 1 of 2024-07-15
2024-07-15T22:32:54 Commit 2 of 2024-07-15
2024-07-16T23:34:32 Commit 1 of 2024-07-16
2024-07-16T08:25:23 Commit 2 of 2024-07-16
2024-07-16T19:03:07 Commit 3 of 2024-07-16
2024-07-17T10:38:15 Commit 1 of 2024-07-17
2024-07-17T06:27:50 Commit 2 of 2024-07-17
2024-07-17T11:04:00 Commit 3 of 2024-07-17
2024-07-18T17:04:44 Commit 1 of 2024-07-18
2024-07-19T01:15:34 Commit 1 of 2024-07-19
2024-07-19T01:34:30 Commit 2 of 2024-07-19
2024-07-20T13:30:47 Commit 1 of 2024-07-20
2024-07-21T17:42:43 Commit 1 of 2024-07-21
2024-07-22T04:01:01 Commit 1 of 2024-07-22
2024-07-22T17:31:58 Commit 2 of 2024-07-22
2024-07-22T06:16:58 Commit 3 of 2024-07-22
2024-07-23T11:19:41 Commit 1 of 2024-07-23
2024-07-23T11:02:29 Commit 2 of 2024-07-23
2024-07-23T17:55:53 Commit 3 of 2024-07-23
2024-07-24T13:42:14 Commit 1 of 2024-07-24
2024-07-24T04:43:24 Commit 2 of 2024-07-24
2024-07-24T08:59:23 Commit 3 of 2024-07-24
2024-07-25T18:34:09 Commit 1 of 2024-07-25
2024-07-25T14:08:43 Commit 2 of 2024-07-25
2024-07-26T06:44:28 Commit 1 of 2024-07-26
2024-07-26T13:54:14 Commit 2 of 2024-07-26
2024-07-26T17:17:08 Commit 3 of 2024-07-26
2024-07-27T23:58:53 Commit 1 of 2024-07-27
2024-07-14T14:15:25 Commit 1 of 2024-07-14
2024-07-14T09:29:04 Commit 2 of 2024-07-14
2024-07-14T08:50:45 Commit 3 of 2024-07-14
2024-07-15T05:25:27 Commit 1 of 2024-07-15
2024-07-16T05:17:42 Commit 1 of 2024-07-16
2024-07-17T21:13:36 Commit 1 of 2024-07-17
2024-07-17T16:01:18 Commit 2 of 2024-07-17
2024-07-17T18:36:15 Commit 3 of 2024-07-17
2024-07-18T06:45:11 Commit 1 of 2024-07-18
2024-07-18T20:02:46 Commit 2 of 2024-07-18
2024-07-18T18:33:14 Commit 3 of 2024-07-18
2024-07-19T16:27:14 Commit 1 of 2024-07-19
2024-07-20T10:05:36 Commit 1 of 2024-07-20
2024-07-21T03:26:12 Commit 1 of 2024-07-21
2024-07-21T18:13:15 Commit 2 of 2024-07-21
2024-07-22T08:07:14 Commit 1 of 2024-07-22
2024-07-22T11:20:32 Commit 2 of 2024-07-22
2024-07-23T15:15:52 Commit 1 of 2024-07-23
2024-07-23T14:23:22 Commit 2 of 2024-07-23
2024-07-24T16:14:38 Commit 1 of 2024-07-24
2024-07-24T08:37:17 Commit 2 of 2024-07-24
2024-07-24T11:38:38 Commit 3 of 2024-07-24
2024-07-25T18:29:21 Commit 1 of 2024-07-25
2024-07-25T08:47:50 Commit 2 of 2024-07-25
2024-07-25T06:56:13 Commit 3 of 2024-07-25
2024-07-26T10:35:33 Commit 1 of 2024-07-26
2024-07-26T22:38:38 Commit 2 of 2024-07-26
2024-07-27T00:26:48 Commit 1 of 2024-07-27
2024-07-27T23:44:14 Commit 2 of 2024-07-27
2024-07-28T09:01:15 Commit 1 of 2024-07-28
2024-07-29T00:25:14 Commit 1 of 2024-07-29
2024-07-30T01:02:03 Commit 1 of 2024-07-30
2024-07-31T02:47:12 Commit 1 of 2024-07-31
2024-07-31T03:17:52 Commit 2 of 2024-07-31
2024-07-31T20:39:24 Commit 3 of 2024-07-31
2024-08-01T10:10:25 Commit 1 of 2024-08-01
2024-08-02T11:33:24 Commit 1 of 2024-08-02
2024-08-03T14:40:55 Commit 1 of 2024-08-03
2024-08-03T09:06:17 Commit 2 of 2024-08-03
2024-08-03T06:49:23 Commit 3 of 2024-08-03
2024-08-04T20:11:03 Commit 1 of 2024-08-04
2024-08-04T13:15:44 Commit 2 of 2024-08-04
2024-08-04T06:59:19 Commit 3 of 2024-08-04
2024-08-05T00:54:13 Commit 1 of 2024-08-05
2024-08-05T20:23:12 Commit 2 of 2024-08-05
2024-08-05T21:38:17 Commit 3 of 2024-08-05
2024-08-06T00:12:42 Commit 1 of 2024-08-06
2024-08-06T13:27:26 Commit 2 of 2024-08-06
2024-08-06T09:35:09 Commit 3 of 2024-08-06
2024-08-07T14:12:16 Commit 1 of 2024-08-07
2024-08-07T07:07:34 Commit 2 of 2024-08-07
2024-08-07T07:48:36 Commit 3 of 2024-08-07
2024-08-08T23:09:38 Commit 1 of 2024-08-08
2024-08-09T00:30:25 Commit 1 of 2024-08-09
2024-08-09T20:53:57 Commit 2 of 2024-08-09
2024-08-09T09:08:05 Commit 3 of 2024-08-09
2024-08-10T15:41:58 Commit 1 of 2024-08-10
2024-08-10T01:00:33 Commit 2 of 2024-08-10
2024-08-11T10:24:14 Commit 1 of 2024-08-11
2024-08-11T10:53:38 Commit 2 of 2024-08-11
2024-08-11T07:24:22 Commit 3 of 2024-08-11
2024-08-12T18:32:44 Commit 1 of 2024-08-12
2024-08-12T01:29:52 Commit 2 of 2024-08-12
2024-08-12T16:51:03 Commit 3 of 2024-08-12
2024-08-13T07:37:41 Commit 1 of 2024-08-13
2024-08-13T18:59:57 Commit 2 of 2024-08-13
2024-08-14T16:45:17 Commit 1 of 2024-08-14
2024-08-14T02:24:07 Commit 2 of 2024-08-14
2024-08-15T13:14:24 Commit 1 of 2024-08-15
2024-08-15T21:31:56 Commit 2 of 2024-08-15
2024-08-16T15:55:50 Commit 1 of 2024-08-16
2024-08-17T12:42:54 Commit 1 of 2024-08-17
2024-08-18T17:28:28 Commit 1 of 2024-08-18
2024-08-18T16:19:49 Commit 2 of 2024-08-18
2024-08-19T22:30:48 Commit 1 of 2024-08-19
2024-08-19T23:03:15 Commit 2 of 2024-08-19
2024-08-19T06:09:29 Commit 3 of 2024-08-19
2024-08-20T04:05:47 Commit 1 of 2024-08-20
2024-08-20T12:23:47 Commit 2 of 2024-08-20
2024-08-21T23:00:06 Commit 1 of 2024-08-21
2024-08-21T02:47:08 Commit 2 of 2024-08-21
2024-08-21T15:01:11 Commit 3 of 2024-08-21
2024-08-22T02:28:46 Commit 1 of 2024-08-22
2024-08-22T18:52:11 Commit 2 of 2024-08-22
2024-08-23T12:18:15 Commit 1 of 2024-08-23
2024-08-24T15:32:49 Commit 1 of 2024-08-24
2024-08-24T07:45:18 Commit 2 of 2024-08-24
2024-08-25T17:27:45 Commit 1 of 2024-08-25
2024-08-26T16:27:25 Commit 1 of 2024-08-26
2024-08-26T15:56:24 Commit 2 of 2024-08-26
2024-08-26T07:53:47 Commit 3 of 2024-08-26
2024-08-27T18:25:20 Commit 1 of 2024-08-27
2024-08-27T04:24:21 Commit 2 of 2024-08-27
2024-08-27T09:00:25 Commit 3 of 2024-08-27
2024-08-28T11:41:11 Commit 1 of 2024-08-28
2024-08-28T09:19:12 Commit 2 of 2024-08-28
