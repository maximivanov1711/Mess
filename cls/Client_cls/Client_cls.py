class Client:
    def __init__(self, userName):
        self.userName = userName

    def __repr__(self):
        return f'Client({self.userName})'