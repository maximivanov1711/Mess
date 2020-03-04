import re
from cls.Thread_cls.Thread_cls import Printer 
from cls.ChatList_cls.ChatList_cls import ChatList
from cls.Client_cls.Client_cls import Client
from cls.Message_cls.Message_cls import Message
from modules.generate_closed_key.generate_closed_key import generate_closed_key
from modules.generate_chat_id.generate_chat_id import generate_chat_id


# main program

ChatList.create() # create chatList.json

# registration
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
            with open('username.txt', 'w') as file:
                file.write(username)
            print('Регистрация прошла успешно')
            break
        else:
            print('Неверное имя...')
else:
    User = Client(username)
    print(f'Привет, {User.userName}')

while True:
    inp = input().strip()
    if re.match(r'/.*/', inp):
        if inp.startswith('/connect/'): #/connect/ {chat_id}
            attr = inp[9:].split()

            try:
                assert attr
            except AssertionError:
                print('Неверные аргументы...')
                continue

            # attributes
            username = attr[0]
            
            if ChatList.chat_is_created(username):
                t = Printer('thread')
                t.start()
                while True:
                    inp = input().strip()
                    if inp == '/close/':
                        t.stop = True
                        break
            else:
                print('Такого чата нет...')

        elif inp.startswith('/new/'): # /new/ {username}
            attr = inp[5:].split() #comand attributes

            try:
                assert attr
            except AssertionError:
                print('Неверные аргументы...')
                continue

            # attributes
            username = attr[0]

            if not ChatList.chat_is_created(username):
                chat_id = generate_chat_id()
                closed_key = generate_closed_key()
                ChatList.add_chat(username, chat_id, closed_key)
                print('Чат создан')
            else:
                print('Чат с этим пользователем уже создан...')

        elif inp.startswith('/get/'): # /get/ {username}
            attr = inp[5:].split() #comand attributes

            try:
                assert attr
            except AssertionError:
                print('Неверные аргументы...')
                continue

            # attributes
            username = attr[0]

            if ChatList.chat_is_created(username):
                print(ChatList.get_chat(username))
            else:
                print('Такого чата нет...')

        elif inp.startswith('/delete/'): # /delete/ {username}
            attr = inp[8:].split() #comand attributes

            try:
                assert attr
            except AssertionError:
                print('Неверные аргументы...')
                continue

            # attributes
            username = attr[0]

            if ChatList.chat_is_created(username):
                ChatList.delete_chat(username)
                print('Чат удален')
            else:
                print('Такого чата нет...')
        
        elif inp == '/list/':
            if ChatList.list_chats():
                for chat in ChatList.list_chats():
                    print(chat)
            else:
                print('Нет чатов...')
            
        elif inp == '/exit/':
            exit()
        
        else:
            print('Такой команды не существует...')        
