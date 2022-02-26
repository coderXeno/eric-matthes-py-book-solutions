cities = {
    'paris':{
        'country':'france',
        'population':2160000,
        'fact':'bla'
    },
    'texas':{
        'country':'US',
        'population':29000000,
        'fact': 'bla'
    },
    'montreal':{
        'country':'Canada',
        'population':1780000,
        'fact':'bla'
    }
}

for city,info in cities.items():
    print("Details about "+city.title()+" is: ")
    for prop,value in info.items():
        print(prop+":",value,"\n")
