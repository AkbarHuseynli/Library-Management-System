import random
class Member:
    def __init__(self,name,surname,email):
        self.__name = name
        self.__surname = surname
        self.__email = email

    def getName(self):
        return self.__name
    def setName(self,Name):
        self.__name = Name

    def getSurname(self):
        return self.__surname
    def setSurname(self,Surname):
        self.__surname = Surname

    def getEmail(self):
        return self.__email
    def setEmail(self,Email):
        self.__email = Email

    def search_mentors(self,Library):
        print(self.getName(),self.getSurname(), " is searching available masters")
        Mentor = Library.mentors
        choice = random.choice(Mentor)
        print(self.getName(),self.getSurname(),"chose",choice.full_name)
        return choice

    def contact_mentors(self,Mentor):
        contact_num = Mentor.get_mentor_number()
        print("Mentor's contact name:",Mentor.full_name)
        print("Mentor's contact number:",contact_num)

    def search_couriers(self,Delivery):
        print(self.getName(),self.getSurname(), " is searching available courier")
        Courier = Delivery.courier
        choice = random.choice(Courier)
        print(self.getName(),self.getSurname(),"chose",choice.name)
        return choice


class DebitCardInfo(Member):
    def __init__(self, name, surname, email, card_number, card_pin, card_expdate, balance):
        Member.__init__(self, name, surname, email)
        self.__card_number = card_number
        self.__card_pin = card_pin
        self.__card_expdate = card_expdate
        self.__balance = balance
        if not isinstance(card_number,int) and isinstance(card_pin,int):
            raise TypeError("Enter Attributes in correct type")
        if not isinstance(card_expdate,str):
            raise TypeError("Enter Attributes in correct type")
        cn = str(card_number)
        cp = str(card_pin)
        if len(cn) != 16:
            raise TypeError("Card number has to be 16 digit")
        if len(cp) != 4:
            raise TypeError("Card password has to be 3 or 4 digit")

    def getCard_number(self):
        return self.__card_number

    def setCard_number(self, Cnum):
         self.__card_number = Cnum

    def getCard_pin(self):
        return self.__card_pin

    def setCard_pin(self, Cpin):
         self.__card_pin = Cpin

    def getCard_expdate(self):
        return self.__card_expdate

    def setCard_expdate(self, Cexp):
        self.__card_expdate = Cexp

    def getBalance(self):
        return self.__balance

    def setBalance(self, newBalance):
         self.__balance = newBalance

    def increaseBalance(self, Amount):
        print("If you want increase:")
        IncBalance = self.getBalance() + Amount
        self.setBalance(IncBalance)
        print("Your balance was increased")
        return self.getBalance()

    def card_info(self):
        print("User's card information:")
        print("Full name:", self.getName(), self.getSurname())
        print("Card number:", self.getCard_number())
        print("Card password:", self.getCard_pin())
        print("Card expiration date:", self.getCard_expdate())
        print("Card Balance:", self.getBalance())














