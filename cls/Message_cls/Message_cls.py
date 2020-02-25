class Message:

    # в разработке!
    @staticmethod
    def send(open_key):
        pass


    @staticmethod
    def encrypt(text, closed_key):
        """
        Функция шифровки сообщений
        :param text: аргумент функции хранит текст сообщения
        :param closed_key: аргумент функции хранит закрытый ключ шифрования
        :return: функция возвращает зашифрованное сообщение (шифротекст)
        """
        open_key = []
        for i in text:
            open_key.append(ord(i) * closed_key)
        print(open_key)

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
