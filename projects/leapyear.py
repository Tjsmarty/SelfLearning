year = int(input("enter year: "))
if year % 4 == 0:
    print(f"{year} is a leap year")

    if year % 100 == 0:
        print(f"{year} is not a leap year")
    else:
        print(f"{year} is a leap year")

    if year % 400 == 0:
        print(f"{year} is a leap year")
    else:
        print(f"{year} is not a leap year")


else:
    print(f"{year} is not a leap year")
