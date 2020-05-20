class Salary:
    def __init__(self, name, monry):
        self.name = name
        self.money = monry
    def __str__(self):
        return self.name + ' ' + str(self.money)
    def __add__(self, n):
        self.money = self.money + n

if __name__ == '__main__':
    s1 = Salary('Mary', 40000)
    s2 = Salary('Jhon', 50000)
    print(s1, s2)
    s1 + 5000
    s2 + 6000
    print(s1, s2)