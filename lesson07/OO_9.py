class Book:
    def __getattr__(self, name):
        try:
            return object.__getattribute__(name)
        except:
            return name + ' is not found!'

b = Book()
print(b.bookname)
b.bookname = 'Python'
b.price = 500
print(b.bookname, b.price)
