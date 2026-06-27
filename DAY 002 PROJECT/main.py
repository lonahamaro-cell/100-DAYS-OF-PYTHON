# TIP CALCULATOR


print("welcome to a tip calculator!")
bill = float(input("how much is you bill? $ "))
tip = int(input("How much tip would you like to give? 10, 12, or 15?"))

people = int(input("How many people would you like?"))

bill_with_tip = tip/100 * bill + bill
print(f"your bill is {bill_with_tip}")

bill_per_person = bill_with_tip/people
print(f"Each will pay: {bill_per_person}")
print(round(bill_per_person, 2))
