# This version is my public version that does not have some features (that i will be adding)

from datetime import datetime
import turtle
import time

def add(x, y):
  return x + y
def subtract(x, y):
  return x - y
def multiply(x, y):
  return x * y
def divide(x, y):
  return x / y
def now():
          return datetime.now().strftime('%d/%m/%Y %H:%M:%S')

tr = turtle.Turtle()
wn = turtle.Screen()
wn.addshape('PyShell.gif')
tr.shape('PyShell.gif')
tr.left(90)
tr.left(90)
tr.left(90)
tr.left(90)
tr.left(90)
Un = input('UserName: \u001b[32m')
time.sleep(2)
print('\u001b[0m')
print(' __________ ')
print('|  \u001b[33mPy\u001b[34mShell\u001b[0m |')
print('|    by    |')
print('| EMS16218 |')
print('|__________|')
time.sleep(2)
print('')
print('>>> \u001b[33mPy\u001b[34mShell\u001b[0m 0.0.8')
print('>>> Type "help" for list of commands.')

while True:
 print('')
 q = input('\u001b[32m' + Un + '@\u001b[33mPy\u001b[34mShell\u001b[0m\u001b[34m >>> \u001b[36m')
 print('\u001b[0m')
 if q == 'help':
  print('>>> calculator, datetime, info, EndProcess, Madlibs')
 elif q == '':
   print('>>> ')
 elif q == 'datetime':
   print('{}'.format(now()))
 elif q == 'info':
   print('>>> Version: \u001b[36m0.0.8\u001b[0m')
   print('>>> type: \u001b[34mShell\u001b[0m')
   print('>>> Source: \u001b[33mPython\u001b[0m')
   print('>>> Creator: \u001b[32mems16218@penguin\u001b[0m')
   print('>>> Version type: \u001b[31mAlpha\u001b[0m')
 elif q == 'Madlibs':
   N1 = input('>>> Noun: ')
   AJ1 = input('>>> Adjective: ')
   V1 = input('>>> Verb: ')
   AV1 = input('>>> Adverb: ')
   print('>>> The ' + AJ1 + ' ' + N1 + ' ' + V1 + ' ' + AV1 + '.')
 elif q == 'calculator':
   while True:
     print("Select operation.")
     print("1. M")
     print("2. D")
     print("3. A")
     print("4. S")
     print("5. Exit")
     choice = input("Enter choice(1/2/3/4/5): ")
    
     print
     
  
     if choice in ('1', '2', '3', '4', '5'):
           if choice == '1':
             num1 = float(input("Enter first number: "))
             num2 = float(input("Enter second number: "))            
             print(num1, '*', num2,  '=', multiply(num1, num2))
             print
             print
           elif choice == '2':
             num1 = float(input("Enter first number: "))
             num2 = float(input("Enter second number: "))
             print(num1, "/", num2, "=", divide(num1, num2))
             print
             print
           elif choice == '3':
             num1 = float(input("Enter first number: "))
             num2 = float(input("Enter second number: "))
             print(num1, "+", num2, "=", add(num1, num2))
             print
             print
           elif choice == '4':
             num1 = float(input("Enter first number: "))
             num2 = float(input("Enter second number: "))
             print(num1, "-", num2, "=", subtract(num1, num2))
             print
             print
           elif choice == '5':
             break
 elif q in ('EndProcess', 'endprocess'):
   break