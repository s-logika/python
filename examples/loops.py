#for i in range(8):
for i in range(4,9):
    print(i)





# Simple Calculator Program in Python
def add(x, y): return x + y
def subtract(x, y): return x - y
def multiply(x, y): return x * y
def divide(x, y): return x / y if y != 0 else "Error"

print("Select: 1.Add, 2.Sub, 3.Mult, 4.Div")
while True:
    choice = input("Enter choice (1-4): ")
    if choice in ('1', '2', '3', '4'):
        n1 = float(input("First number: "))
        n2 = float(input("Second number: "))
        if choice == '1': print(add(n1, n2))
        elif choice == '2': print(subtract(n1, n2))
        elif choice == '3': print(multiply(n1, n2))
        elif choice == '4': print(divide(n1, n2))
        if input("Another? (y/n): ").lower() != 'y': break
    else: print("Invalid Input")
