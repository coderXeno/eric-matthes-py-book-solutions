favorite_numbers = {
    'jen': [42,35],
    'sarah': [36,21],
    'edward': [24,17],
    'phil': [45,84],
    'john': [17,65]
}

for person,numbers in favorite_numbers.items():
    print("Favorite Numbers of "+person.title()+" are: ")
    for number in numbers:
        print(number,"\n")