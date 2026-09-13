inventory = 0

while True:

    user_Input = input("Enter stock (or quit to exit): ")

    if user_Input == "quit":
            break

    amount = int(user_Input)

    inventory += amount

   

    if inventory > 500:
        print("Over limit of 500")
        break

print("\nReport Summary")
print(f"fTotal Units Processed: {inventory}")
print(f"Number of Failed/Rejected Entries: ")