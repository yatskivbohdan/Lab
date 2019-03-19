class A:
    def __init__(self, *args):
        if type(args)==list:
            self.data = args
        else:
            self.data = list(args)
        self.evens = self.evens()
        self.odds = self.odds()
    def evens(self):
        lst = []
        for el in self.data:
            if el % 2 == 0:
                lst.append(el)
        lst.sort()
        return lst
    def odds(self):
        lst = []
        for el in self.data:
            if el % 2 != 0:
                lst.append(el)
        return lst
    def __eq__(self, other):
        if isinstance(other, self.__class__):
            if self.evens == other.evens:
                return True
            else:
                return False

    def  __str__(self):
        return "A(evens={},odds={})".format(str(self.evens), str(self.odds))

    def clearOdds(self):
        self.odds = []
    def clearedOdds(self):
        self.new = A(self.data)
        return



class B(A):
    def __init__(self, a, b):
        super().__init__(*args)
        for i in range(a, b+1):
            self.data.append(i)
    def shifted(self, num):
        for el in self.odds():
            el += num
        for el in self.evens():
            el += num


a1 = A(1, 2, 3)