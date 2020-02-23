from modules.key_gen.key_gen import generate_key


class Client:

    def __init__(self):
        pass

    def sendMessage(self, text):
        """
        :param text:
        :return:
        """
        pass


def encrypt(text, closed_key):
    """
    Функция шифрования сообщений
    :param text: аргумент функции хранит текст сообщения
    :param closed_key: аргумент функции хранит закрытый ключ шифрования
    :return: функция возвращает открытый ключ (шифротекст)
    """
    open_key = []
    for i in text:
        open_key.append(ord(i) * closed_key)
    return open_key


def decrypt(open_key, closed_key):
    """
    Функция дешифровки сообщений
    :param open_key: аргумент функции хранит открытый ключ (шифротекст)
    :param closed_key: аргумент функции хранит закрытый ключ шифрования
    :return: функция возвращает расшифрованное сообщение
    """
    message = ''
    for i in open_key:
        let = int(i / closed_key)
        message += chr(let)
    return message


# main program
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
    closed_key = generate_key()
    print(f'Закрытый ключ создан\nclosed_key: {closed_key}')
    print('Сохранить локально? [y /n]', end=' ')
    if input().strip() == 'y':
        with open('closed_key.txt', 'w') as file:
            file.write(str(closed_key))
        print('Ключ сохранен')
