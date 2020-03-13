from cls.Thread_cls import Thread
from cls.Server_cls import Server
from cls.ChatList_cls import ChatList
from cls.Client_cls import Client
from cls.Message_cls import Message
from modules.generate_chat_id import generate_chat_id
from modules.generate_closed_key import generate_closed_key
from modules.validate_username import validate_username


# Основная программа

# Регистрация
print('...')
try:
    with open('username.txt') as file:
        username = file.read()
    assert validate_username(username)
except (FileNotFoundError, AssertionError):
    ChatList.create_chatlist()
    print('Регистрация...')
    while True:
        username = input('Введите имя > ').strip()
        if validate_username(username):
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
    if inp.startswith('/connect/'): #/connect/ {username}
        attribuеs = inp[9:].split()

        if not attribuеs:
            print('Неверные аргументы...')
            continue

        username = attribuеs[0]

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
        attribuеs = inp[5:].split()

        if len(attribuеs) < 3:
            print('Неверные аргументы...')
            continue

        username = attribuеs[0]
        chat_id = attribuеs[1]
        closed_key = attribuеs[2]

        if Server.user_is_created(username):
            if not ChatList.chat_is_created(username):
                ChatList.create_chat(username, chat_id, closed_key) 
                print('Чат добавлен')
            else:
                print('Чат с этим пользователем уже создан...')
        else:
            print('Такого пользователя не существует...')

    elif inp.startswith('/new/'): # /new/ {username}
        attribuеs = inp[5:].split()

        if not attribuеs:
            print('Неверные аргументы...')
            continue

        username = attribuеs[0]

        if Server.user_is_created(username):
            if not ChatList.chat_is_created(username):
                chat_id = generate_chat_id()
                closed_key = generate_closed_key()
                ChatList.create_chat(username, chat_id, closed_key)
                Server.create_chat(chat_id, User.username, username)
                print(f'Чат создан\nchat_id: {chat_id}\nclosed_key: {closed_key}')
            else:
                print('Чат с этим пользователем уже создан...')
        else:
            print('Такого пользователя не существует...')

    elif inp.startswith('/get/'): # /get/ {username}
        attribuеs = inp[5:].split()

        if not attribuеs:
            print('Неверные аргументы...')
            continue

        username = attribuеs[0]

        if ChatList.chat_is_created(username):
            print(ChatList.get_chat(username))
        else:
            print('Такого чата нет...')

    elif inp.startswith('/delete/'): # /delete/ {username}
        attribuеs = inp[8:].split()

        if not attribuеs:
            print('Неверные аргументы...')
            continue

        username = attribuеs[0]

        if ChatList.chat_is_created(username):
            chat_id = ChatList.get_chat(username)['chat_id']
            ChatList.delete_chat(username)
            Server.delete_chat(chat_id)
            print('Чат удален')
        else:
            print('Такого чата нет...')

    elif inp == '/list/':
        list_chats = ChatList.get_list_chats()
        if list_chats:
            for chat in list_chats:
                print(chat)
        else:
            print('Нет чатов...')

    elif inp == '/exit/':
        exit()

    else:
        print('Такой команды не существует...')
