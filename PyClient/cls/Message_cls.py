class Message:
    @staticmethod
    def format(message):
        date = message[0]
        user = message[2]
        text = message[3]
        message = f'{date} | {user}: {text}'
        return message

    @staticmethod
    def encrypt(message, closed_key):
        open_key = []
        text = message[3]
        for i in text:
            open_key.append(ord(i) * closed_key)
        message[3] = open_key
        return message

    @staticmethod
    def decrypt(message, closed_key):
        open_key = message[3]
        text = ''
        for i in open_key:
            let = int(i / closed_key)
            text += chr(let)
        message[3] = text
        return message
