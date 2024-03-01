# Encapsulation is the process of preventing clients from accessing certain properties
# which can only be accessed through special methods. Private attributes are 
# inaccessable attributes and information hiding is the process of making particular 
# attributes private. You use two underscores to declare private characteristics
# for instance __discount attribute for the Book class 

# class Book:
#     def __init__(self, title, quantity, author, price):
#         self.title = title
#         self.quantity = quantity
#         self.author = author
#         self.price = price 
#         self.__discount = 0.10 

#     def __repr__(self):
#         return f'Book {self.title}, Quantity: {self.quantity}, Author: {self.author}, Price: {self.price}'
    
# book1 = Book('Book 1', 12, 'Author 1', 120)

# print(book1.title)
# print(book1.quantity)
# print(book1.author)
# print(book1.price)
# print(book1.__discount)

# all the attributes are printed out except discount attribute which is private.
# You use getter and setter methods to access private attributes

class Book:
    def __init__(self, title, quantity, author, price):
        self.title = title
        self.quantity = quantity
        self.author = author 
        self.price = price 
        self.__discount = None 

    def set_discount(self, discount):
        self.__discount = discount

    def get_price(self):
        if self.__discount:
            return self.price * (1 - self.__discount)
        return self.price
    
    def __repr__(self):
        return f"Book: {self.title}, Quantity: {self.quantity}, Author: {self.author}, Price: {self.get_price()}"
    

single_book = Book('Two States', 1, 'Chetan Bhagat', 200)

bulk_books = Book('Two States', 25, 'Chetan Bhagat', 200)

bulk_books.set_discount(0.20)

print(single_book.get_price())
print(bulk_books.get_price())

print(single_book)
print(bulk_books)




