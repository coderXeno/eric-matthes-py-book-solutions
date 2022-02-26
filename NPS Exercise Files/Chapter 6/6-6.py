favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'ruby',
'phil': 'python',
}

favorite_languages['xeno'] = 'javascript'
favorite_languages['db'] = 'r'
favorite_languages['atr'] = 'python',
favorite_languages['jgt'] = 'c++',
favorite_languages['rockz'] = 'javascript'

polls = ['jen','xtremecoder','xeno','mitochondricity','bloodC++']

for person in favorite_languages.keys():
    if person in polls:
        print("Thank you for taking the poll, "+person.title())
    else:
        print("Hello "+person.title()+", Please take the favourite languages poll")