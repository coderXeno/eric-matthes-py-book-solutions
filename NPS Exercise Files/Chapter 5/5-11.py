numbers = []

for i in range(0,10):
    numbers.append(i)

for number in numbers:
    if(number == 1):
        print(number,"st\n")
    elif(number == 2):
        print(number,"nd\n")
    elif(number == 3):
        print(number,"rd\n")
    else:
        print(number,"th\n")