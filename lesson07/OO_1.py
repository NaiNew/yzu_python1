class Human:
    name = ''
    age = 0
    sex = ''

    def __str__(self):
        return self.name + ' ' + self.sex + ' ' + str(self.age)

if __name__ == '__main__':
    h = Human()
    h.name = 'Edward'
    h.sex = '男'
    h.age = 27
    print(h.name, h.sex, h.age)
    print(h)
