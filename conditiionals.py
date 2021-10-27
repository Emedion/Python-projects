print('price of house is 10million naira')
credit_status = input("Enter g if your credit is good and n if otherwise: ")
if credit_status == 'g':
    down_payment = 10000000 * 0.1
    print(f'You are expected to pay a down payment of {down_payment}')
elif credit_status == 'n':
    down_payment = 10000000 * 0.2
    print(f'You are expected to pay a down payment of {down_payment}')
else:
    print(f'Invalid entry.')

'''
Logical operators:
AND - both conditions are true
OR - One of the conditions is true
NOT - Returns opposite result
'''

name = input("Enter your name: ")
if len(name) < 3:
    print(f"Name must be more than 3 characters.")
elif len(name) > 50:
    print(f"Name must not be more than 50 characters.")
else:
    print("Name is just fine.")


weight = int(input('Weight: '))
unit = input('(L) lbs or (K) Kilos: ').lower()
if unit == 'l':
    kilo = weight * 0.45
    print(f'You are {kilo} kilos')
elif unit == 'k':
    pounds = weight/0.45
    print(f'You are {pounds} lbs')
else:
    print('Invalid entry')