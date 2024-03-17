#Hello this is my first project so im rather excited. 
#This is a automated currency exchange rate between SGD and Euro.
#Other exchange rates can be implemented but im too lazy to do that rn. Let's begin.

# from forex_python.converter import CurrencyRates

# def get_exchange_rates():
#     c = CurrencyRates()
#     return {
#         'SGD_to_EUR': c.get_rate('SGD', 'EUR'),
#         'EUR_to_SGD': 1.0 / c.get_rate('EUR', 'SGD')
#     }

# exchange_rates = get_exchange_rates()

exchange_rate_sgd_to_eur = 0.69
exchange_rate_eur_to_sgd = 1/exchange_rate_sgd_to_eur #next time the exchange rate changes i can just edit the sgd to eur value
exchange_rate_sgd_to_won = 984.94
exchange_rate_won_to_sgd = 1/exchange_rate_sgd_to_won

while True: #This is so that the system will continue to prompt for currency exchange unless the user decides to quit
    print("Hello! You are using Joel's currency converter: ")
    print("1. SGD to EUR")
    print("2. EUR to SGD")
    print("3. SGD to WON")
    print("4. WON to SGD")
    print("5. Quit")

    choice = input("Select an option: ")

    if choice == "1":
        sgd_amt = float(input("Enter the amount of SGT you wish to convert: "))
        eur_amt = sgd_amt * exchange_rate_sgd_to_eur
        print("The amount of EUR is:", eur_amt)

    elif choice == "2": 
        eur_amt = float(input("Enter the amount of EUR you wish to convert: "))
        sgd_amt = eur_amt * exchange_rate_eur_to_sgd
        print("The amount of SGD is: ", sgd_amt)

    elif choice == "3":
        sgd_amt = float(input("Enter the amount you wish to convert: "))
        won_amt = sgd_amt * exchange_rate_sgd_to_won
        print("The amount of WON is:", won_amt)

    elif choice == "4":
        won_amt = float(input("Enter the amount you wish to convert: "))
        sgd_amt = won_amt * exchange_rate_won_to_sgd
        print("The amount of SGD is:", sgd3_amt)

    elif choice == "5":
        print("Thank you and goodbye!")
        break

    else:
        print("Invalid answer. Please select 1, 2, 3, 4 or 5.")