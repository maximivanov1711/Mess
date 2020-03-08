from cls.Message_cls import Message
import requests


class Server:
	@staticmethod
	def user_is_created(username):
		return True

	@staticmethod
	def create_user(username):
		pass

	@staticmethod
	def create_chat(chat_id, user1, user2):
		pass

	@staticmethod
	def delete_chat(chat_id):
		pass

	@staticmethod
	def get_messages_from_chat(chat_id, initial):
		return [['07-03-2020', 12345, 'Dmitriy', [82778892144, 80391039486, 85962695688, 85962695688, 88350548346]]]

	@staticmethod
	def send_message(chat_id, username, text, closed_key):
		message = Message.encrypt([chat_id, username, text], closed_key)
		print(message)