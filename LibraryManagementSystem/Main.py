from LibrarySystem.Member import Member
from LibrarySystem.EnteringLibrary import Register,Login
from LibrarySystem.Library import Library,Location
from LibrarySystem.Service import*
from LibrarySystem.Mentor import Mentor
from LibrarySystem.BookInfo import Categories,Author,Language
from LibrarySystem.BookFromLib import Buy_Book,ExtraProducts,Borrow_Book,Return_Book,Discount
from LibrarySystem.Staff import Staff,Employee
from APP.AccessToApp import E_Register,E_Login
from APP.EbookApp import*
from APP.Shelf import MyBookshelf
from APP.Subscription import*

#Creating Member to library
Akbar1 = Member("Akbar","Huseynli","AkbarHuseynli@gmail.com")
Akbar = DebitCardInfo("Akbar","Huseynli","AkbarHuseynli@gmail.com",1111222233334444,5664,"03/22",1655)
Akbar.increaseBalance(150)
Akbar.card_info()
print("Member was created")
#Entering to library system
print("------------------------------------------------------")
Akbar = Register("Akbar","Huseynli","AkbarHuseynli@gmail.com","0553933859","M.F.AKHUNDOV STREET NO_07")
Akbar.register("Akbar","Huseynli","AkbarHuseynli@gmail.com","0553933859","M.F.AKHUNDOV STREET NO_07")
Akbar.gettingID()
Akbar = Login("Akbar","Huseynli","AkbarHuseynli@gmail.com",89)
Akbar.login("Akbar","Huseynli","AkbarHuseynli@gmail.com",89)
print("------------------------------------------------------")
#Creating Books
Book1 = Book("A Christmas Carol","Charles Dickens","fantasy","EN","2009",1003,True,15)
Book2 = Book("Chess","Stefan Zweig","classic","EN","1943",2345,True,20)
Book3 = Book("The Old Man and the Sea","Ernest Hemingway","novella","EN","1952",1755,False,13.5)
Book4 = Book("The Eye of the World","Robert Jordan","fantasy","EN","1990",1357,True,37)
#creating mentors
Orkhan = Mentor("Orkhan Mammadov",5,True,"0552022222")
Anar =Mentor("Anar Rzayev",3,True,"0552873747")
Calil =Mentor("Calil Calilov",10,False,"0502873747")
Gunel =Mentor("Gunay Aliyev",1,False,"0512873747")
Aysel =Mentor("Aysel Amanov",3,True,"0702873747")
Ziya = Mentor("Ziya Garayev",4,True,"0505626262")
#Creating employees
librarian1 = Employee("librarian",15,500)
librarian2 = Employee("librarian",4,500)
cashier = Employee("cashier",-2,500)
cleaner = Employee("cleaner",0,300)
#Creating Staff
print("---------------------About Staff--------------------------")
A = Staff([librarian1,librarian2,cashier,cleaner],1550,35000)
A.Sales_to_Salary()
cashier.Bonus()
cashier.Dismissal()
print("------------------------About Service--------------------------")
#Creating Service
Dessert1 = Products()
#Creating Courier
Courier1 = Courier("Hamza Jafarov","055",True)
Courier2 = Courier("Ali Rahmanov","051",False)
Courier3 = Courier("Arif Yasharov","070",True)
#Creating delivery

Del = Delivery("Akbar","Huseynli","AkbarHuseynli@gmail.com",1111222233334444,5664,"03/22",1655,[Courier1,Courier2,Courier3],Book1,15,[Dessert1],1.5)
Del.PayForDistance()
Del.TotalBill()
Del.Payment()
Del.PayBill()
Akbar1.search_couriers(Del)
#Creating library
Khazar = Library("Neftchilar",[Book1,Book2,Book3],[Orkhan,Anar],A,"Khazar",Del)
Khazar2 = Library("Neftchilar",[Book1,Book2,Book4],[Gunel,Ziya],A,"Khazar2",Del)
Khazar3 = Library("Narimanov",[Book1,Book2,Book4],[Gunel,Ziya],A,"Khazar3",Del)
Khazar4 = Library("Narimanov",[Book1,Book2,Book4],[Gunel,Ziya],A,"Khazar4",Del)
#Locations
Neftchilar = Location("Neftchilar",[Khazar,Khazar2])
Narimanov = Location("Narimanov",[Khazar3,Khazar4])

#Methods
print("---------------------Library Methods----------------------------")
Khazar.finding_available_mentor()
Khazar.finding_available_books()
print("-----------------------Location Methods------------------------------")
Neftchilar.search_libraries()
Narimanov.search_libraries()
print("---------------------Searching for books----------------------------")
Khazar.search_by_author("Charles Dickens")
Khazar.search_by_category("fantasy")
Khazar.search_by_lang("EN")
#Categories, authors, languages
Fantasy = Categories("fantasy",[Book1,Book4])
Cha = Author("Charles Dickens",[Book1])
EN = Language("EN",[Book1,Book2,Book3,Book4])
print("--------------------Showing available books by authors, categories and lang-------------------------------")
def show_available_books(object_name):
    object_name.show_av_books()
