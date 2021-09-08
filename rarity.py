from brownie import *
import csv
from threading import Event
import configparser

address = "0xce761D788DF608BD21bdd59d6f4B54b2e27F25Bb"
users = {}

def execute(acc, ids):
    print(f"Auto advanture with account: {acc}")
    latest_block_timestamp =  web3.eth.get_block(web3.eth.blockNumber).timestamp

    try:
        rarity = Contract(address, owner=users[acc])
    except:
        rarity = Contract.from_explorer(address, owner=users[acc])

    for id in ids:
        print(f"Adventure for {id}")
        try:
            _xp, _log, _class, _level = rarity.summoner(id)
        except:
            print(f"Error for {id} fetch summoner info, {e}")
            continue
        if latest_block_timestamp <= _log:
            print(f"Next adventure after {_log - latest_block_timestamp}s")
            continue
        try:
            ret = rarity.adventure(id)
            _xp, _log, _class, _level = rarity.summoner(id)
        except ValueError as e:
            print(f"Error for {id} adventure, {e}")
        try:
            if _xp >= rarity.xp_required(_level):
                ret = rarity.level_up(id)
        except ValueError as e:
            print(f"Error for {id} level_up, {e}")


def load_config():
    config = configparser.ConfigParser()
    config.read("config.ini")
    inteval = int(config['main']['inteval'])
    accs = [acc for acc in config['main']['accounts'].split(',') if acc.strip()]
    data = {}
    for acc in accs:
        if acc not in users:
            users[acc] = a.load(acc)
        data[acc] = []
        with open(config[acc]['summoner']) as f:
            for row in csv.reader(f):
                if row[6] != "TokenId" and row[8] == 'RM':
                    data[acc].append(int(row[6]))
    return inteval, data


# Take advanture for all of them!
def main():
    inteval, accs = load_config()
    e = Event()
    while True:
        for acc, ids in accs.items():
            execute(acc, ids)
        print(f"Waiting {inteval} minutes for next loop...")
        e.wait(inteval * 60)
