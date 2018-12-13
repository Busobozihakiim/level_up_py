"""Make a grading system for the students marks below
[23,4,5,6,64,90,67,98,45,23,67,78,89]
Create two lists and add numbers greater than 50 and another list for numbers less than 50
And show an appropriate message for his mark"""
one = [23,4,5,6,64,90,67,98,45,23,67,78,89]
two = []
three = []
for num in one:
    if num >= 90:
        print(num, "Excellent")
        two.append(num)
    elif num >= 70 and num <= 89:
        print(num, "very good")
        two.append(num)
    elif num >= 60 and num <= 69:
        print(num, "good")
        two.append(num)
    elif num >= 40 and num <= 59:
        print(num, "poor")
        two.append(num)
        three.append(num)
    elif num >= 20 and num <= 39:
        print(num, "very poor")
        three.append(num)
    elif num >= 0 and num <= 19:
        print(num, "repeat")
        three.append(num)
    
print(two)
print(three)