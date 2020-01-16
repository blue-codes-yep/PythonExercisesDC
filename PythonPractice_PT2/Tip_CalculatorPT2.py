
# Same ole stuff from PT1

bill_amount = float(input("What was your bill total? "))

service = input("How was the service? good, fair, or bad? ")

amount_of_people = int(input("How many people are splitting the check? "))

# Same ole stuff from PT1 prolly needs work 

if service == "good" or "Good":
    total_tip = .20 * bill_amount

if service == "fair" or "Fair":
    total_tip = .15 * bill_amount

if service == "bad" or "Bad":
    total_tip = .10 * bill_amount

print("You should leave $%.2f " % (total_tip / amount_of_people))