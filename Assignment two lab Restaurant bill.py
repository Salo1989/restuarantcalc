#Program allows user to import cost of meal
#Cost of meal is later added into other cost
#cost of tax and tip are added to meal cost
#program displays tax added, tip, meal cost and adds them together to know total cost



print('Welcome to Restaurant Cost Generator')
meal_cost = int(input("Enter meal cost "))
tax_percentage = 0.07
tax_amount = meal_cost * tax_percentage
print("Tax Added:", tax_amount)
tip_owed=0.20
tip_added = meal_cost * tip_owed
print("Added Tip:", tip_added)
total_amount = meal_cost + tax_amount + tip_added
print("Total Bill:", total_amount)
