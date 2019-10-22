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
    addr = {}
    for i in range(len(bks)):
        time = datetime.fromtimestamp(bks[i]["timestamp"]).strftime("%Y-%m-%d %H:%M:%S")
        impeach_item = {"address": bks[i]['impeachProposer'], 'number': bks[i]['number'],
                        'time': time}
        if impeach_item['address'] not in addr:
            addr[impeach_item['address']] = 1
        else:
            addr[impeach_item['address']] +=1
        li.append(impeach_item)

    li.reverse()
    pprint(li)
    print("*"*100)

    pprint(sorted(addr.items(),key=lambda x:x[1],reverse=True))

    print('total impeach number: ', len(li))


if __name__ == '__main__':
    fire.Fire(get_address)

