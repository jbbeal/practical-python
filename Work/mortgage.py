# mortgage.py
#
# Exercise 1.7

principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
month = 1

extra_pay_amount = 1000.0
extra_pay_start = 61
extra_pay_end = 108

while principal > 0:
    if month >= extra_pay_start and month <= extra_pay_end:
        cur_payment = payment + extra_pay_amount
    else:
        cur_payment = payment
    adjusted_principal = principal * (1 + rate / 12)
    cur_payment = min(cur_payment, adjusted_principal)
    principal = adjusted_principal - cur_payment
    total_paid = total_paid + cur_payment
    print(month, round(total_paid), round(principal,1))
    month = month + 1

print('Total paid', round(total_paid), 'in', month-1, 'months')
