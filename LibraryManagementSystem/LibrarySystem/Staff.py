class Staff:
    def __init__(self, employees, average_monthly_sales, average_monthly_income):
        # monthly income is salary of general staff
        self.employees = employees
        self.sales = average_monthly_sales
        self.__monthly_income = average_monthly_income

    def getIncome(self):
        return self.__monthly_income
    def setIncome(self,inc):
        self.__monthly_income = inc

    def Sales_to_Salary(self):
        monthly_sales = int(input("Enter the sales of current month: "))
        if monthly_sales >= self.sales:
            earned_income = float(input("Enter the earned income with AZN: "))
            self.setIncome((earned_income/2)+self.getIncome())
        else:
            lost_income = float(input("Enter the lost income with AZN"))
            self.setIncome(self.getIncome()-(lost_income/2))
        return self.getIncome()


class Employee:
    def __init__(self,job,service,salary):
        self.job = job
        # librarians,cashiers,cleaners'
        self.service = service
        self.__salary = salary

    def getSalary(self):
        return self.__salary
    def setSalary(self,x):
        self.__salary = x

    def Bonus(self):
        if 5 >= self.service > 0:
            print("Thank you for your responsibility")
            print("You rechieve 5 percent salary bonus")
            self.setSalary(self.getSalary()*1.05)
        elif 10 >= self.service > 5:
            print("Thank you for your responsibility")
            print("You rechieve 10 percent salary bonus")
            self.setSalary(self.getSalary() * 1.1)
        elif self.service > 10:
            print("Thank you for your responsibility")
            print("You rechieve 15 percent salary bonus")
            self.setSalary(self.getSalary() * 1.15)
        else:
            print("No possible bonus")

    def Dismissal(self):
        if -5 < self.service < 0:
            print("WARNING!")
            print("Be attendable in your job")
            print("Your salary was decreased 10 percent")
            self.setSalary(self.getSalary()*0.90)
        elif -10 < self.service < -5:
            print("Increase your attendance! Otherwise, You will be dismissed")
            print("Your salary was decreased 20 percent")
            self.setSalary(self.getSalary()*0.8)
        elif self.service < -10:
            print("Sorry!,You was dismissed by directory")








