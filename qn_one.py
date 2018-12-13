"""program which finds all numbers divisible by 7 but are not a multiple of 5"""

for number in range(2000, 3201):
    if number % 7 == 0 and number % 5 != 0:
        print("{}".format(number), end=",")