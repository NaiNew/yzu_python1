class Account:
    name = ''
    __balance = 100

    def __str__(self):
        return self.name + ' 有 $' + str(self.__balance)

if __name__ == '__main__' :
    Account.bank = '元大銀行'
    acc = Account()
    acc.name = 'Edward'
    print(Account.bank, acc)
