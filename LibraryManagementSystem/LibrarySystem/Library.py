class Library:
    def __init__(self,location,books,mentors,staff,name,service):
        self.location = location
        self.books = books
        self.mentors = mentors
        self.name = name
        self.staff = staff
        self.service = service

    def finding_available_mentor(self):
        av_mentors = []
        print("Available Mentors of Library in",self.location,":")
        for Mentor in self.mentors:
            if Mentor.get_av_lec():
                av_mentors.append(Mentor)
                print(Mentor.full_name)
        return av_mentors

    def finding_available_books(self):
        av_books = []
        for Book in self.books:
            if Book.getStockInformation():
                av_books.append(Book)
                print("Title of Available books:",Book.title)
        return av_books

    def search_by_category(self,category):
        books_by_category = []
        for Book in self.books:
            if Book.category == category:
                books_by_category.append(Book)
                print("Books:", Book.title)
        return books_by_category

    def search_by_author(self,author):
        books_by_author =[]
        for Book in self.books:
            if Book.author == author:
                books_by_author.append(Book)
                print("Books:",Book.title)
        return books_by_author

    def search_by_lang(self,lang):
        books_by_lang =[]
        for Book in self.books:
            if Book.language == lang:
                books_by_lang.append(Book)
                print("Books:",Book.title)
        return books_by_lang

class Location:
    def __init__(self,region_name,libraries):
        self.region_name = region_name
        self.libraries = libraries

    def search_libraries(self):
        libraries = []
        for Library in self.libraries:
                libraries.append(Library)
                print("Libraries:",Library.name)
        return libraries



















