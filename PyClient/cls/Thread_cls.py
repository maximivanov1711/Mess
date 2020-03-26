from .Server_cls import Server
from .ChatList_cls import ChatList
from .Message_cls import Message
import threading
import logging
import time


logging.basicConfig(
	level=logging.INFO,
	filename='./server.log',
	filemode='w',
	format='%(message)s'
)


class Thread(threading.Thread):
	def __init__(self, username, chat_id, closed_key):
		threading.Thread.__init__(self)
		self.username = username
		self.chat_id = chat_id
		self.closed_key = closed_key
		self.initial = ChatList.get_chat(username)['initial']
		self.stop = False
	
	def run(self):
		while True:
			time.sleep(3)

			if self.stop:
				break

			try:
				response = Server.get_messages_from_chat(self.chat_id, self.initial)
			except Exception as e:
				print('ERROR', e)
				continue
			else:
				if response:
					messages = response.json()
				elif response.status_code == 404:
					continue
				else:
					print('SERVER ERROR', response.status_code, response.text)
					continue
			
			# decoding
			messages = list(map(Message.decrypt, messages, [self.closed_key] * len(messages)))
			# formating
			messages = list(map(Message.format, messages))

			for message in messages:
				logging.info(f'> :SERVER: |NEW MESSAGE| {message}')
				print(message)

			self.initial += len(messages)
			ChatList.update_initial(self.username, len(messages))	
