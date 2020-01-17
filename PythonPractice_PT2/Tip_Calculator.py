# Prompt the user for two things: 
# 1. Total bill amount 2. Level of service : Good, Fair, or Bad
# Calculate tip amount and the total amount (bill amount + tip amount)
# good -> 20% fair -> 15% bad -> 10%

# Asking the total bill amount with a float just incase there is change? 
bill_amount = float(input("What was your bill total? ))

service = input("How was the service? good, fair, or bad?" )

# To be honest not sure if I need the or's I didn't try just thought 
# it would save me a little debugging 
if service == "good" or "Good":
    total_tip = .20 * bill_amount

if service == "fair" or "Fair":
    total_tip = .15 * bill_amount

if service == "bad" or "Bad":
    total_tip = .10 * bill_amount

print("You should leave $%.2f " % (total_tip))

# % Modulus	Divides left hand operand 
# by right hand operand and returns remainder