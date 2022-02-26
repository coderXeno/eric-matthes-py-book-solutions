favorite_places = {
    'xtremeboi':['paris','new york','texas'],
    'lolbro':['berlin','tokyo','belgium'],
    'bloodc++':['las vegas','sydney','hong kong']
}

for person,places in favorite_places.items():
    print("Favorite Places for "+person.title()+" are: ")
    for place in places:
        print(place.title()+"\n")