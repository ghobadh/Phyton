has_good_credit = True
has_high_income=True
price = 1000000

if(has_good_credit or has_high_income):
    message= "Eligible for loan.They need to put down 10%"
    rate=10

else:
    message="They need to put down 20%"
    rate=20
down_payment=price*rate/100
print(message)
print(f'Down payment: ${down_payment}')