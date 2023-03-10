# mortgage.py
#
# Exercise 1.7
principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
months = 0
extra_payment_month_start = 61
extra_payment_month_end = 108
extra_payment = 1000

while principal > payment:
    months += 1
    if principal < payment:
        payment = principal

    principal = principal * (1 + rate / 12) - payment
    total_paid = total_paid + payment
    if months >= extra_payment_month_start and months <= extra_payment_month_end:
        total_paid += extra_payment
        principal -= extra_payment
    print(months, round(total_paid, 2), round(principal, 2))
months += 1
total_paid += principal

print('Total paid', round(total_paid, 2))
print(months)