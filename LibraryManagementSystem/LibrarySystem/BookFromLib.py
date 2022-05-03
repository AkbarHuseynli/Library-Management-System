from LibrarySystem.BookInfo import Book
from LibrarySystem.EnteringLibrary import Register
'''You can buy any book with its id, if it is in stock'''
class Buy_Book(Book):
    def __init__(self,title,author,category,language,pub_Year,BookID,instock,price):
        Book.__init__(self,title,author,category,language,pub_Year,BookID,instock,price)

    def PossibleBuying(self):
        if self.getStockInformation():
            print("You can buy the book")
        else:
            print("Impossible buying operation, Book is not in stock")

class ExtraProducts(Buy_Book):
    def set(self,product,price1):
        #catalogs,gazette,journals,atlasses and etc
        self.__product = product
        self.__price1 = price1

    def getPrice(self):
        return self.__price1
    def setPrice(self,x):
        self.__price1 = x

    def BuyingExtraProducts(self):
        if self.getPrice() > 50 and self.getStockInformation() == True:
            self.setPrice(0)
            print("You can get extra product for free")
            return self.getPrice()
        elif self.getPrice() > 30 and self.getStockInformation() == True:
            self.setPrice(self.getPrice()*0.5)
            print("50% DISCOUNT TO EXTRA PRODUCT")
            return self.getPrice()
        else:
            print("No possible discount! Take it paying",self.getPrice(),"AZN")

class Discount(Buy_Book):
    def __init__(self,title,author,category,language,pub_Year,BookID,instock,price,discount_percent):
        Buy_Book.__init__(self,title,author,category,language,pub_Year,BookID,instock,price)
        self.__discount_percent = discount_percent

    def getDiscount(self):
        return self.__discount_percent
    def setDiscount(self,dis):
        self.__discount_percent = dis

    def PriceInDiscount(self):
        total = self.getPrice()*((100-self.getDiscount())/100)
        self.setPrice(total)
        print("Price with discount is",self.getPrice())
        return self.getPrice()

'''You can borrow book with your information, if you have been registered'''
class Borrow_Book:
    def __init__(self,title,author,category,language,pub_Year,BookID,instock,price,name,surname,email,phone_num,address,ReTime):
        self.comp1 = Book(title,author,category,language,pub_Year,BookID,instock,price)
        self.comp2 = Register(name,surname,email,phone_num,address)
        self.ReTime = ReTime
        if not isinstance(ReTime,int):
            raise TypeError("Enter returning time of book with days")

    def PossibleBorrowing(self):
        if self.comp1.getStockInformation():
            print("You can borrow the book")
        else:
            print("Impossible borrowing operation, Book is not in stock")

class Return_Book(Borrow_Book):
    def __init__(self,title,author,category,language,pub_Year,BookID,instock,price,name,surname,email,phone_num,address,ReTime,UsedTime):
        Borrow_Book.__init__(self,title,author,category,language,pub_Year,BookID,instock,price,name,surname,email,phone_num,address,ReTime)
        self.UsedTime = UsedTime
        if not isinstance(UsedTime,int):
            raise TypeError("Enter using time of book with days")

    def Return_or_Pay_for_delay(self):
        if self.ReTime >= self.UsedTime:
            print("Successful returning")
            skip = ('skip','s')
            try:
                x = int(input("Rate the book with 1-5 /If you want to skip, write down zero 0:"))
                if x == 0:
                    pass
                elif not x in range(1,5):
                    raise TypeError("Rate the book correctly")
                y = str(input("Leave comment about book /If you want to skip, write down skip:"))
                if y in skip:
                    pass
            except ValueError:
                print("Enter correct input to Rating book and leaving comment")
        else:
            print("You have to pay",(self.UsedTime - self.ReTime)*0.5,"AZN for delay")















