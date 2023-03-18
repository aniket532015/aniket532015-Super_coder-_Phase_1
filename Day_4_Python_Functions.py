###
#wap nearset palindrome()which accepts a number and return the nearest palindrome greater than the given string
#sample Input
#99              101
#1221             1331
'''
n=int(input())
flag=0
def palindrome(n):
        while flag==0:
                n=n+1
                a=str(n)
                if(str(n)[::-1]==str(a)):
                        return n
print(palindrome(n))
'''
#care hospital wants to know the medical specillaty visited by the maximum m=number of patients .assume that the patient id of paitent along with
#the details of the medical specilities are stored in a dictionary as follows{"P":"prediatrics","O":Orthopedics","E":ENT}
#write a function to find the specillity visited by the maximum no of patient which is visited by maximum no of patients
#perform case sensetive string where necessary
#input --- [101,P,102,o,304,p,305,p]
#output--Pediatrics
'''
n=input()
def hos(n):
        for i in n.split():
                count=count1=count2=0
                if(i=='P'):
                        count+=1
                elif(i=='O'):
                        count1+=1
                else:
                        count2+=1
        if(count>count1 and count>count2):
                print("ENt")
        elif(count1>count and count1>count2):
                print("Orthopedics")
        else:
                print("Prediatrics")
                
hos(n)
'''
#wap to take input in 2 string and return the common character case sesitive return -1 if no string matches
#sample "i=I Like Python"
#"Java is a very popular language"
#lieyon
'''
n=("I like Python")
a=("Java is a very popular language")
def con(n,a):
        n=list(n)
        a=list(a)
        for i in n:
                if(i!=" "):
                        for word in a:
                                if(word==i):
                                        print(word,end=" ")
        if(word<str(0)):
                print("-1")                        
                                
con(n,a)
'''
'''
n=("I like Python")
a=("Java is a very popular language")
print(''.join([i for i in n if i in a and i!=" "]))

'''
'''
class Employee:
        def __init__(self):
                self.employee_id=none
        def check_elegib(self):
                if(self.employee_id>=9000 and self.employee_id<=10000):
                        print("eligible for special beifites")'=
                else:
emp1=Employee()                     print("not eligible")
emp1.employee_id=10000
em1.employee_elegib()
emp2=Employee()
emp2.employee_id=10000
emp2.employee_elegib()
'''
'''
class Example:
        def __init__(self,num):
                self.num=num

        def set_num(self,num):
                self.num=num

        def get_num(self):
                return self.num
obj=Example(10)
print(obj.get_num())
obj.set_num(15)
print(obj.get_num())
'''
'''
class coust:
        def __init__(self):
               self.coustm_id=100
c1=coust()
print(c1.coustm_id)
'''
'''
class cous:
        def __init__(self,id):
                self.id=id#100
c1=cous(200)
print(c1.id)
'''
#
'''
class book:
        def __init__(self):
                self.title=None
my_fav=book()
my_fav.title="head prog"
your_fav=book()
your_fav.title="Learn python"
print("My fav is",my_fav.title)
print("yours is",your_fav.title)
'''
#
'''
class shoe:
        def __init__(self,price,material):
                self.price=price
                self.material=material
        def __str__(self):
                return "shoe with price:"+str(self.price)+"and material:"+self.material
s1=shoe(1000,"canvas")
print(s1)# it will show error
print(s1.price,s1.material)
print(id(s1))
'''
#
'''
class mobile:
        def __init__(self):
                print(id(self))
        def display(self):
                
                print("display details")
        def purchase(self):
                self.display()
                print("calculating price")

#mobile().purchase()
#mobile().purchase()
m1=mobile()
print(m1)
m2=mobile()
print(m2)
m1=m2
print(m1)
'''
#
'''
class mobile:
        def __init__(self,brand,price):
                self.brand=brand
                self.price=price
                self.total_price=None
        def purchase(self):
                if self.brand=="Apple":
                        discount=10
                else:
                        discount=5
                self.total_price=self.price-self.price*(discount/10)
                print("tatal price",self.brand,"mobile is",self.total_price)
        def amount_return(self):
                return self.price-self.total_price
mob1=mobile("Apple",20000)
mob1.purchase()
m2=mobile("samsung",10000)
m2.purchase()
print(mob1.amount_return())
print(m2.amount_return())
'''
#ANALYSIS THE CODE
'''
class coust:
        def __init__(self,cust_id,name,age,wallet_bal):
                self.cust_id=cust_id
                self.name=name
                self.age=age
                self.__wallet_bal=wallet_bal
        def set_balance(self,amount):
                if amount<50000 and amount>0:
                        self.__wallet_bal+=amount
        def show_balance(self):
                print("the balance is",self.__wallet_bal)
        def get_wallet_balance(self):
                return self.__wallet_bal
c1=coust(100,"aniket",22,1000)
#c1.update(500)
print(c1.get_wallet_balance())
#print(c1.__show_balance())
c1.set_balance(5000)
print(c1.get_wallet_balance())
'''
'''
class dam:
        def __init__(self,name,length):
                self.name=name
                self.__length=length
        def get_length(self):
                return self.__length
dam1=dam("ABC dam",3.5)
print("dam name:",dam1.name)
print("dam length:",dam1.get_length())
'''
'''
class table:
        def _init_(self):
                self.no_of_legs=4
                self.__glass_top = None
                self.__wooden_top =None
        def assign_data(self,glass_top, wooden_top):
                self.__glass_top=glass_top
                self.__wooden_top=wooden_top
        def identify_rate (self, glass_top,wooden_top):#
                self.assign_data(glass_top, wooden_top)
                if(self.__glass_top==True):
                        rate=20000
                elif(self.__wooden_top==True):
                        rate=30000
                else:
                        rate=0
                return rate

dining_table=table()
rate=dining_table.identify_rate(False, True)
print(rate)
'''
'''
class table:
        def __init__(self):
                print(id(self))
                self.no_of_legs=4
                self.glass_top=None
                self.wooden=None
dining_table=table()
back_table=table()
front_table=back_table
back_table=dining_table
print(id(dining_table),id(back_table),id(front_table))
'''
#question
'''
class wecare:
        def __init__(self):
                self.__Id=None
                self.__cost=None
                self.__type=None
                self.__pre=None
        def setvalues(self,Id,type,cost):
                self.__Id=Id
                self.__cost=cost
                self.__type=type
               
        def prem(self):
                if self.__type=="Two Wheeler":
                        self.__pre=(self.__cost*0.02)
                elif self.__type=="Four Wheeler":
                    self.__pre=self.__cost*0.06
                else:
                        self.__pre=-1
        def getvalues(self):
            if self.__pre != -1:
                print(self.__Id,self.__cost,self.__type,self.__pre)
            else:
                print("invalid Input")
ob=wecare()
ob.setvalues("101","Two Wheeler",22000)
ob.prem()
ob.getvalues()
'''
