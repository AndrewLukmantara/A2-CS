class Book():
    
    # Initiliazing of attributes
    
    def __init__(self, pTitle, pAuthor, pisBorrowed):
        self.__title = pTitle # type string
        self.__author = pAuthor # type string
        self.__isBorrowed = pisBorrowed # type boolean
    
    # Getters
    
    def get_title(self):
        return self.__title

    def get_author(self):
        return self.__author
    
    def get_isBorrowed(self):
        return self.__isBorrowed
    
    # Setters
    
    def set_title(self, newTitle):
        self.__title = newTitle
    
    def set_author(self, newAuthor):
        self.__author = newAuthor
        
    def set_isBorrowedd(self, newisBorrowed):
        self.__isBorrowed = newisBorrowed
    
    # Borrowing the book
    
    def borrowBook(self):
        self.__isBorrowed = True
    
    # Returning the book
    
    def returnBook(self):
        self.__isBorrowed = False
    
    # Getting the status of the book
    
    def getStatus(self):
        print(f"Book Name : {self.__title}\nAuthor : {self.__author}\nisBorrowed : {self.__isBorrowed}")
    

bookArr = [] # Making an empty array

# Making 4 Book objects

book1 = Book("Physics", "Mr Edwin", False)
book2 = Book("Computer Science", "Mr Khan", False)
book3 = Book("Chemistry", "Mr Gopi", False)
book4 = Book("Math", "Mr Gopal", False)

# Initiliazing the array with books

bookArr.append(book1)
bookArr.append(book2)
bookArr.append(book3)
bookArr.append(book4)

# Simulation of borrowing, returning and getting the status of each book in the array

for book in bookArr:
    book.getStatus()
    book.borrowBook()
    book.getStatus()
    book.returnBook()
    book.getStatus()

