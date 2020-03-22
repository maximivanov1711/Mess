from cls.Thread_cls import Thread
from cls.Server_cls import Server
from cls.ChatList_cls import ChatList
from cls.Client_cls import Client
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
        
        try:
            request = Server.user_is_created(username)
        except Exception as e:
            print(e)
        else:
            if request:
                print('Имя занято...')
                continue
            else:
                print('ERROR', request.status_code)

        if not validate_username(username):
            print('Неправильное имя...')
            continue
        
        try:
            request = Server.create_user(username)
        except Exception as e:
            print(e)
        else:
            if request:
                with open('username.txt', 'w') as file:
                    file.write(username)
                print('Регистрация прошла успешно')
            else:
                print('ERROR', request.status_code) 
finally:
    User = Client(username)
    print(f'Привет, {User.username}')

# Основная программа
while True:
    inp = input().strip()
    if inp.startswith('/connect/'): #/connect/ {username}
        attribuеs = inp[9:].split()

        if not attribuеs:
            print('Неверные аргументы...')
            continue

        username = attribuеs[0]

        if not ChatList.chat_is_created(username):
            print('Такого чата нет...')
            continue

        chat_id = ChatList.get_chat(username)['chat_id']
        closed_key = ChatList.get_chat(username)['closed_key']
        
        t = Thread(username, chat_id, closed_key)
        t.start()
        
        while True:
            inp = input().strip()
            
            if inp == '/close/':
                t.stop = True
                break

            try:
                request = Server.send_message(chat_id, User.username, inp, closed_key)
            except Exception as e:
                print(e)
            else:
                if request:
                    ChatList.update_initial(username, 1)
                    print('Успешно!')
                else:
                    print('ERROR', request.status_code)

    elif inp.startswith('/add/'): # /add/ {username} {chat_id} {closed_key}
        attribuеs = inp[5:].split()

        if len(attribuеs) < 3:
            print('Неверные аргументы...')
            continue

        username = attribuеs[0]
        chat_id = attribuеs[1]
        closed_key = attribuеs[2]

        try:
            request = Server.user_is_created(username)
        except Exception as e:
            print(e)
            continue
        else:
            if not request:
                print('Такого пользователя не существует...')
                continue
            else:
                print('ERROR', request.status_code)

        if not ChatList.chat_is_created(username):
            ChatList.create_chat(username, chat_id, closed_key) 
            print('Чат добавлен')
        else:
            print('Чат с этим пользователем уже создан...')

    elif inp.startswith('/new/'): # /new/ {username}
        attribuеs = inp[5:].split()

        if not attribuеs:
            print('Неверные аргументы...')
            continue

        username = attribuеs[0]

        try:
            request = Server.user_is_created(username)
        except Exception as e:
            print(e)
            continue
        else:
            if not request:
                print('Такого пользователя не существует...')
                continue

        if ChatList.chat_is_created(username):
            print('Чат с этим пользователем уже создан...')
            continue

        chat_id = generate_chat_id()
        closed_key = generate_closed_key()
        
        ChatList.create_chat(username, chat_id, closed_key)
        try:
            request = Server.create_chat(chat_id, User.username, username)
        except Exception as e:
            print(e)
        else:
            if request:
                print(f'Чат создан\nchat_id: {chat_id}\nclosed_key: {closed_key}')
            else:
                print('ERROR', request.status_code)

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

        if not ChatList.chat_is_created(username):
            print('Такого чата нет...')
            continues

        chat_id = ChatList.get_chat(username)['chat_id']
        
        ChatList.delete_chat(username)
        try:
            request = Server.delete_chat(chat_id)
        except Exception as e:
            print(e)
        else:
            if request:
                print('Чат удален')
            else:
                print('ERROR', request.status_code)

    elif inp == '/list/': # /list/
        list_chats = ChatList.get_list_chats()
        if list_chats:
            for chat in list_chats:
                print(chat)
        else:  
            print('Нет чатов...')

    elif inp == '/exit/': # /exit/
        exit()

    else:
        print('Такой команды не существует...')
