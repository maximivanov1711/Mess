class Message:

    @staticmethod
    def send(text, closed_key):
        """
        Функция отправки сообщения
        :param text: аргумент функции хранит текст сообщения
        :param closed_key: аргумент функции хранит закрытый ключ шифрования
        :return: функция возвращает открытый ключ (шифротекст)
        """
        open_key = []
        for i in text:
            open_key.append(ord(i) * closed_key)

    @staticmethod
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