#Polymorphism used here
show_available_books(EN)
show_available_books(Cha)
show_available_books(Fantasy)
print("------------------------------------------------------")
#Member methods
print("-----------------------About Mentors---------------------------")
Akbar.search_mentors(Khazar)
Akbar.contact_mentors(Orkhan)
print("-------------------------------------------------------")
#GETTING BOOKS FROM LIBRARY
print("------------------------Buying Book--------------------------")
Book1 = Buy_Book("A Christmas Carol","Charles Dickens","fantasy","EN","2009",1003,True,35)
Book1.PossibleBuying()
print("-----------------------Extra Products-------------------------------")
Book1 = ExtraProducts("A Christmas Carol","Charles Dickens","fantasy","EN","2009",1003,True,35)
Book1.set("journal",10)
Book1.BuyingExtraProducts()
print("---------------------------Borrowing Book---------------------------")
Book2 = Borrow_Book("Chess","Stefan Zweig","classic","EN","1943",2345,True,20,"Akbar","Huseynli","AkbarHuseynli@gmail.com","0553933859","M.F.AKHUNDOV STREET NO_07",7)
Book2.PossibleBorrowing()
print("-----------------------Returning Book-------------------------------")
Book2 = Return_Book("Chess","Stefan Zweig","classic","EN","1943",2345,True,20,"Akbar","Huseynli","AkbarHuseynli@gmail.com","0553933859","M.F.AKHUNDOV STREET NO_07",7,3)
Book2.Return_or_Pay_for_delay()
print("-------------------------Discount For books----------------------------")
Book1 = Discount("A Christmas Carol","Charles Dickens","fantasy","EN","2009",1003,True,15,15)
Book1.PriceInDiscount()
print("------------------------------------------------------")
'''E-BOOK APPLICATION'''
#ENTRY TO APP
print("------------------------Entering to mobile application------------------------------")
Akbar = E_Register("Akbar","Huseynli","AkbarHuseynli@gmail.com","0553933859")
Akbar.e_register("Akbar","Huseynli","AkbarHuseynli@gmail.com","0553933859")
Akbar.getPassword()
Akbar = E_Login("Akbar","Huseynli","AkbarHuseynli@gmail.com","0553933859","pJ?Ko%4Wh6")
Akbar.e_login("AkbarHuseynli@gmail.com","0553933859","pJ?Ko%4Wh6")
#Creating Ebooks
EBook1 = Ebooks("A Christmas Carol","Charles Dickens","fantasy","EN","2009",1003,True,15)
EBook2 = Book("Chess","Stefan Zweig","classic","EN","1943",2345,True,20)
EBook3 = Book("The Old Man and the Sea","Ernest Hemingway","novella","EN","1952",1755,True,13.5)
EBook4 = Book("The Eye of the World","Robert Jordan","fantasy","EN","1990",1357,True,37)
#Creating Audio books
Audio1 = AudioBooks("Audio1","EN","Speaker1",123)
Audio2 = AudioBooks("Audio2","EN","Speaker2",223)
Audio3 = AudioBooks("Audio3","EN","Speaker3",323)
Audio4 = AudioBooks("Audio4","EN","Speaker4",523)
#creating Podcasts
Podcast1 = Podcasts("Subject1","Speaker1 and Speaker2")
Podcast2 = Podcasts("Subject2","Speaker3 and Speaker4")
Podcast3 = Podcasts("Subject3","Speaker1 and Speaker2 and Speaker3")
#Creating Ebook App
APP = Application([EBook1, EBook2, EBook3, EBook4], [Audio1, Audio2, Audio3, Audio4], [Podcast1, Podcast2, Podcast3])
print("----------------------Searching Ebooks--------------------------------")
APP.search_by_lang("EN")
APP.search_by_author("Ernest Hemingway")
APP.search_by_category("classic")
#creating Shelf
print("-----------------------Shelf-------------------------------")
Myshelf = MyBookshelf([EBook3,EBook4],True)
Myshelf.addToMyShelf()
#GettingSubscription
print("-------------------------Discount for subscription price-----------------------------")
Pr = SubscriptionPrice(50,200,500)
Pr.Discount(5)
print("---------------------Adding card---------------------------------")
Akbar = GetSubscription("Akbar","Huseynli","AkbarHuseynli@gmail.com",1111222233334444,5664,"03/22",1655,50,200,500)
Akbar.addingCard("Akbar","Huseynli",1111222233334444,5664,"03/22")
print("-----------------------Checking and paying for subscription-------------------------------")
Akbar.CheckingForSubsription()
Akbar.PriceToBalance()
Akbar.PayForSubscription()
print("----------------------Gift Cards--------------------------------")
Akbar = GiftCard("Akbar","Huseynli","AkbarHuseynli@gmail.com",1111222233334444,5664,"03/22",1655,50,200,500)
Akbar.FreeGiftCards()





































