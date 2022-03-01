print("Welcome to the Tip Calculator.")

bill = float(input("What was the total bill? $"))
tip_percentage = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))

bill_with_tip = bill * (100 + tip_percentage) / 100

bill_per_person = bill_with_tip / people

# Rounding the bill to 2 decimal places
final_amount = "{:.2f}".format(bill_per_person)

# Formatting the output
print(f"Each person should pay: ${final_amount}")
