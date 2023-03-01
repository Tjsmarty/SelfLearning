# first = int(input("enter first number: "))
# second = int(input("enter second number: "))


def summation(number_1, number_2):
    first = int(input("enter first number: "))
    second = int(input("enter second number: "))


# cal = summation(first, second)
# print(cal)
"""Hello"""
a = 10
b = 20

c = a
a = b
b = c

# print(f"a = {a}")
# print(f"b = {b}")
# c = (2 * 2 + 2 / 2 - 2)
# print(4 * " Teejay")
# name = input("What\nis ur name? ")

# print(name)

# age = int(input("what is your age? \n"))
# newAge = str(age)
# print("my age is " + newAge)
#
# year = int(input("enter year: "))
# # week = year * 52
# # print(f" There are {week} weeks in {year} years")
# print(round(3.4567896754, 3))
# hours = float(input("enter hours: "))
# rates = float(input("enter rates: "))
# pay = round(hours * rates, 2)
# print(pay)
# celsius = int(input("enter temp in celsius: "))
# fahrenheit = int((celsius * 9/5) + 32)
# print(f" {fahrenheit} fahrenheit")
# days = int(input("How many days will you stay? "))
# hotel = float(input("How much does hotel cost per night?$ "))
# flight = float(input("How much does flight cost?$ "))
# car_rent = float(input("if you need rental of car please enter the price otherwise enter zero:$ "))
# others = float(input("enter other possible expenses?$ "))
# totalCost = float((days * hotel) + flight + (days * car_rent) + others)
# print(f"Total Cost:$ {totalCost}")
# print(1 >= 2)

# number = int(input("enter no: "))
# if number % 2 == 0:
#     print("even")
# else:
#     print("odd")
#
# height = float(input("Enter your height in m: "))
# weight = float(input("Enter your weight in kg: "))
# bmi = round(weight / height ** 2,2)
# if bmi < 18.5:
#     print(f"Your BMI is {bmi}, you are underweight")
# elif bmi < 25:
#     print(f"Your BMI is {bmi}, you weight is normal")
# elif bmi < 30:
#     print(f"Your BMI is {bmi}, you are overweight")
#
# else:
#     print(f"Your BMI is {bmi}, you are obese")
# try:
#     number = int(input("enter number: "))
# except:
#     print("You did not enter a valid value")
# else:
#     print(f"number is {number}")
# hours = float(input("enter hours: "))
# rates = float(input("enter rates: "))
# if hours > 40:
#     extra_hours = hours - 40
#     gross_pay = round(40*rates + (extra_hours*1.5*rates), 2)
#     print(f"your salary is {gross_pay}")
# else:
#     gross_pay2 = hours * rates
#     print(f"your salary is {gross_pay2}")

# score = float(input("enter a score between 0.0 and 1.0: "))
#
#
# if score < 0.0 or score > 1.0:
#     print("score is out of range")
#
# elif score >= 0.9:
#     print("A")
# elif score >= 0.8:
#     print("B")
# elif score >= 0.7:
#     print("C")
# elif score >= 0.6:
#     print("D")
# else:
#     print("F")

#
# import math
#
# r = int(input("enter radius: "))
# area = round(math.pi * r**2, 2)
# print(f"The area of a circle is: {area}")
import math

r = int(input("enter radius: "))
area = round(math.pi * pow(r,2), 2)
print(f"The area of a circle is: {area}")

