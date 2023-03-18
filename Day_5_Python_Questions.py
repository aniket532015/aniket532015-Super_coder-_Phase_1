#
#given a number n,WAP to find the sum of the largest prime factor of each nine consecutive numbers starting from n
#g(n)=f(n)+f(n+1)+f(n+2)+f(n+3)+f(n+4)+f(n+5)+f(n+6)+f(n+7)+f(n+8)
#where ,g(n) is sum and f(n) os the largest prime factor of n
# exp= g(10)=f(11)+f(12)+f(13)+f(14)+f(15)+f(16)+f(17)+f(18)
#5+11+3+13+7+5+2+17+3=66
             

### A University wants to automate their admission process. Students are admitted based on marks according to a qualifying exams.
#
#A Student is identified by studentid, age and marks in qualifying exam
#
#Data is valid, if:
#  * Age is greater than 20
#  * Marks is between 0 and 100
#
#A Student qualifies for the admission if:
#  * Age and Marks are Valid
#  * Marks is greater than 65
#
#Rules to Follow:
#Class Name: Student
#-- Attributes: (private)
#   * student_id
#   * marks
#   * age
#
#Methods:
#(public)
#* _init_()
#* validate_marks()
#* validate_age()
#* check_qualification()
'''
class data:
        def __init__(self):
                self.__ID=None
                self.__age=None
                self.__marks=None
                self.__cal=None
                self.__course=None
        def setID(self,ID):
                self.__ID=ID
        def setage(self,age):
                self.__age=age
        def setmarks(self,marks):
                self.__marks=marks
        def calculate(self):
                if self.getage()>20 and self.getmarks() > 0 and self.getmarks() < 100:
                        if(self.getmarks()>65):
                                print("Eligible for Admission") 
                                print(self.fee())
                        else:
                                print("Not Eligible")
                else:
                        print("Not eligible")
        def fee(self):
                d={1001:25575,1002:15500}
                if self.getmarks()>85:
                        return "after 25% discount  :"+ str(d[self.getID()]*0.75)
                else:
                        return "Not Eligible For Discount  : "+ str(d[self.getID()])
        def getID(self):
                return self.__ID
        def getage(self):
                return self.__age
        def getmarks(self):
                return self.__marks
obj=data()
obj.setID(1001)
obj.setage(21)
obj.setmarks(77)
obj.calculate()
#'''
#### Pizza for You is a pizza store which sells different kinds of pizzas based on customer's order. Customer can either collect the order in person or opt for a door delivery. Write a python program based on the class diagram given below
#
#### Rules to follow
#Customer Class:
#   * validate_quantity() -  Customer can order 1 to 5 pizzas. If valid return true, else return false
#PizzaService Class:
#   * Initialise static variable counter to 100
#   Attribute
#   * additional_topping is a boolean value which indicates whether additional topping is required or not, True if required. False, if not required
#   * validate_pizza_type() - Customers can order small or medium type pizzas. If valid return True else return False
#   * calculate_pizza_cost() - Calculate Pizza Cost, validate type and quantity
#                 - If valid, Identify the pizza cost based on the details mentioned belw in the table
#                 - Set attribute pizza cost with calculated pizza cost
#                 - Autogenerate service_id based starting from 101 by first letter of pizza type
#                             - Example - S101, s102, m103, S104, M105 etc.
#                 - If Invalid set pizza cost to -1
#- Pizza Type | Cost | Additional Topping Cost
#- Small      | 150  |  35
#- Medium     |  200 |  50
#
#DoorDelivery Class:
#* validate_distance_in_kms() - Minimum distance for door delivery is 1km and maximum is 10km
#                             - If valid, return true, else return false
#* caclulate_pizza_cost() - Calculate pizza cost
#Validate Distance in kms
#if valid,
#Calculate pizza cost (Hint: Invoke Overriden Method in Parent Class)
#If pizza_cost is not -1 identify the delivery charge based on the details
#
#Distance in kms Delivery charge in km 
#For first 5km      5
#For remaining 5km  7
#Else set pizza_cost to  -1
#
#Perform case insensitive string comparision
#For testing:
#Create objects of PizzaService and Doordelivery Class
#Invoke calculate_pizza_cost() on Pizzaservice and DoorDelivery
#Display the details
#
class coustmer():
        def __init__(self):
                self.quantity=None
        def setquantity(self,quantity):
                self.quantity=quantity
        def getquantity(self):
                return self.quantity
        
        def calquan(self):
                if setquantity() !=0:
                        if setquantity()<=5:
                                return True
                        else:
                                return False
                else:
                        return False
class pizzaservice(coustmer):
        count=100
        def __init__(self,valcount):
                self.valcount=valcount
                self.pizzatype=None
                self.pizzacost=None
                self.serviceID=None
        def setserviceID(self,serviceID):
                self.serviceID=serviceID
        def getserviceID(self):
                return self.serviceID
        def setpizzatype(self,pizzatype):
                self.pizzatype=pizzatype
        def getpizzatype():
                return self.pizzatype
        def setpizzacost(self,pizzacost):
                self.pizzacost=pizzacost
        def getpizzacost(self):
                return self.pizzacost
        def validate_pizza_type(self):
                if getpizzatype()=="small":
                        self.serviceID='S'+str(count+1)
                        return True
                        
                elif getpizzatype()=="medium":
                        self.serviceID='m'+str(count+1)
                        return True
                        
                else:
                        return False
        def calculatepizzacost(self):
                if validate_pizza_type()==True:
                        return getpizzacost()*150
                elif validate_pizza_type()==True:
                        return getpizzacost()*200
                else:
                        return getpizzacost()="-1"
        
        
                                
 c=coustmer()
 print(c.calquan(5))
