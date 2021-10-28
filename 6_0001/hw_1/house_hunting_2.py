starting_salary = float(input("What is your annual salary?"))
biannual_raise = float(input("What is your biannual raise as a proportion of your salary?"))
portion_saved = float(input("What portion of your salary do you save, as a decimal?"))
total_cost = float(input("What is the cost of your dream home?"))
annual_salary = starting_salary
current_savings = 0
r = 0.04
payment_proportion = 0.25
down_payment = total_cost*payment_proportion
months_count = 0
while(current_savings < down_payment):
    current_savings = current_savings + current_savings*r/12
    current_savings = current_savings + annual_salary*portion_saved/12
    if months_count % 6 == 0 and months_count != 0:
        annual_salary = annual_salary + annual_salary*biannual_raise
    months_count += 1
print("\n\n It will take you " + str(months_count) + "months to save enough for a down payment on your dream home.")


    
    
