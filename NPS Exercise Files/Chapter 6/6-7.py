info_1 = {
    'first_name' : 'John',
    'last_name' : 'McMillan',
    'age' : '21',
    'city' : 'Montreal'
}

for item in info_1.keys():
    print(item+": "+info_1[item])

print("-----------------------")

info_2 = {
    'first_name' : 'Grace',
    'last_name' : 'Matthews',
    'age' : '21',
    'city' : 'Montreal'
}

info_3 = {
    'first_name' : 'Katherine',
    'last_name' : 'Bliss',
    'age' : '21',
    'city' : 'Montreal'
}

people = {
    'person_1': info_1,
    'person_2': info_2,
    'person_3': info_3
}

for person,info in people.items():
    print("Details for "+person+":")
    for prop,details in info.items():
        print(prop+": "+details+"\n")