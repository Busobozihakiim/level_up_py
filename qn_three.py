"""Write a program which accepts a sequence of comma separated 4 digit binary numbers as its input and 
then check whether they are divisible by 5 or not. The numbers that are divisible by 5 are to be printed 
in a comma separated sequence."""
print("Enter a sequence of comma separated 4 digit binary numbers")
store = []

while True:
    from_user = input("Press return when finished-->")
    to_list = from_user.split(",")
    break

for num in to_list:
    if int(num,10) % 5 == 0:
        store.append(num)
    else:
        pass

print("these are divisible by 5,", store)