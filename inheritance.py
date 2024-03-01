# A class's ability to inherit methods and characteristics from another class is known as inheritance.
# The subclass or a child class is a class that inherits. A parent class is the class from which methods
# and/or attributes are inherited.


class Book:
    def __init__(self, title, quantity, author, price):
        self.title = title
        self.quantity = quantity
        self.author = author
        self.__price = price
        self.__discount = None

    def set_discount(self, discount):
        self.__discount = discount

    def get_price(self):
        if self.__discount:
            return self.__price * (1-self.__discount)
        return self.__price

    def __repr__(self):
        return f"Book: {self.title}, Quantity: {self.quantity}, Author: {self.author}, Price: {self.get_price()}"
    
class Novel(Book):
    def __init__(self, title, quantity, author, price, pages):
        super().__init__(title,quantity, author, price)
        self.pages = pages 

class Academic(Book):
    def __init__(self, title, quantity, author, price, branch):
        super().__init__(title, quantity, author, price)
        self.branch = branch

novel1 = Novel('Two States', 20, 'Chetan Bhagat', 200, 187)
novel1.set_discount(0.20)

academic1 = Academic('Python Fundamentals', 12, 'PSF', 655, 'IT')

print(novel1)
print(academic1)

