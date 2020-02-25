import re
from cls.Client_cls.Client_cls import Client
from cls.Chat_cls.Chat_cls import Chat
from cls.Message_cls.Message_cls import Message
from modules.keyGen_module.keyGen_module import generate_key


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

        if inp.startswith('/connect/'): #/connect/ {chat_id, closed_key}
            try:
                attr = inp[9:].split()
                assert len(attr) == 2
                chat_id = int(attr[0])
                closed_key = int(attr[1])
            except (ValueError, AssertionError):
                print('неверный id или closed_key')
                continue
            else:
                MyChat = Chat(closed_key, chat_id)
                print(MyChat)

        elif inp == '/exit/':
            exit()

        else:
            print('Такой команды не существует...')
