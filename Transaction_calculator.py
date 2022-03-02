import math

print("Would you like to do an investment or bond: \n1. investment \n2. bond\n")
trans_type = float(input()) 
#bond = float(input())

if trans_type == 1:
    #INVESTMENT
    P = float(input("Enter amount being deposited: "))
    t = float(input("Enter number of years of investment: "))   
    i = float(input("Enter interest rate: "))
    interest = input("Simple or Compound interest?\n1. simple\n2. compound\n ")
    r = i/100 
    #Simple interest
    if interest == "1":
        amount = round(P*(1+r*t) ,2)
        print("R", amount)
        
    #Compound interest
    elif interest == "2":
        amount = round(P * math.pow((1 + r), t),2)
        print("R", amount)
    
    else:
        print("You entered an invalid number")
        
#BOND
elif trans_type == 2:
    print("Please enter the present value of the house: ")
    house_value = int(input("R"))
    
    print("Please enter your interest rate: ")
    r = int(input())
    
    print("Please enter the number of months you plan to take to repay the bond: ")
    num_months = int(input())
    
    monthly_repayment = round((r / 100 / 12 * house_value) / (1 - math.pow((1+ r / 100 / 12), (-1 * num_months))), 2)
    
    print("Your monthly repayment amount for the home loan is equal to R{}.".format(monthly_repayment))

else:
    print("You entered an invalid output")