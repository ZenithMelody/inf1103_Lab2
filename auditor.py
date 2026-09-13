inventory = 0
failed_Enteries = 0

while True:

    user_Input = input("Enter stock (or quit to exit): ")

    if user_Input == "quit":
            break

    if not user_Input.isdigit():
         print("Try again")
         failed_Enteries += 1
         continue

    amount = int(user_Input)

    inventory += amount

    if inventory > 500:
        print("Over limit of 500")
        break

print("\nReport Summary")
print(f"fTotal Units Processed: {inventory}")
print(f"Number of Failed/Rejected Entries: {failed_Enteries}")