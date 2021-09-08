# Rarity automation

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
6. Run the automation script with this command:
```bash
brownie run rarity.py --network ftm-main
```