from LibrarySystem.Member import DebitCardInfo

class Products:
    #Dishes,dessert and drinks
    def __init__(self):
        x = str(input("Enter if you want skip product details or not"))
        if x == "not":
            self.product_name = str(input("Enter Product name:"))
            self.product_price = float(input("Enter Product price:"))
        elif x == "skip":
            pass
        else:
            raise TypeError("Enter skip or not")

class Courier:
    def __init__(self, name,contact_number, available):
        self.name = name
        self.contact_number = contact_number
        self.available = available

class Delivery(DebitCardInfo):
    def __init__(self,name, surname, email, card_number, card_pin, card_expdate, balance,courier,book,price_of_books,products,price_of_products):
        DebitCardInfo.__init__(self, name, surname, email, card_number, card_pin, card_expdate, balance)
        self.courier = courier
        self.book = book
        self.price_of_books = price_of_books
        self.products = products
        self.price_of_products = price_of_products
        self.distance = float(input("Enter distance from library with meter"))
        self.payment_type = str(input("Enter payment type (Cash/Debit Card)"))

    def PayForDistance(self):
        if self.distance < 1000:
            self.pay_for_distance = 1.5
            return self.pay_for_distance
        elif 3000 > self.distance >= 1000:
            self.pay_for_distance = 2
            return self.pay_for_distance
        elif self.distance >= 3000:
            self.pay_for_distance = 3
            return self.pay_for_distance

    def TotalBill(self):
        print("Price of books:",self.price_of_books)
        print("Price of products:", self.price_of_products)
        print("Price of delivery :", self.pay_for_distance)
        self.total_bill = (self.price_of_books+self.price_of_products+self.pay_for_distance)
        print("total:",self.total_bill)
        possible_discount = str(input("Enter if discount available or not in Library/Yes or No"))
        if possible_discount == "Yes":
            self.total_bill = self.total_bill*(100-int(input("Enter discount percent:")))/100
            print("You have to pay",self.total_bill,"AZN")
            return self.total_bill
        elif possible_discount == "No":
            print("Unavailable disscount")
            print("You have to pay",self.total_bill,"AZN")
            return self.total_bill

    def Payment(self):
        if self.payment_type == "Cash":
            print("Pay at the door")
        elif self.payment_type == "Debit Card":
            print("Add your debit card")
            if self.getName() == str(input("Enter your name on debit card:")) and self.getSurname() == str(input("Enter your surname on debit card:")) and self.getCard_number() == int(input("Enter debit card number")) and self.getCard_pin() == int(input("Enter debit card password:")) and self.getCard_expdate()==str(input("Enter card expiration date MM/YY:")):
                print("Card was added")
            else:
                raise TypeError("Incorrect card information")
        else:
            print("Choose Cash or Debit Card")

    def PayBill(self):
        if self.getBalance() >= self.total_bill:
            self.setBalance(self.getBalance()-self.total_bill)
            print("Current Balance:",self.getBalance())
            return self.getBalance()
        else:
            print("Balance is not enough to pay bills")




