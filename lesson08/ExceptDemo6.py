class LoginException(Exception):
    def __int__(self, *args: object) -> None:
        super().__init__(*args)

    def __str__(self) -> str:
        return super().__str__()

    def howToDo(self):
        print('請重新輸入')
        print('若能無法登入請電洽XX-XXXX-XXXX')
        