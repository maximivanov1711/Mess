from .client.dialog_interface.dialog_interface import dialog_interface

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


dialog_interface()
