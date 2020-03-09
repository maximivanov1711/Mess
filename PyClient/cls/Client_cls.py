class Client:
    def __init__(self, username):
        self.username = username

    def __repr__(self):
        return f'Client({self.username})'
        