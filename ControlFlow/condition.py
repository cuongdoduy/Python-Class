phone_balance=4
bank_balance=100
if phone_balance < 5:
    phone_balance += 10
    bank_balance -= 10 
elif phone_balance < 10: #else if 
    phone_balance += 20
    bank_balance -= 20
else:
    print("You have enough money to make a call.")

print(phone_balance)
print(bank_balance)


