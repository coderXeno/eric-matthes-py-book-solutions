guests = ["sam","mike","darren"]

for i in range(len(guests)):
    print("Hello, "+guests[i].title()+" you are invited to dinner")

print(guests[0]+" cant make it to dinner unfortunately")
guests[0] = "alicia"
for i in range(len(guests)):
    print("Hello, "+guests[i].title()+" you are invited to dinner")
