import math

princical = int(input("Enter the loan capital: "))


def m():
    per_month = int(input("Enter the monthly payment: "))
    month_payments = -(-princical // per_month)
    if month_payments == 1:
        print("It will take", per_month, "month to repay the loan")
    else:
        print("It will take", month_payments, "months to repay the loan")


def p():
    no_months = int(input("Enter the number of months: "))
    month_amount = math.ceil(float(princical) / float(no_months))
    last_pay = princical - (no_months - 1) * month_amount

    if month_amount > last_pay:
        print("Your monthly payment =", month_amount, "and the last payment =", last_pay)
    else:
        print("Your monthly payment =", int(month_amount))


print("What do you want to calculate?")
choice = input("type 'm' - for number of monthly payments,\ntype 'p' - for the monthly payment:")
if choice == "m":
    m()
else:
    p()
