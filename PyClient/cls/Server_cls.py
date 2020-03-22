from cls.Message_cls import Message
import requests
import logging
from datetime import datetime


logging.basicConfig(
	level=logging.INFO,
	filename='./server.log',
	filemode='w',
	format='%(message)s'
)


class Server:
	@staticmethod
	def user_is_created(username): # get http://api.mess.host/get/user_is_created?username=max
		logging.info(f'< :USER: <get> |user_is_created| username={username}')
		r = requests.get('http://api.mess.host/get/user_is_created', params={'username':username})
		logging.info(f'> :SERVER: |user_is_created| username={username} code={r.status_code}')
		if r:
			return True
		return True

	@staticmethod
	def create_user(username): # post http://api.mess.host/post/create_user data={username}
		logging.info(f'< :USER: <post> |create_user| username={username}')
		r = requests.post('http://api.mess.host/post/create_user', data={'username':username})
		logging.info(f'> :SERVER: |create_user| username={username} code={r.status_code}')
		return r

	@staticmethod
	def delete_user(username): # post http://api.mess.host/post/delete_user data={username}
		logging.info(f'< :USER: <post> |delete_user| username={username}')
		r = requests.post('http://api.mess.host/post/delete_user', data={'username':username})
		logging.info(f'> :SERVER: |delete_user| username={username} code={r.status_code}')
		return r

	@staticmethod
	def chat_is_created(chat_id): # get http://api.mess.host/get/chat_is_created?chat_id=12345
		logging.info(f'< :USER: <get> |chat_is_created| chat_id={chat_id}')
		r = requests.get('http://api.mess.host/get/chat_is_created', params={'chat_id':chat_id})
		logging.info(f'> :SERVER: |chat_is_created| chat_id={chat_id} code={r.status_code}')
		if r:
			return True
		return False

	@staticmethod
	def create_chat(chat_id, user1, user2): # post http://api.mess.host/post/create_chat data={chat_id, user1, user2}
		logging.info(f'< :USER: <post> |create_chat| chat_id={chat_id} user1={user1} user2={user2}')
		r = requests.post('http://api.mess.host/post/create_chat', data={'chat_id': chat_id,'user1': user1,'user2':user2})
		logging.info(f'> :SERVER: |create_chat| chat_id={chat_id} user1={user1} user2={user2} code={r.status_code}')
		return r

	@staticmethod
	def delete_chat(chat_id): # post http://api.mess.host/post/delete_chat data={chat_id}
		logging.info(f'< :USER: <post> |delete_chat| chat_id={chat_id}')
		r = requests.post('http://api.mess.host/post/delete_chat', data={'chat_id':chat_id})
		logging.info(f'> :SERVER: |delete_chat| chat_id={chat_id} code={r.status_code}')
		return r

	@staticmethod
	def get_messages_from_chat(chat_id, initial): # get http://api.mess.host/get/get_messages_from_chat?chat_id=12345&initial=0
		r = requests.get('http://api.mess.host/get/get_messages_from_chat', params={'chat_id':chat_id,'initial':initial})
		# messages = r.json()
		# return messages
		return [['07-03-2020', 12345, 'Dmitriy', [14455075648, 14038102312, 15011040096, 15011040096, 15428013432]]]

	@staticmethod
	def send_message(chat_id, username, text, closed_key): # post http://api.mess.host/post/send_message data={message}
		date = str(datetime.now())
		logging.info(f'< :USER: <post> |send_message| message={chat_id, date, username, text}')
		message = Message.encrypt([chat_id, date, username, text], closed_key)
		r = requests.post('http://api.mess.host/post/send_message', data={'message':message})
		logging.info(f'> :SERVER: |send_message| message={chat_id, date, username, text} code={r.status_code}')
		return r
		