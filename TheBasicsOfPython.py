
# wykład 20

# print(7*6)
# print("h"+"w")
# gree = "ziomek"
# tree = "gra"
# print(gree + ' ' + tree)

# wykład 21

# greetinr = "Hello"
# name = input("Please enter name")
# print(greetinr + ' ' + name)

# splitString = "this string has been\nsplit\nseveral\nlines"
# print(splitString)
# tabbstring = "1\t2\t3\t4\t5\t"
# print(tabbstring)
# print('the pet shop owner said "No, no, \'e\'s uh ...he\'s resting"')
# print("the pet shop owner said \"No, no, 'e's uh ...he's resting\"")
# anotherSplitString = """this
# will
# be
# split"""
# print(anotherSplitString)
# print('''the pet shop owner said "No, no, 'e's uh ...he's resting''')
# print("""the pet shop owner said "No, no, 'e's uh ...he's resting""")


# a = 12
# b = 3
# print(a + b)
# print(a - b)
# print(a * b)
# print(a / b)
# print(a // b)
# print(a % b)

# for i in range(1, a//b):
#     print(i)

# Wykład 23
# c = a + b
# d = c / 3
# e = d - 4
# print(e * 12)

# parrot = "Norwegian Blue"
# print(parrot)
# print(parrot[0])
# print(parrot[3])
# print(parrot[-1])
# print(parrot[0:6])
# print(parrot[:6])
# print(parrot[6:])
# print(parrot[-4:-2])
# print(parrot[0:6:2])
# print(parrot[0:7:6])
# number = "9,223,372,036"
# print(number[1::4])
# numbers = "1, 2, 3, 4, 5, 6"
# print(numbers[0::3])
#
# print("Hello " * 5)
# print("Hello " * (5 + 4))
# print("Hello " * 5 + "4")
#
# today = "friday"
# print("day" in today)
# print("fri" in today)
# print("thur" in today)
# print("parrot" in "frord")

# Wykład 24

age = 24
# print("My age is " + str(age) + " years")
# print("My age is {0} years".format(age))
# print("There are {0} days in {1}, {2}, {3}, {4}, {5}, {6} and {7} ".format
#       (31, "January", "March", "May", "July", "August", "October", "December"))

# print("""January: {2}
# February: {0}
# March: {2}
# April: {1}
# May: {2}
# June: {2}""".format(28, 30, 31))

# TYLKO PYTHON 2

# print("My age is %d years" % age)
# print("My age is %d %s, %d %s" % (age, "years", 6, "months"))
#
# for i in range(1, 12):
#     print("No. %2d squered is %4d and cubed is %4d" % (i, i ** 2, i ** 3))
# for i in range(1, 12):
#     print("No. %d squered is %d and cubed is %d" % (i, i ** 2, i ** 3))
#
# print("Pi is approximately %12f" % (22 / 7))
# print("Pi is approximately %12.50f" % (22 / 7))

# Python 3
for i in range(1, 12):
    print("No. {0:2} squered is {1:4} and cubed is {2:4}".format(i, i ** 2, i ** 3))

for i in range(1, 12):
    print("No. {0:2} squered is {1:<4} and cubed is {2:<4}".format(i, i ** 2, i ** 3))

print("Pi is approximately {0:12f}".format(22 / 7))
print("Pi is approximately {0:12.50f}".format(22 / 7))