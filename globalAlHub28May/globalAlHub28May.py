
def hello():
    print("Hello Everyone!!")
print(hello())

def hello(name):
    print("Hello " + name)
print(hello("Asli"))

def func_in_func(name1):
    return hello(name1)

print(func_in_func("Ugurcan"))

def func1():
    print("Hello World!!")

print(func1())
print("Google")
print(func1())



def func(x,y):
    summ = x + y
    multip = x * y
    return (summ,multip)

t,c = func(23,45)
print(t,c)

print("Sum of the values: " + str(t) + ", Multiplying of the values: " + str(c))

#Let's write a function that it will square the entered number, but will be terminated when you enter the number 5 and give us an error message.
def sqr(x):
    if x == 5:
        return ("Terminated because you entered 5")
    result = x **2
    return (result)
d = sqr(5)
print(d)


#Let's write a function that tells you whether the entered number is positive, negativeor zero.
def func(x):
    if x > 0:
       return ("Positive")
    elif x < 0:
       return ("Negative")
    else:
       return ("Zero")
for i in [-2,5,6,0,-4,-7]:
    print(func(i))

#factorial calculation
#0! = 1
#1!= 1
#2!= 2 * 1 =2
#6! = 6 * 5* 4 *3 * 2 *1 = 720
def factorial(num):
    factorial = 1
    if (num == 0 or num == 1):
        print("Factorial: ", factorial)
    else:
        while (num >= 1):
            factorial = factorial * num
            num -= 1
        print("Factorial: ", factorial)
# 1 * 5 = 5 = factorial
# 5 * 4 = 20
print(factorial(5))


def faktoriyel(sayi):
    faktoriyel = 1
    for i in range(1,sayi+1):
        faktoriyel *= i
    return faktoriyel
print(factorial(5))

#using for loop
def factorial2(num2):
    factorial2 = 1
    if (num2 == 0 or num2 == 1):
        print("Factorial: ", factorial2)
    else:
         for i in range(factorial2, num2+1):
             factorial2 *= i
         print("Factorial: ", factorial2)
print(factorial2(6))

def factorial3(nums):
    factorial3 = 1
    if (nums == 0 or nums == 1):
        return ("Factorial: ", factorial3)
    else:
        for i in range(factorial3, nums+1):
            factorial3 *= i
        return (factorial3)
x = factorial3(4)
print(x)

#lambda function
x=(lambda x: x + 1)(2)
print(x)

full_name = lambda first, last: f'Full name: {first.title()} {last.title()}'
print(full_name('guido', 'van rossum'))

# *args keeps the data as tuple type.
def multp(*args):
    result = 1
    for i in args:
        result *= i
        print(result)
print(multp(4,5,6,7,8,9))

# *args keeps the data as tuple type.
def multp1(*args):
    result = 2
    for i in args:
        result *= i # result = result * i
        print(result)
print(multp1([4,5,6,7]))
print(multp1(2,3,4,5))

def func_kwargs(**kwargs):
    print(kwargs)
func_kwargs(name = "Murat", name2 = "Ömer", number=12345, can='Emir', beril='yılmaz')

def salaryCalc(salary):
    if salary < 0:
        return("Invalid value")
    else:
        if 0 < salary <= 1000:
            salary = salary + salary * 0.15
        elif salary <= 2000:
            salary = salary + salary * 0.1
        elif salary <= 3000:
            salary = salary + salary * 0.05
        else:
            salary = salary + salary * 0.025
        return ("New salary: ", salary)
print(salaryCalc(800))

def salaryCalc2():
    salary = float(input("Please enter your current salary: "))
    if salary < 0:
      return("Invalid value")
    else:
      if 0 < salary <= 1000:
        salary = salary + salary * 0.15
      elif salary <= 2000:
        salary = salary + salary * 0.1
      elif salary <= 3000:
        salary = salary + salary * 0.05
      else:
        salary = salary + salary * 0.025
      return ("New salary: ", salary)

new_salary = salaryCalc2()
print(new_salary)

words = ["artificial","intelligence","machine","learning","python","programming"]
#from random import *
import random as rnd
def randomWord(words):
    index = rnd.randint(0, len(words)-1)
    return words[index]

word = randomWord(words)
print(word)

s = input("Please enter a name: ")
print(s.upper())

#return the index of the element with the highest value in a given list.
myList = [45,7,23,6,12,78]
maxElement = max(myList)
maxIndex = myList.index(maxElement)
print(maxIndex)

#bug example.
num1 = input("Enter the first integer: ")
num2 = input("Enter the second integer: ")
print(num1, "+", num2, "=", num1 + num2)

num3 = input("First integer: ")
num4 = input("Second integer: ")
try:
    num3_int = int(num3)
    num4_int = int(num4)
    print(num3_int, "/",num4_int, "=", num3_int/num4_int)
except ZeroDivisionError:
    print("Please enter the second input different than 0 value!!!")
    ebru = int(input("Enter a integer number"))
