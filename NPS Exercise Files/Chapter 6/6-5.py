rivers = {
    'nile': 'egypt',
    'thames': 'london',
    'ganga': 'himalayas'
}

for river in rivers.keys():
    print("The "+river.title()+" runs through "+rivers[river].title())