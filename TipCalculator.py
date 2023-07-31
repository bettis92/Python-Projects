bill_total = float(input("What was the total bill? $"))
tip_perc = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
num_people = int(input("How many people to split the bill? "))


bill_total = round(bill_total, 2)
total_w_tip = ((tip_perc / 100)+1) * bill_total
div_num = total_w_tip / num_people

print(f"Each person should pay: ${round(div_num, 2)}")