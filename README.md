# Rarity automation

## Basic settings
1. Clone the repo:
```bash
git clone https://github.com/snowtigersoft/rarity.git
```
2. Folow https://eth-brownie.readthedocs.io/en/stable/install.html to install brownie
3. Download your Erc721 Txns from https://ftmscan.com/, if you have more than one accounts, you need download for each account.
4. Setup your account with its private key, you can add as many accounts as you like.
```bash
brownie accounts new <account_name>
```
5. Add your accounts to "config.ini" file, each account in a section, section is the account_name, "summoner" property set to the path of the downloaded filename from step 3.

## Run the automation script with this command:
It will auto adventure, level_up and collect_gold
```bash
brownie run rarity.py --network ftm-main
```

## Collect gold manually:
```bash
brownie run rarity.py collect_gold --network ftm-main
```