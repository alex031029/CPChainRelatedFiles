It is for retrieve the CPChain addresses that have impeached blocks from a given block height to latest.

The command is 
```shell
python3 retrieveImpeach.py --bk=775000
```
, where 77500 can be an arbitrary positive integer smaller than the latest one. This command will return all information about the impeached blocks including their proposers between blocks 77500 and the latest, as well as a statistical analysis about all impeached block proposers.

This script requires two labs, `fire` and `requests`. Please download it using pip3.


Author: Wu Jiajing
