from cls.Message_cls import Message
import requests
from datetime import datetime


class Server:
	@staticmethod
	def user_is_created(username): # get 'http://api.mess.host/get/user_is_created?username=max'
		r = requests.get('http://api.mess.host/get/user_is_created', params={'username':username})
		if r:
			return True
		return False

	@staticmethod
	def create_user(username): # post http://api.mess.host/post/create_user data={username}
		r = requests.post('http://api.mess.host/post/create_user', data={'username':username})
		return None

	@staticmethod
	def create_chat(chat_id, user1, user2): # post http://api.mess.host/post/create_chat data={chat_id, user1, user2}
		r = requests.post('http://api.mess.host/post/create_chat', data={'chat_id': chat_id,'user1': user1,'user2':user2})
		return None

	@staticmethod
	def delete_chat(chat_id): # post http://api.mess.host/post/delete_chat data={chat_id}
		r = requests.post('http://api.mess.host/post/delete_chat', data={'chat_id':chat_id})
		return None

	@staticmethod
	def get_messages_from_chat(chat_id, initial): # get 'http://api.mess.host/get/get_messages_from_chat?chat_id=12345&initial=0'
		r = requests.get('http://api.mess.host/get/get_messages_from_chat', params={'chat_id':chat_id,'initial':initial})
		# messages = r.json()
		# return messages
		return [['07-03-2020', 12345, 'Dmitriy', [83125490032, 80727639358, 86322624264, 86322624264, 88720474938]]]

	@staticmethod
	def send_message(chat_id, username, text, closed_key): # post http://api.mess.host/post/send_message data={message}
		date = str(datetime.now())
		message = Message.encrypt([chat_id, date, username, text], closed_key)
		return None