import math


def calculate(height, width):
    area = height * width
    number_can = math.ceil((area / 4))
    print(f"{number_can} can of paint will cover {area} square meter")


tall = int(input("enter height: "))
wide = int(input("enter width: "))

calculate(tall, wide)
