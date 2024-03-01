# The term polymorphism comes from Greek language and means
# "something that takes on multiple forms"

# Polymorphism refers to subclass's ability to adapt a method that already
# exists in its superclass to meet its needs. To put it another way, a subclass
# can use a method from its superclass as it is or modify it as needed.


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

    def __repr__(self):
        return f"Book: {self.title}, Branch: {self.branch}, Quantity: {self.quantity}, Author: {self.author}, Price: {self.get_price()}"
    
# The Book superclass has a specific method called __repr__. 
# This method can be used by subclass Novel so that it is called whenever an object is printed.

# The Academic subclass, on the other hand, is defined with its own __repr__ special function in the example code above. 
# The Academic subclass will invoke its own method by suppressing the same method present in its superclass, thanks to polymorphism.  


novel1 = Novel('Two States', 20, 'Chetan Bhagat', 200, 187)
novel1.set_discount(0.20)

academic1 = Academic('Python Foundations', 12, 'PSF', 655, 'IT')

print(novel1)
print(academic1)  