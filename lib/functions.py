#!/usr/bin/env python3

def greet_programmer():
    print('Hello, programmer!')

def greet(name):
    print(f'Hello, {name}!')
   
greet('Naureen')

def greet_with_default(name="programmer"):
    print(f'Hello, {name}!')

def add(num1, num2):
    print(num1+ num2)
    
add(45,55)    

def halve(number):
    return number / 2

result = halve(100)
print(result)
  
