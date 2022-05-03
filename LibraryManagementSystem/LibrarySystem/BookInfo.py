class Book:
    def __init__(self,title,author,category,language,pub_Year,BookID,instock,price):
        self.title = title
        self.author = author
        self.category = category
        self.language = language
        self.pub_Year = pub_Year
        self.BookID = BookID
        self.__instock = instock
        self.__price = price
        if not isinstance(instock,bool):
            raise TypeError("Stock attributes must be in boolean type")
        if not isinstance(BookID,int):
            raise TypeError("Book id must be integer")
        if len(str(self.BookID)) != 4:
            raise TypeError("Book id consist of 4 digits")

    def getStockInformation(self):
            return self.__instock
    def setStock(self, STOCK):
            self.__instock = STOCK

    def getPrice(self):
        return self.__price
    def setPrice(self,p):
        self.__price = p

class Categories:
    def __init__(self,type,books):
        self.type = type
        self.books = books


    def getBooks(self):
        return self.books

    def show_av_books(self):
            books_by_category = []
            for Book in self.books:
                if Book.getStockInformation():
                    books_by_category.append(Book)
                    print("Books:", Book.title)
            return books_by_category

class Author:
    def __init__(self,full_name,books):
        self.__full_name = full_name
        self.books = books

    def getName(self):
        return self.__full_name
    def setName(self,Name):
        self.__full_name = Name

    def show_av_books(self):
        books_by_author =[]
        for Book in self.books:
            if Book.getStockInformation():
                books_by_author.append(Book)
                print("Books:",Book.title)
        return books_by_author

class Language:
    def __init__(self,lang,books):
        self.lang = lang
        self.books = books

    def show_av_books(self):
        books_by_lang = []
        for Book in self.books:
            if Book.getStockInformation:
                books_by_lang.append(Book)
                print("Books:", Book.title)
        return books_by_lang

# Polymorphism here
def show_available_books(object_name):
    object_name.show_av_books()







