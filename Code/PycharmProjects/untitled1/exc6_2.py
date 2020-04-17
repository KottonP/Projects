class TelNumbers(object):
    def __init__(self):
        self.telnum = {}

    def add_numb(self, key, number):
        self.telnum.update({key: number})

    def print_num(self):
        for key in sorted(self.telnum):
            print("{} : {} ".format(key, self.telnum[key]))

    pass


x = TelNumbers()
x.add_numb("Andrew", 100000)
x.add_numb('Jonathan', 20000)
x.add_numb('Brian', 300000)
x.add_numb('Joseph', 40000)
x.add_numb('Kristian', 500000)
x.add_numb('Zero', 000000)
x.print_num()
