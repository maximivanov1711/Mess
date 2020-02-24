from cls.Client.Client import Client
from cls.Chat.Chat import Chat
from cls.Message.Message import Message
from modules.key_gen.key_gen import generate_key


# main program

# username
print('...')
try:
    with open('username.txt') as file:
        User = Client(file.read())
        assert len(user.userName) > 0
        print(f'Привет, {user.userName}')
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

# closed_key
print('Создан ли ключ? [y / n]', end=' ')
if input().strip() == 'y':
    while True:
        print('Введите закрытый ключ...')
        try:
            closed_key = int(input().strip())
            assert len(str(closed_key)) <= 50
            Chat = Chat(closed_key)
            break
        except (ValueError, AssertionError):
            print('Попробуйте еще раз... ключ должен содержать только цифры')
            continue
else:
    Chat = Chat(generate_key())
    print(f'Закрытый ключ создан\nclosed_key: {closed_key}')
    print('Сохранить локально? [y /n]', end=' ')
    if input().strip() == 'y':
        with open('closed_key.txt', 'w') as file:
            file.write(str(closed_key))
        print('Ключ сохранен')
