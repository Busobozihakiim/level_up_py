"""function which can generate a list where the values are square of numbers between 1 and 20 (both included)
 It also prints the first 5 elements in the list."""
store = []
def squares():
    for num in range(1, 21):
        x = num ** num
        store.append(x)
    print(store[:5])

squares()