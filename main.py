print("Welcome to the tip calculator!")
bill=float(input("What was the total bill? ₹"))
tip=float(input("What percentage tip would you like to give? 10, 12, or 15? "))
num=float(input("How many people split the bill? "))
total_tip=(bill*tip)/100
total_bill=bill+total_tip
each=total_bill/num
each2=round(each,2)
print("Each person should pay: ₹", each2)
