#!/usr/bin/python3

import rocketchat
import argparse
import datetime


parser = argparse.ArgumentParser()
parser.add_argument('--rcuser', help='The username used with rocketchat, Only needs to be set once.')
parser.add_argument('--rcpass', help='The password used with rocketchat. Only needs to be set once.')
parser.add_argument('--rchost', help='Chat host to use for API access')
parser.add_argument('--install', help='create config file on this machine for access, pass --rcuser (user@domain.com) --rcpass (rcpassword)  and --rchost http://chat.domain.com',action='store_true')
parser.add_argument('--channel', help='channel to send to/operate on')
parser.add_argument('--group', help='group to send to/operate on')
parser.add_argument('--user', help='user to send to/operate on')
parser.add_argument('--whoami', help='test of connection to rocketchat api', action='store_true')
parser.add_argument('--delete', help='delete messages from group or channel', action='store_true')
parser.add_argument('--verbose', help='enable more logging to console')
parser.add_argument('--send', help='text to send to room, user, or channel', action='store_true')
parser.add_argument('--iknow', help='required for deletion of messages.', action='store_true')
parser.add_argument('--text', help='text to send to room, user, or channel')
parser.add_argument('--trash',help='user with --iknow to spam a room with messages, mainly used for testing', action='store_true')
args = parser.parse_args()


# store variables
whoami = args.whoami
text = args.text
user = args.user
group = args.group
channel = args.channel
sendmsg = args.send
install = args.install
rcuser = args.rcuser
rcpass = args.rcpass
rchost = args.rchost
verbose = args.verbose
iknow = args.iknow
delete = args.delete
now = datetime.datetime.now()
trash = args.trash

# first setup, creates local file with config data defaults.
if install == True:
    if rcuser != None:
        if rcpass != None:
            if rchost != None:
                rocketchat.create_creds_file(rcuser,rcpass)
                rocketchat.configure(domain=rchost)
                if verbose == True:
                    print("storing config")
                rocketchat.store_config()

# prints basic info about logged in bot user, used to test config
if whoami == True:
    print(rocketchat.models.User.me)


#send message code
if sendmsg == True:
    if channel != None:
        if text != None:
            myroom = rocketchat.channels()[channel]
            myroom.send(text)
    if user != None:
        if text != None:
            users = rocketchat.users()
            foo = users[user]
            foo.send(text)
            #users[user].send(text)
    if group != None:
        if text != None:
            mygroup = rocketchat.groups()[group]
            mygroup.send(text)

# channel cleaning
if iknow == True:
    if delete == True:
        if channel != None:
            while True:
                try:
                    myroom = rocketchat.channels()[channel]
                    message = myroom.messages.last[0]
                    message.delete()
                except:
                    myroom.send("Room cleaned: " + str(now))
                    break
                
        if group != None:
            while True:
                try:
                    myroom = rocketchat.groups()[group]
                    message = myroom.messages.last[0]
                    message.delete()
                except:
                    myroom.send("Room cleaned: " + str(now) )
                    break

# room trashers for testing deletes
if trash == True:
    if channel != None:
        if iknow == True:
            count = 0
            mychannel = rocketchat.channels()[channel]
            while True:
                print(count)
                mychannel.send('*testmessage* ' + str(count))
                count += 1
                if count == 3000:
                    mychannel.send('room successfully trashed')
                break

    if group != None:
        if iknow == True:
            count = 0
            mygroup = rocketchat.groups()[group]
            while True:
                print(count)
                mygroup.send('*testmessage* ' + str(count))
                count += 1
                if count == 3000:
                    mygroup.send('room successfully trashed')
                    if verbose == True:
                        print('room trashed successfully!')
                    break                    
