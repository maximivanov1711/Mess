import json
from datetime import datetime


class ChatList:
    @staticmethod
    def create():
        with open('chatList.json', 'w') as file:
            json.dump({}, file)

    @staticmethod
    def chat_is_created(username):
        try:
            with open('./chatList.json') as file:
                chatlist = json.load(file)
        except FileNotFoundError:
            return False
        else:
            for i in chatlist.keys():
                if i == username:
                    return True
            return False

    @staticmethod
    def add_chat(username, chat_id, closed_key):
        try:
            with open('./chatList.json') as file:
                chatlist = json.load(file)
        except FileNotFoundError:
            chatlist = {
                username: {
                    'date': str(datetime.now()),
                    'chat_id': chat_id,
                    'closed_key': closed_key
                }
            }
        finally:
            chatlist[username] = {
                'date': str(datetime.now()),
                'chat_id': chat_id,
                'closed_key': closed_key
            }
            with open('./chatList.json', 'w') as file:
                json.dump(chatlist, file, indent=4, ensure_ascii=False)

    @staticmethod
    def get_chat(username):
        with open('./chatList.json') as file:
            chatlist = json.load(file)
        return chatlist[username]

    @staticmethod
    def delete_chat(username):
        with open('./chatList.json') as file:
            chatlist = json.load(file)
        del chatlist[username]
        with open('./chatList.json', 'w') as file:
            json.dump(chatlist, file, indent=4, ensure_ascii=False)

    @staticmethod
    def list_chats():
        try:
            with open('./chatList.json') as file:
                chatlist = json.load(file)
        except FileNotFoundError:
            return None
        else:
            return list(chatlist.keys())