# hour = input("Enter Hours: ")
# rate = input("Enter Rate: ")
# hour = float(hour)
# rate = float(rate)
# extra_hour = 0
# if hour <= 40:
#    pay = round(hour * rate, 2)
# else:
#     extra_hour = hour - 40
#     hour = hour - extra_hour
#     pay = round(hour * rate + 1.5 * rate * extra_hour, 2)
# print(f"Pay: {pay}")

try:
    hours = float(input("enter hours: "))

except valueError:

    print("wrong input")
    hours = float(input("try enter hours again: "))
    rates = float(input("try enter rates again: "))
if hours > 40:
    extra_hours = hours - 40
    gross_pay = round(40 * rates + (extra_hours * 1.5 * rates), 2)
    print(f"your salary is {gross_pay}")
else:
    gross_pay2 = hours * rates
    print(f"your salary is {gross_pay2}")
