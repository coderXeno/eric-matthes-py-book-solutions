def make_car(manufacturer_name,model_name,**props):
    car = {
        'manufacturer': manufacturer_name,
        'model': model_name,
    }

    for prop,value in props.items():
        car[prop] = value

    print(car)

car = make_car('subaru', 'outback', color='blue', tow_package=True)