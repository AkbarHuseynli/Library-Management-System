from LibrarySystem.BookInfo import Book
class Application:
    def __init__(self,e_books,audio_books,podcasts):
        self.e_books = e_books
        self.audio_books = audio_books
        self.podcasts = podcasts

    def search_by_category(self,category):
        books = []
        for Ebooks in self.e_books:
            if Ebooks.category == category:
                books.append(Ebooks)
                print("Title:",Ebooks.title)
        return books

    def search_by_author(self,author):
        books = []
        for Ebooks in self.e_books:
            if Ebooks.author == author:
                books.append(Ebooks)
                print("Title:",Ebooks.title)
        return books

    def search_by_lang(self,lang):
        books = []
        for Ebooks in self.e_books:
            if Ebooks.language == lang:
               books.append(Ebooks)
               print("Title:",Ebooks.title)
        return books

class Ebooks(Book):
    def __init__(self,title,author,category,language,pub_Year,BookID,instock,price):
        Book.__init__(self,title,author,category,language,pub_Year,BookID,instock,price)
        if self.getStockInformation() != True:
            raise TypeError("Instock must be true")

    '''There is no limit on using books in Ebook application, so instock must be true anyway'''

class AudioBooks:
    def __init__(self,title,language,speaker,AudioID):
        self.title = title
        self.language = language
        self.speaker = speaker
        self.AudioID = AudioID

class Podcasts:
    def __init__(self,subject,speakers):
        self.subject = subject
        self.speakers = speakers

'''Polymorphism was used to search books for category, author and language in Library system and Ebook application '''
def search_books_Fcategory(class_name):
    class_name.search_by_category()

def search_books_Fauthor(class_name):
    class_name.search_by_author()

def search_books_Flang(class_name):
    class_name.search_by_lang()





















