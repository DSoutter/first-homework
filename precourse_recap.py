#In the file, create a simple Python guessing game using:
# Guessing game for what city I live in. 

city = input("What city do I live in? ")
if city.upper() == "EDINBURGH":
    print("Yes!")
elif city.upper() == "SCOTLAND":
    print("Scotland is not a city")
else:
    print("No, better luck next time.")