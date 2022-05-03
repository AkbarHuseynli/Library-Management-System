from LibrarySystem.Member import Member
import random
import string
class E_Register(Member):
    def __init__(self,name,surname,email,phone_num):
         super().__init__(name,surname,email)
         self.phone_num = phone_num
    def e_register(self,name,surname,email,phone_num):
        if self.getName() and self.getSurname() and ( self.getEmail() or self.phone_num ):
            print("Online registering completed successfully")
            print("Get your password!")
            self.name = name
            self.surname = surname
            self.email = email
            self.phone_num = phone_num
        else:
            print("Registering failed")

    def getPassword(self):
        random_source = string.ascii_letters + string.digits + string.punctuation
        password = random.choice(string.ascii_lowercase)
        password += random.choice(string.ascii_uppercase)
        password += random.choice(string.digits)
        password += random.choice(string.punctuation)

        for i in range(6):
            password += random.choice(random_source)
        password_list = list(password)
        random.SystemRandom().shuffle(password_list)
        password = ''.join(password_list)
        print("Your password:",password)
        return password

class E_Login(E_Register):
     def __init__(self,name,surname,email,phone_num,password):
         super().__init__(name,surname,email,phone_num)
         self.password = password

     def e_login(self,e_email,e_password,Phone_num):
        if (e_email == self.getEmail() or Phone_num == self.phone_num) and e_password == self.password:
             print("Online logging completed successfully")
        else:
             print("Logging failed")

'''After user registered,it's necessary to subscript for using books and mp3'''
