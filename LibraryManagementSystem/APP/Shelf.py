class MyBookshelf():
    def __init__(self,e_books,fav):
        self.fav = fav
        self.e_books = e_books
        if not isinstance(fav,bool):
            raise TypeError("You have to enter that is your favourite one or not")

    def addToMyShelf(self):
        Myshelf = []
        for Ebooks in self.e_books:
            if self.fav:
                Myshelf.append(Ebooks)
                print(Ebooks.title,"was added to your shelf")
        return Myshelf

