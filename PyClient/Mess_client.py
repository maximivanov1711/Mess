import re
from cls.Thread_cls import Thread
from cls.Server_cls import Server
from cls.ChatList_cls import ChatList
from cls.Client_cls import Client
from cls.Message_cls import Message
from modules.generate_chat_id import generate_chat_id
from modules.generate_closed_key import generate_closed_key


# Основная программа

# Регистрация
print('...')
try:
    with open('username.txt') as file:
        username = file.read()
        assert re.match(r'^[\w\d]{5,30}$', username)
except (FileNotFoundError, AssertionError):
    ChatList.create()
    print('Регистрация...')
    while True:
        username = input('Введите имя > ').strip()
        if re.match(r'^[\w\d]{5,30}$', username):
            if not Server.user_is_created(username):
                with open('username.txt', 'w') as file:
                    file.write(username)
                Server.create_user(username)
                print('Регистрация прошла успешно')
                break
            else:
                print('Имя занято...')
        else:
            print('Неверное имя...')
finally:
    User = Client(username)
    print(f'Привет, {User.username}')

while True:
    inp = input().strip()
    if re.match(r'/.*/', inp):
        if inp.startswith('/connect/'): #/connect/ {username}
            attr = inp[9:].split()

            try:
                assert attr
            except AssertionError:
                print('Неверные аргументы...')
                continue

            # Атрибуты команды 
            username = attr[0]

            # Логика команды
            if ChatList.chat_is_created(username):
                chat_id = ChatList.get_chat(username)['chat_id']
                closed_key = ChatList.get_chat(username)['closed_key']
                t = Thread(username, chat_id, closed_key)
                t.start()
                while True:
                    inp = input().strip()
                    if inp != '/close/':
                        ChatList.update_initial(username, 1)
                        Server.send_message(chat_id, User.username, inp, closed_key)
                    else:
                        t.stop = True
                        break
            else:
                print('Такого чата нет...')

        elif inp.startswith('/add/'): # /add/ {username} {chat_id} {closed_key}
            attr = inp[5:].split()

            try:
                assert len(attr) >= 3
            except AssertionError:
                print('Неверные аргументы...')
                continue

            # Атрибуты команды 
            username = attr[0]
            chat_id = attr[1]
            closed_key = attr[2]

            # Логика команды
            if not ChatList.chat_is_created(username):
                if Server.user_is_created(username):
                    ChatList.create_chat(username, chat_id, closed_key)
                    Server.create_chat(chat_id, User.username, username)
                    print('Чат добавлен')
                else:
                    print('Такого пользователя не существует...')
            else:
                print('Чат с этим пользователем уже создан...')

        elif inp.startswith('/new/'): # /new/ {username}
            attr = inp[5:].split()

            try:
                assert attr
            except AssertionError:
                print('Неверные аргументы...')
                continue

            # Атрибуты команды 
            username = attr[0]

            # Логика команды
            if not ChatList.chat_is_created(username):
                if Server.user_is_created(username):
                    chat_id = generate_chat_id()
                    closed_key = generate_closed_key()
                    
                    ChatList.create_chat(username, chat_id, closed_key)
                    Server.create_chat(chat_id, User.username, username)
                    
                    print(f'Чат создан\nchat_id: {chat_id}\nclosed_key: {closed_key}')
                else:
                    print('Такого пользователя не существует...')
            else:
                print('Чат с этим пользователем уже создан...')

        elif inp.startswith('/get/'): # /get/ {username}
            attr = inp[5:].split()

            try:
                assert attr
            except AssertionError:
                print('Неверные аргументы...')
                continue

            # Атрибуты команды 
            username = attr[0]

            # Логика команды
            if ChatList.chat_is_created(username):
                print(ChatList.get_chat(username))
            else:
                print('Такого чата нет...')

        elif inp.startswith('/delete/'): # /delete/ {username}
            attr = inp[8:].split()

            try:
                assert attr
            except AssertionError:
                print('Неверные аргументы...')
                continue

            # Атрибуты команды 
            username = attr[0]

            # Логика команды
            if ChatList.chat_is_created(username):
                chat_id = ChatList.get_chat(username)['chat_id']
                ChatList.delete_chat(username)
                Server.delete_chat(chat_id)
                print('Чат удален')
            else:
                print('Такого чата нет...')
        
        elif inp == '/list/':
            # Логика команды
            if ChatList.list_chats():
                for chat in ChatList.list_chats():
                    print(chat)
            else:
                print('Нет чатов...')
            
        elif inp == '/exit/':
            exit()
        
        else:
            print('Такой команды не существует...')       
