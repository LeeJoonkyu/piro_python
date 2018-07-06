# TODO : implement WatingList.


class WaitingList(object):

    def __init__(self):
        self.list = []

    def add_customer(self, name):
        self.list.append(name)

    def print_current_list(self):
        for person in self.list:
            print(person, end= ' ')

    def pop_customer(self):
        name = self.list.pop(0)
        return name
