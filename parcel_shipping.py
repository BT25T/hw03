import sys #Let me use it if you are handsome :D

try:
    weight = float(input("Enter weight in kg: "))
    if weight <= 0 :
        error = True
        print("Please enter a valid weight")
        sys.exit()

    cost = 0
    
    if 0 < weight <= 1:
        cost += 40
    elif weight <= 5:
        cost += 80
    elif weight <= 20:
        cost += 150
    else:
        print("Too heavy (max 20 kg)")
        sys.exit()

    destination = str(input("Enter the destination (bangkok or other): ")).lower()
    if destination not in ["bangkok", "other"]:
        print("Unknown destination")
        sys.exit()

    express = str(input("Enter express (yes/no): ")).lower()

    if destination != "bangkok":
        cost += 30

    if express == "yes":
        cost *= 2

    print(f"Shipping cost: {cost} baht")

except ValueError:
    print("Please enter a valid weight")