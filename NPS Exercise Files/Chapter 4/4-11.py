pizzas = ["chicken","cheese","onion"]

for pizza in pizzas:
    print(pizza)

for pizza in pizzas:
    print("I really like "+pizza.title()+" pizza")

print("bla bla bla")
print("bla bla bla")
print("I really love pizza")

print("_____________________________")
friend_pizzas = pizzas[:]
pizzas.append("pork")
friend_pizzas.append("pepperoni")

print("My favourite pizzas are: ")
for pizza in pizzas:
    print(pizza)

print("My friend's favourite pizzas are: ")
for pizza in friend_pizzas:
    print(pizza)