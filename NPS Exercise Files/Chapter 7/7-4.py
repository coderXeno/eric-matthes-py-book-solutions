toppings = []

while(True):
    topping = input("Enter the name of the topping. Type 'quit' to exit\n")
    if(topping == 'quit'):
        print("Exiting process...")
        print("Your toppings are: \n",toppings)
        break
    else:
        print("I will add "+topping+" to your pizza")
        toppings.append(topping)
        continue