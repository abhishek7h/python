def bruh():
    list = ['USD', 'EUR', 'GBP', 'BTC', 'CAD', 'ETH']
    print(list)
    currency = input("Enter the currency you want to convert to INR: ")

    if currency == "USD":
        usd = float(input("> Enter USD ($): "))
        inr = usd * 82.85
        print(f"${usd} is ₹{inr} ")

    elif currency == "EUR":
        euro = float(input("Enter Euros (€): "))
        inr = euro * 88.33
        print(f"€{euro} is ₹{inr} ")

    elif currency == "GBP":
        gbp = float(input("Enter Pound Sterlings (£): "))
        inr = gbp * 99.93
        print(f"£{gbp} is ₹{inr} ")
        
    elif currency == "BTC":
        btc = float(input("Enter Bitcoin (₿): "))
        inr = btc * 1395644.23
        print(f"₿{btc} is ₹{inr} ")

    elif currency == "CAD":
        cad = float(input("Enter Canadian Dollars ($): "))
        inr = cad * 61.23
        print(f"${cad} is ₹{inr} ")

    elif currency == "ETH":
        eth = float(input("Enter Ethereum (Ξ): "))
        inr = eth * 100854.11
        print(f"Ξ{eth} is ₹{inr} ")
        
    repeat = input("Would you like to run again? y/n ")
    if repeat == "y":
        bruh()
    elif repeat == "n": 
        exit()
bruh()