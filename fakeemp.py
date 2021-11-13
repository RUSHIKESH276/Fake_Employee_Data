from random import *
alpha='abcdefghijklmnopqrstuvwxyz'
digit='0123456789'
city=['Hyderabad','Chennai','Bangalore','Pune','Delhi','Mumbai']
Designation=['Software Engineer','Senior Software Engineer','Team Leader','Project Lead','project Manager']

def name():
    name=choice(alpha).upper()
    n=randint(2,9)
    for i in range(n):
        name=name+choice(alpha)
    return name


def number():
    a="e-"
    for i in range(4):
        a=a+choice(digit)
    return a
    #print("e-",randint(0,9),randint(0,9),randint(0,9),randint(0,9),sep="")

def salary():
    return uniform(10000,50000)

def city1():
    return choice(city)

def mobile():
    mob=choice('6789')
    for i in range(9):
        mob=mob+choice(digit)
    return mob
    #print(randint(6,9),randint(6,9),randint(6,9),randint(6,9),randint(0,9),randint(0,9),randint(0,9),randint(0,9),randint(0,9),randint(0,9),sep="")

def empdesign():
    return choice(Designation)

def get_emp_data():
    print("Employee name is",name())
    print("Employee id number is",number())
    print("Employee salary is {:.2f}".format(salary()))
    print("Employee City is",city1())
    print("Employee mobile number is",mobile())
    print("Employee Profession is",empdesign())

for i in range(10):
    get_emp_data()
    print(" ")