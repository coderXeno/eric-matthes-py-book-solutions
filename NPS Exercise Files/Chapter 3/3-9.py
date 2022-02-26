guests = ["sam","mike","darren"]

for i in range(len(guests)):
    print("Hello, "+guests[i].title()+" you are invited to dinner")

print(" ")
print(guests[0]+" cant make it to dinner unfortunately")
guests[0] = "alicia"
for i in range(len(guests)):
    print("Hello, "+guests[i].title()+" you are invited to dinner")

print("Hello, I just reserved a bigger dinner table so now there's room for more people")
guests.insert(0,"john")

middle_index = (len(guests)/2).__ceil__();
guests.insert(middle_index,"janet")

guests.insert(len(guests),"brown")

for i in range(len(guests)):
    print("Hello, "+guests[i].title()+" you are invited to dinner")

c = 0
for i in range(len(guests)):
    c = c + 1

print("No of guests invited to dinner: ",c)