class Chat:

    def __init__(self, id, closed_key):
        self.id = id
        self.closed_key = closed_key

    def __repr__(self):
        return f'Chat({self.id}, {self.closed_key})'
