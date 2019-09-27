# It is for retrieve the CPChain addresses that have impeached blocks
# from a given block height to latest.
# The command is "python3 retrieveImpeach.py --bk=775000", 
# where 77500 can be a arbitrary positive integer smaller than the latest one.
# This script requires two labs, `fire` and `requests`.
# Please download it using pip3.
# Author: Wu Jiajing




from pprint import pprint
from _datetime import datetime
import requests
import json
import fire


def get_address(bk=770000):
    url = f'https://cpchain.io/explorer/impeachs_by_block/{bk}/0'
    r = requests.get(url)
    bks = json.loads(r.text).get('impeach_bks')
    li = []
    for i in range(len(bks)):
        time = datetime.fromtimestamp(bks[i]["timestamp"]).strftime("%Y-%m-%d %H:%M:%S")
        impeach_item = {"address": bks[i]['impeachProposer'], 'number': bks[i]['number'],
                        'time': time}
        li.append(impeach_item)
    print('total impeach number: ', len(li))

    li.reverse()
    pprint(li)


if __name__ == '__main__':
    fire.Fire(get_address)

