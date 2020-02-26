import json
from datetime import datetime


class Data:
    @staticmethod
    def is_created(username):
        try:
            with open('./data.json') as file:
                data = json.load(file)
        except FileNotFoundError:
            return False
        else:
            for i in data.keys():
                if i == username:
                    return True
            return False

    @staticmethod
    def add_chat(username, chat_id, closed_key):
        try:
            with open('./data.json') as file:
                data = json.load(file)
        except FileNotFoundError:
            data = {
                username: {
                    'date': str(datetime.now()),
                    'chat_id': chat_id,
                    'closed_key': closed_key
                }
            }
        finally:
            data[username] = {
                'date': str(datetime.now()),
                'chat_id': chat_id,
                'closed_key': closed_key
            }
            with open('./data.json', 'w') as file:
                json.dump(data, file, indent=4)


    @staticmethod
    def get_chat(username):
        with open('./data.json') as file:
            data = json.load(file)
        return data[username]

    @staticmethod
    def delete_chat(username):
        with open('./data.json') as file:
            data = json.load(file)
        del data[username]
        with open('./data.json', 'w') as file:
            json.dump(data, file, indent=4)

    @staticmethod
    def list_chats():
        try:
            with open('./data.json') as file:
                data = json.load(file)
        except FileNotFoundError:
            return None
        else:
            return list(data.keys())