
select_size = input("choose burger size, M , N or L: ")
add_mushroom = input("add mushroom, y/n: ")
add_cheese = input("add cheese, y/n: ")

M = 0
N = 0
L = 0
cheese = 0
mush_mini_normal = 0
mush_large = 0
final_bill = 0

if select_size == "M":
    M = 5

    if add_mushroom == "y":
        mush_mini_normal += 1
    else:
        mush_mini_normal = 0

    if add_cheese == "y":
        cheese = 1
    else:
        cheese = 0

    final_bill = M + mush_mini_normal + cheese
    print(f"your final bill is ${final_bill}")

elif select_size == "N":
    N = 8
    if add_mushroom == "y":
        mush_mini_normal += 1
    else:
        mush_mini_normal = 0

    if add_cheese == "y":
        cheese = 1
    else:
        cheese = 0

    final_bill = N + mush_mini_normal + cheese
    print(f"your final bill is ${final_bill}")

elif select_size == "L":
    L = 10
    if add_mushroom == "y":
        mush_large += 2
    else:
        mush_large = 0

    if add_cheese == "y":
        cheese = 1
    else:
        cheese = 0

    final_bill = L + mush_large + cheese
    print(f"your final bill is ${final_bill}")
