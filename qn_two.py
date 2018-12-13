"""Program that accepts sequence of lines as input and prints the lines after making all characters 
    in the sentence capitalized."""
print("Enter a string to be capitalized")
print("Enter q to quit")

while True:
    fromUser = input("-->")
    if fromUser == 'q':
        break
    elif type(fromUser) is not str:
        print(str.upper(fromUser))
    elif type(fromUser) is str and int:
        print(str.upper(fromUser))
    else:
        print("Input must be made of characters from a to z")