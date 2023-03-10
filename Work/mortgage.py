# mortgage.py
#
# Exercise 1.7
principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
months = 0

while principal > 0:
    months += 1
    
    principal = principal * (1 + rate / 12) - payment
    total_paid = total_paid + payment
    if months < 13:
        total_paid += 1000
        principal -= 1000
    print(total_paid)
    

print ('Total paid', round(total_paid))
print(months)