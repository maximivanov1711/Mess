import re
from cls.Data_cls.Data_cls import Data
from cls.Client_cls.Client_cls import Client
from cls.Message_cls.Message_cls import Message
from modules.generate_closed_key.generate_closed_key import generate_closed_key
from modules.generate_chat_id.generate_chat_id import generate_chat_id

# main program

# username
print('...')
try:
    with open('username.txt') as file:
        User = Client(file.read())
        assert len(User.userName) > 0
        print(f'Привет, {User.userName}')
except (FileNotFoundError, AssertionError):
    while True:
        username = input('Введите ваше имя...\n').strip()
        if 10 >= len(username) > 0:
            with open('username.txt', 'w') as file:
                User = Client(username)
                file.write(username)
            print('Сохранено')
            break
        else:
            print('Имя должно содержать не больше 10 символов')
            continue
print(User)
while True:
    inp = input().strip()
    if re.match(r'/.*/', inp):
        if inp.startswith('/connect/'): #/connect/ {chat_id}
            pass

        elif inp.startswith('/new/'): # /new/ {username}
            attr = inp[5:].split() #comand attributes

            try:
                assert attr
            except AssertionError:
                print('Неверные аргументы')
                continue

            # attributes
            username = attr[0]

            if not Data.is_created(username):
                chat_id = generate_chat_id()
                closed_key = generate_closed_key()
                Data.add_chat(username, chat_id, closed_key)
            else:
                print('Чат с этим пользователем уже создан')

        elif inp.startswith('/get/'): # /get/ {username}
            attr = inp[5:].split() #comand attributes

            try:
                assert attr
            except AssertionError:
                print('Неверные аргументы')
                continue

            # attributes
            username = attr[0]

            if Data.is_created(username):
                print(Data.get_chat(username))
            else:
                print('Такого чата нет')

        elif inp.startswith('/delete/'): # /delete/ {username}
            attr = inp[8:].split() #comand attributes

            try:
                assert attr
            except AssertionError:
                print('Неверные аргументы')
                continue

            # attributes
            username = attr[0]

            if Data.is_created(username):
                Data.delete_chat(username)
                print('Чат удален')
            else:
                print('Такого чата нет')
        
        elif inp == '/list/':
            print(*Data.list_chats())
            
        elif inp == '/exit/':
            exit()
        
        else:
            print('Такой команды не существует...')        
