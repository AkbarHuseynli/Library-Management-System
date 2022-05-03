from LibrarySystem.Member import DebitCardInfo

class SubscriptionPrice:
    def __init__(self, weeklyPr, monthlyPr, annualPr):
        self.weeklyPr = weeklyPr
        self.monthlyPr = monthlyPr
        self.annualPr = annualPr

    def Discount(self,discount_percent):
        w = self.weeklyPr*((100-discount_percent)/100)
        self.weeklyPr = w
        m = self.monthlyPr * ((100 - discount_percent) / 100)
        self.monthlyPr = m
        y = self.annualPr * ((100 - discount_percent) / 100)
        self.annualPr = y

class GetSubscription(DebitCardInfo, SubscriptionPrice):
    def __init__(self, name, surname, email, card_number, card_pin, card_expdate, balance,weeklyPr, monthlyPr, annualPr):
        DebitCardInfo.__init__(self, name, surname, email, card_number, card_pin, card_expdate, balance)
        SubscriptionPrice.__init__(self,weeklyPr, monthlyPr, annualPr)

    def addingCard(self, name, surname, card_number, card_pin, card_expdate):
        if self.getName() == name and self.getSurname() == surname and self.getCard_number() == card_number and self.getCard_pin() == card_pin and self.getCard_expdate() == card_expdate:
            print("Card was added")
        else:
            print("Incorrect card information ")

    def CheckingForSubsription(self):
        print("Your balance:", self.getBalance())
        if  self.weeklyPr <= self.getBalance() < self.monthlyPr:
            print("You can get weekly subscription")

        elif self.monthlyPr <= self.getBalance() < self.annualPr:
            print("You can get monthly subscription")

        elif self.getBalance() >= self.annualPr:
            print("You can get annual subscription")

        else:
            print("Current balance isn't enough to get Subscription!")

    def PriceToBalance(self):
        if  self.weeklyPr <= self.getBalance() < self.monthlyPr:
            return self.weeklyPr
        elif self.monthlyPr <= self.getBalance() < self.annualPr:
            return self.monthlyPr
        elif self.getBalance() >= self.annualPr:
            return self.annualPr
        else:
            return "Nothing"

    def PayForSubscription(self):
        Amount = self.getBalance() - self.PriceToBalance()
        print("Your subscription operation completed successfully")
        self.setBalance(Amount)
        return print("Current balance:", self.getBalance())

class GiftCard(GetSubscription):
    def FreeGiftCards(self):
      if self.PriceToBalance() == self.weeklyPr:
          print("You can buy weekly gift card for free")
      elif self.PriceToBalance() == self.monthlyPr:
          print("You can buy monthly gift card for free")
      elif self.PriceToBalance() == self.annualPr:
          print("You can buy yearly gift card for free")
      else:
          print("You don't have any subscription")




