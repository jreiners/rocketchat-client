# rocketchat-client

```

first install example:
./rc-client.py --install --rcuser rocketchatuser --rcpass rocketchatpass --rchost http://chat.reiners.io

delete messages from channel:
./rc-client.py --delete --iknow --channel general

delete messages from room:
./rc-client.py --delete --iknow --group mygroup

send a message to a group:
./rc-client.py --send --group mygroup --text "Hello there"

send a message to a channel:
./rc-client.py --send --channel general --text "Hello there"

send a message to a user:
/.rc-client.py --send --user username --text "Hello there"

fill a channel with test messages:

./rc-client.py --trash --channel general 

file a group with test messages:

./rc-client.py --trash --group mygroup
```
