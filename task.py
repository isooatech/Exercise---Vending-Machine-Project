import Table_setup as ts
import pandas as pd

def receive_input():
    choice_range = ['1', '2', '3', '4']
    choice = input("Welcome to the vending machine. Select an option:\n1. Login (admin only)\n2. Add products (admin only)\n3. Buy products\n4. Exit\n").strip()
    while choice not in choice_range:
        choice = input("Invalid option. Try again.\nWelcome to the vending machine. Select an option:\n1. Login (admin only)\n2. Add products (admin only)\n3. Buy products\n4. Exit\n").strip()
    return choice

def input_handler(choice):
    if choice == '2':
        add_products()
    if choice == '3':
        buyproducts()


def logincheck():
    print("Login First!")

def add_products():
    print("This is the current stock of the vending machine:\n", ts.df)
    slot = input("Select a slot to add one more product:\n").strip()

    while slot not in ts.df.index or pd.isnull(ts.df['amount'][slot]) or ts.df['amount'][slot]==8:
        if slot not in ts.df.index:
            slot= input("Invalid slot, try again\n").strip()
        elif slot ==8:
            slot = input("this slot has already the max amount permitted, try another one\n").strip()
        else:
            slot=input("No products left on this slot, try another one\n").strip()

    addition = 1.0
    amount_left = ts.df['amount'][slot]
    new_amount = amount_left + addition
    ts.df.loc[slot, 'amount'] = new_amount

    print("the product has been added, here is the updated stock:\n", ts.df)


def buyproducts():
    print("This is the current stock of the vending machine:\n", ts.df)
    slot = input("Select a product to buy:\n").strip()
    while slot not in ts.df.index or pd.isnull(ts.df['amount'][slot]):
        if slot not in ts.df.index:
            slot= input("Invalid slot, try again\n").strip()
        else:
            slot=input("No products left on this slot, try another one\n").strip()
    print(f"Product to buy: {ts.df['snack'][slot]}\nPrice: {ts.df['price'][slot]}")

    amount = input("Please enter the amount of money to pay:\n")

    while isinstance(amount, float) == False :
        try:
            amount = float(amount)
            if amount < 0:
                amount = input('you inserted "negative" money! try again!\n').strip()
                continue
            elif amount < ts.df['price'][slot]:
                amount= input("you need to pay more, try again\n").strip()
                continue
            else:
                break
        except:
            print("please enter a number")
            amount = input("Please enter the amount of money to pay:").strip()

    amount_intended = amount // ts.df['price'][slot]
    amount_left = ts.df['amount'][slot]
    price = ts.df['price'][slot]
    purchase = False
    if amount_left == 0.0:
        print("there is no stuck for now for the chosen item")
    elif amount_intended <=amount_left:
        change = amount-(amount_intended*price)
        amount_bought = amount_intended
    else:
        change = amount - (amount_left*price)
        amount_bought = amount_left
    print(amount_intended)
    print(amount_left)
    print(amount_bought)
    snack_left = amount_left - amount_bought
    ts.df.loc[slot, 'amount'] = snack_left
    print(f"Your change is {change}\nThe number of snacks left in {slot} is {snack_left}")


def login_handler():
    attempt = 0
    user = input("Please enter your username\n").strip()
    while user != 'admin':
        attempt += 1
        print(f"Invalid username, current attempts are {attempt}")
        if attempt <4:
            user = input("Please enter your username\n").strip()
        else:
            break
    password = 0
    if user == 'admin':
        password = input("Please enter your password:\n")
        while password not in ['0','1','2','3','4','5','6','7','8','9']:
            attempt += 1
            if password.isdigit():
                print(f"invalid password, current attempts are {attempt}")
            elif password.isalpha():
                print(f"password should be a number, current attempts are {attempt}")
            elif password.isalnum():
                print(f"password should be a number, current attempts are {attempt}")

            if attempt < 4:
                password = input("Please enter your password\n").strip()
            else:
                break
    choice = 0
    if user=='admin' and password in ['0','1','2','3','4','5','6','7','8','9']:
        print('login successful')


    return user, password







def main():
    while True:
        choice = receive_input()
        retry = 'yes'
        if choice == "1":
            user, password = login_handler()
            if user=='admin' and password in ['0','1','2','3','4','5','6','7','8','9']:
                choice = receive_input()
                while choice == '1':
                    print("You already logged in, back to main menu")
                    choice = receive_input()
                if choice == '2':
                    add_products()
                if choice == '3':
                    input_handler(choice)
                if choice == '4':
                    retry = 'no'
                    print(retry)
            else:
                retry = input("Login attempts exhausted, enter 'yes' to retry or any other key to exit\n").lower().strip()
                print(retry)
        elif choice == '2':
            logincheck()
        elif choice == '3':
            input_handler(choice)
        else:
            retry = 'no'
        if retry != 'yes':
            break


if __name__ == "__main__":
	main()

#while True:

    #if restart.lower() != 'yes':
        #break