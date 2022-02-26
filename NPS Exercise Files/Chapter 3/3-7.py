from traceback import print_tb
guests = ["sam","mike","darren"]

for i in range(len(guests)):
    print("Hello, "+guests[i].title()+" you are invited to dinner")

print("------------------------------------------")
print(guests[0]+" cant make it to dinner unfortunately")
guests[0] = "alicia"
for i in range(len(guests)):
    print("Hello, "+guests[i].title()+" you are invited to dinner")

print("------------------------------------------")

print("Hello, I just reserved a bigger dinner table so now there's room for more people")
guests.insert(0,"john")

middle_index = (len(guests)/2).__ceil__();
guests.insert(middle_index,"janet")

guests.insert(len(guests),"brown")

for i in range(len(guests)):
    print("Hello, "+guests[i].title()+" you are invited to dinner")

print("------------------------------------------")

print("The new table wont make it in time for dinner. I can only invite two people")

for i in range(len(guests)):
    if(len(guests)!=2): #
        print(guests[i-1].title()+" ,We're sorry we cant invite you.")
        guests.pop(i-1)
    else:
        break

print("------------------------------------------")

for i in range(len(guests)):
    print(guests[i].title()+" You're still invited! make sure to come")

print("------------------------------------------")

del guests[0:2]
print(guests)