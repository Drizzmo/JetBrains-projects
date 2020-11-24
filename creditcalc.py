import math

# principal = int(input("Enter loan principal: "))
# per_month = int(input("Enter the monthly payment: "))
# loan_interest = int(input("Enter the loan interest: "))
# pay_count = int(input("Enter the number of periods: "))

#

decision = input("What do you want to calculate?\n\
type 'n' for number of monthly payments,\n\
type 'a' for annuity monthly payment amount,\n\
type 'p' for loan principal: ")

# define the functions for each option here

# Calculating the number of monthly payments (n) in this function


def num_monthly_payments():
    p = float(input("Enter loan principal: "))
    a = float(input("Enter the monthly payment: "))
    loan_interest = float(input("Enter the loan interest: "))
    i = loan_interest / (12 * 100)
    n = round(math.log(float(a) / (float(a) - i * float(p)), i + 1))
    year = n // 12
    month = round(n % 12) + 1
    if year > 0 and month > 0:
        print("It will take", year, "years and", month, "months to repay this loan!")
    elif year > 1 and month == 0:
        print("It will take", year, "years to repay this loan!")
    elif year == 0 and month > 1:
        print("It will take", month, "months to repay this loan!")
    elif year == 1 and month == 0:
        print("It will take", year, "year to repay this loan!")
    elif year == 0 and month == 1:
        print("It will take", month, "month to repay this loan!")

# calculating the monthly payment (A) here


def monthly_payment():
    p = float(input("Enter loan principal: "))
    n = int(input("Enter the number of periods: "))
    loan_interest = float(input("Enter the loan interest: "))
    i = loan_interest / (12 * 100)
    a = math.ceil(p * ((i * (1 + i) ** n) / (((1 + i) ** n) - 1)))
    print(f"Your monthly payment = {int(a)}!")


def loan_principal():
    a = float(input("Enter the monthly payment: "))
    n = int(input("Enter the number of periods: "))
    loan_interest = float(input("Enter the loan interest: "))
    i = loan_interest / (12 * 100)
    p = a / ((i * (1 + i) ** n) / ((1 + i) ** n - 1))
    print(f"Your loan principal = {int(p)}!")


if decision == "n":
    num_monthly_payments()
elif decision == "a":
    monthly_payment()
elif decision == "p":
    loan_principal()
