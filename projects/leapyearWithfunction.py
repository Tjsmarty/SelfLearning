yr = int(input("enter year: "))


def leap(yr):
    if yr % 4 == 0:
        if yr % 100 == 0:
            if yr % 400 == 0:
                return f"{yr} is a leap year"
            else:
                return f"{yr} is not a leap year"
        else:
            return f"{yr} is a leap year"

    else:
        return f"{yr} is not a leap year"


print(leap(yr))