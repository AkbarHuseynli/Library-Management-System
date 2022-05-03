import random
from LibrarySystem.Member import Member
class Register(Member):
    def __init__(self,name,surname,email,phone_num,address):
        Member.__init__(self,name,surname,email)
        self.phone_num = phone_num
        self.address = address

    def register(self,name,surname,email,phone_num,address):
        if name and surname and email and phone_num and address:
            print("Registered successfully")
            print("Get your ID!")
            self.name = name
            self.surname = surname
            self.email = email
            self.phone_num = phone_num
            self.address = address
        else:
            print("Incorrect registering information")

    def gettingID(self):
        lib_id = random.choice(range(0, 1000))
        print("Your library ID is:",lib_id)

class Login(Member):
    def __init__(self,name,surname,email,lib_id):
        Member.__init__(self,name,surname,email)
        self.lib_id = lib_id

    def login(self,entered_name,entered_surname,entered_email,entered_ID):
        if entered_name == self.getName() and entered_surname == self.getSurname() and entered_email == self.getEmail() and entered_ID == self.lib_id:
            print("Logged succesfully")
        else:
            print("Incorrect logging information")




