from cls.Server_cls import Server
import random


def generate_chat_id():
	while True:
		chat_id = random.randint(10000, 99999)
		if Server.chat_is_created(chat_id):
			continue
		break
	return chat_id