hour = input("enter Hours: ")
try:
    hour = float(hour)
except ValueError:
    print(" please enter valid hours")
    quit()


rate = input("enter rate: ")
try:
    rate = float(rate)
except ValueError:
    print("please enter valid rate")
    quit()

extra_hour = 0
if hour <= 40:
    pay = round(hour * rate, 2)
else:
    extra_hour = hour - 40
    hour = hour - extra_hour
    pay = round(hour * rate + 1.5 * rate * extra_hour, 2)
print(f"Pay: {pay}")
