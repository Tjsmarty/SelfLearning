number1 = int(input("enter first number: "))
number2 = int(input("enter second number: "))
number3 = int(input("enter third number: "))


def num_max(int1, int2, int3):
    if number1 > number2 and number1 > number3:
        return number1
    elif number2 > number3 and number2 > number1:
        return number2
    elif number3 > number1 and number3 > number2:
        return number3


input_num = num_max(number1, number2, number3)
print(f" The maximum number is {input_num}")
