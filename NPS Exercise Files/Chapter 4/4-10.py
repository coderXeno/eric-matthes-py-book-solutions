#from 3-6
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
print("------------------------------------------")
print("The first three items in the list are: ")
print(guests[:3])

print("------------------------------------------")
print("Three items from the middle of the list are: ")
print(guests[middle_index-1:middle_index+2])

print("------------------------------------------")
print("The last three items in the list are: ")
print(guests[-4:-1])