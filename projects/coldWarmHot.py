enter = str(input("enter number: "))


def weather(temperature):
    if enter > "28":
        return "Hot"
    elif "18" <= enter <= "28":
        return "warm"
    else:
        return "cold"


new = weather(enter)
print(new)
