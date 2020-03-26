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
		try:
			response = requests.get('http://api.mess.host/get/user_is_created', params={'username':username})
		except Exception as e:
			logging.info(f'!ERROR! |user_is_created| {e}')
			raise e
		else:
			if response:
				logging.info(f'> :SERVER: |user_is_created| code={response.status_code}')
				return response
			elif response.status_code == 404:
				logging.info(f'> :SERVER: |user_is_created| code={response.status_code}')
				return response
			else:
				logging.info(f'> :SERVER: !ERROR! |user_is_created| code={response.status_code} response={response.text}')
				return response

	@staticmethod
	def create_user(username): # post http://api.mess.host/post/create_user data={username}
		logging.info(f'< :USER: <post> |create_user| username={username}')
		try:
			response = requests.post('http://api.mess.host/post/create_user', data={'username':username})
		except Exception as e:
			logging.info(f'!ERROR! |create_user| {e}')
			raise e
		else:
			if response:
				logging.info(f'> :SERVER: |create_user| code={response.status_code}')
				return response
			else:
				logging.info(f'> :SERVER: !ERROR! |create_user| code={response.status_code} response={response.text}')
				return response

	@staticmethod
	def delete_user(username): # post http://api.mess.host/post/delete_user data={username}
		logging.info(f'< :USER: <post> |delete_user| username={username}')
		try:
			response = requests.post('http://api.mess.host/post/delete_user', data={'username':username})
		except Exception as e:
			logging.info(f'!ERROR! |delete_user| {e}')
			raise e
		else:
			if response:
				logging.info(f'> :SERVER: |delete_user| code={response.status_code}')
				return response
			else:
				logging.info(f'> :SERVER: !ERROR! |delete_user| code={response.status_code} response={response.text}')
				return response

	@staticmethod
	def chat_is_created(chat_id): # get http://api.mess.host/get/chat_is_created?chat_id=12345
		logging.info(f'< :USER: <get> |chat_is_created| chat_id={chat_id}')
		try:
			response = requests.get('http://api.mess.host/get/chat_is_created', params={'chat_id':chat_id})
		except Exception as e:
			logging.info(f'!ERROR! |chat_is_created| {e}')
			raise e
		else:
			if response:
				logging.info(f'> :SERVER: |chat_is_created| code={response.status_code}')
				return response
			elif response.status_code == 404:
				logging.info(f'> :SERVER: |chat_is_created| code={response.status_code}')
				return response
			else:
				logging.info(f'> :SERVER: !ERROR! |chat_is_created| code={response.status_code} response={response.text}')
				return response

	@staticmethod
	def create_chat(chat_id, user1, user2): # post http://api.mess.host/post/create_chat data={chat_id, user1, user2}
		logging.info(f'< :USER: <post> |create_chat| chat_id={chat_id} user1={user1} user2={user2}')
		try:
			response = requests.post('http://api.mess.host/post/create_chat', data={'chat_id': chat_id,'user1': user1,'user2':user2})
		except Exception as e:
			logging.info(f'!ERROR! |create_chat| {e}')
			raise e
		else:
			if response:
				logging.info(f'> :SERVER: |create_chat| code={response.status_code}')
				return response
			else:
				logging.info(f'> :SERVER: !ERROR! |create_chat| code={response.status_code} response={response.text}')
				return response

	@staticmethod
	def delete_chat(chat_id): # post http://api.mess.host/post/delete_chat data={chat_id}
		logging.info(f'< :USER: <post> |delete_chat| chat_id={chat_id}')
		try:
			response = requests.post('http://api.mess.host/post/delete_chat', data={'chat_id':chat_id})
		except Exception as e:
			logging.info(f'!ERROR! |delete_chat| {e}')
			raise e
		else:
			if response:
				logging.info(f'> :SERVER: |delete_chat| code={response.status_code}')
				return response
			else:
				logging.info(f'> :SERVER: !ERROR! |delete_chat| code={response.status_code} response={response.text}')
				return response

	@staticmethod
	def get_messages_from_chat(chat_id, initial): # get http://api.mess.host/get/get_messages_from_chat?chat_id=12345&initial=0
		# try:
		# 	response = requests.get('http://api.mess.host/get/get_messages_from_chat', params={'chat_id':chat_id,'initial':initial})
		# except Exception as e:
		# 	logging.info(f'!ERROR! |get_messages_from_chat| {e}')
		# 	raise e
		# else:
		# 	if response:
		# 		logging.info(f'> :SERVER: |get_messages_from_chat| code={response.status_code}')
		# 		return response
		# 	else:
		#		logging.info(f'> :SERVER: !ERROR! |get_messages_from_chat| code={response.status_code} response={response.text}')
		# 		return response
		return [['07-03-2020', 12345, 'Dmitriy', [14455075648, 14038102312, 15011040096, 15011040096, 15428013432]]]

	@staticmethod
	def send_message(chat_id, username, text, closed_key): # post http://api.mess.host/post/send_message data={message}
		logging.info(f'< :USER: <post> |send_message| message={chat_id, date, username, text}')
		
		date = str(datetime.now())
		message = Message.encrypt([chat_id, date, username, text], closed_key)

		try:
			response = requests.post('http://api.mess.host/post/send_message', data={'message':message})
		except Exception as e:
			logging.info(f'!ERROR! |send_message| {e}')
			raise e
		else:
			if response:
				logging.info(f'> :SERVER: |send_message| code={response.status_code}')
				return response
			else:
				logging.info(f'> :SERVER: !ERROR! |send_message| code={response.status_code} response={response.text}')
				return response
		