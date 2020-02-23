import random


class Client:

    def __init__(self):
        pass

    def sendMessage(self, text):
        pass


def encrypt(text, closed_key):
    open_key = []
    for i in text:
        open_key.append(ord(i) * closed_key)
    return open_key


def decrypt(open_key, closed_key):
    message = ''
    for i in open_key:
        let = int(i / closed_key)
        message += chr(let)
    return message


print('...')
print('Создан ли ключ? [y / n]', end=' ')
if input().strip() == 'y':
    while True:
        print('Введите закрытый ключ...')
        try:
            closed_key = int(input().strip())
            break
        except ValueError:
            print('Попробуйте еще раз... ключ должен содержать только цифры')
            continue
else:
    closed_key = random.randint(10000, 1000000000)
    print(f'Закрытый ключ создан\nclosed_key: {closed_key}')
    print('Сохранить локально? [y /n]', end=' ')
    if input().strip() == 'y':
        with open('closed_key.txt', 'w') as file:
            file.write(str(closed_key))
        print('Ключ сохранен')
while True:
    break