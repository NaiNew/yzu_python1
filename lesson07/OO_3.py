class Account:
    name = ''
    __balance = 100

    def __str__(self):
        return self.name + '有 $' + str(self.__balance)

if __name__ == '__main__' :
    acc = Account()
    acc.name = 'Edward'
    print(acc)
