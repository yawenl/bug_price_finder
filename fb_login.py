from fbchat import Client
from fbchat.models import *
import sys
receiver_ids = []
#yawen_id = '100003776882239'
#beibin_id = '100000279995429'
login_id = ''
login_pwd = ''

def set_receiver_ids(receivers):
	global receiver_ids
	receiver_ids = receivers
def login(id, pwd):
	global login_id, login_pwd
	login_id = id
	login_pwd = pwd
	client = Client(login_id, login_pwd)

def send_message(message):
	for r in receiver_ids:
		client.sendMessage(massage, thread_id=r, thread_type=ThreadType.USER)

print('Own id: {}'.format(client.uid))

client.sendMessage('Hi me!', thread_id=yawen_id, thread_type=ThreadType.USER)
client.sendMessage('SB!', thread_id=beibin_id, thread_type=ThreadType.USER)


