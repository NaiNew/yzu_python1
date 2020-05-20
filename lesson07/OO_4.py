class Father:
    money = 0
    def __init__(self, money):
        self.money = money

class Son(Father):
    age = 0
    def __init__ (self, money, age):
        Father.__init__(self, money)
        self.age = age

if __name__ == '__main__':
    son = Son(50000, 10)
    print(son.money, son.age)

