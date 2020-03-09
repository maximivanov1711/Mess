from cls.Message_cls import Message
import requests


class Server:
	@staticmethod
	def user_is_created(username): # get 'http://api.mess.host/get/user_is_created?username=max'
		return True

	@staticmethod
	def create_user(username): # post http://api.mess.host/post/create_user data={username}
		pass

	@staticmethod
	def create_chat(chat_id, user1, user2): # post http://api.mess.host/post/create_chat data={chat_id, user1, user2}
		pass

	@staticmethod
	def delete_chat(chat_id): # post http://api.mess.host/post/delete_chat data={chat_id}
		pass

	@staticmethod
	def get_messages_from_chat(chat_id, initial): # get 'http://api.mess.host/get/get_messages_from_chat?chat_id=12345&initial=0'
		return [['07-03-2020', 12345, 'Dmitriy', [82778892144, 80391039486, 85962695688, 85962695688, 88350548346]]]

	@staticmethod
	def send_message(chat_id, username, text, closed_key): # post http://api.mess.host/post/send_message data={chat_id, date, username, open_key}
		message = Message.encrypt([chat_id, username, text], closed_key)
		print(message)