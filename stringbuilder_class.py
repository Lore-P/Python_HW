class StringBuilder:
    def __init__(self):
        self.items = ["Once ", "upon ", "a ", "time, "]

    def add(self, item):
        self.items.append(item)

    def remove(self):
        self.items.pop()

    def to_string(self):
        '''
        It converts this class into a string
        :return:
        '''
        to_return = ''
        for item in self.items:
            to_return = to_return + item
        return to_return