import requests


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
