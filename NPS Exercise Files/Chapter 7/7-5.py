cost = 0

while(True):
    print("Type 'quit' to exit the process")
    p = input("Enter the age of the person: ")
    if(p.lower() == 'quit'):
        print("Your total cost will be: ",cost,"$")
        break   
    else:
        person = int(p)
        if(person < 3):
            cost = cost + 0
            print("Your ticket will be free!")
        elif(person >= 3 and person < 12 ):
            cost = cost + 10
            print("Your ticket will cost 10$")
        elif(person >= 12):
            cost = cost + 15
            print("Your ticket will cost 15$")