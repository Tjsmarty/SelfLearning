name1 = input("enter first name: ")
name2 = input("enter first name: ")
name1.lower()
name1.lower()

a = name1.count("t")
b = name1.count("r")
c = name1.count("u")
d = name1.count("e")
if a > 0:
    print(a)
if b > 0:
    print(b)
if c > 0:
    print(c)
if d > 0:
    print(d)
total1 = a + b + c + d

print()
e = name2.count("t")
f = name2.count("r")
g = name2.count("u")
h = name2.count("e")
if e > 0:
    print(e)
if f > 0:
    print(f)
if g > 0:
    print(g)
if h > 0:
    print(h)
total2 = e + f + g + h
print(f" TRUE appear in first name {total1} times")
print(f" TRUE appear in second name {total2} times")
total_true = total1 + total2

print(f"total number of times TRUE appeared in both names is : {total_true}")

print()
i = name1.count("l")
j = name1.count("o")
k = name1.count("v")
l = name1.count("e")
if i > 0:
    print(i)
if j > 0:
    print(j)
if k > 0:
    print(k)
if l > 0:
    print(l)
total3 = i + j + k + l

m = name2.count("l")
n = name2.count("o")
o = name2.count("v")
p = name2.count("e")
if m > 0:
    print(m)
if n > 0:
    print(n)
if o > 0:
    print(o)
if p > 0:
    print(p)
total4 = m + n + o + p
print(f" LOVE appear in first name {total3} times")
print(f" LOVE appear in second name {total4} times")
total_love = total3 + total4

print(f"total number of times LOVE appeared in both names is : {total_love}")
print()

score = str(total_love) + str(total_true)
print(score)

if int(score) <= 10 or int(score) > 85:
    print(f"your score is {score}, you go together like coke and mentos")
elif 40 <= int(score) <= 70:
    print(f"your score is {score}, you are alright together")
else:
    print(f"your score is {score}")

