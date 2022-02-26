smokey = {
    'kind': 'dog',
    'owner': 'john'
}

crocboi = {
    'kind': 'dog',
    'owner': 'xtremeboi'
}

unicorn = {
    'type': 'cat',
    'owner': 'katherine'
}

pets = {
    'pet_1': smokey,
    'pet_2': crocboi,
    'pet_3': unicorn
}

for pet,info in pets.items():
    print("Details for "+pet+":")
    for prop,details in info.items():
        print(prop+": "+details+"\n")