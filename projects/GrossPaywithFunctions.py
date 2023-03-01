

def compute_pay(hrs, rte):
    if hours <= 40:
        pay = round(hrs * rte, 2)
    else:
        extra_hour = hrs - 40
        hour = hrs - extra_hour
        pay = round(hour * rate + 1.5 * rte * extra_hour, 2)
    return pay


def type_of(i_input):
    try:
        val = float(i_input)
        return val

    except valueError:
        print("Error!")

hours = float(input("enter hours: "))
hours = type_of(hours)
rate = float(input("enter rates: "))


output = compute_pay(hours, rate)
print(output)
print(type_of())
