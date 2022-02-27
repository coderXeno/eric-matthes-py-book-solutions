sandwich_orders = ['cheese','onion','pastrami','ham','pork','pastrami','tomato','egg','pastrami']

print("The deli has run out of pastrami")
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

finished_sandwiches = []

while sandwich_orders:
    current_order = sandwich_orders.pop()
    print("I made your "+current_order+" sandwich order")
    