# Exercise 8-12

def make_sandwich(*toppings):
    print("\nMaking a sandwich with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")
    print("Enjoy your sandwich!")

make_sandwich('ham', 'cheese', 'spinach', 'arbys sauce')
make_sandwich('bacon', 'lettuce', 'tomato', 'mayo')
make_sandwich('peanut butter', 'jelly')

# Exercise 8-14

def make_car(manufacturer, model, **vehicle_info):
    car_info = {
        'manufacturer': manufacturer,
        'model': model,
    }
    car_info.update(vehicle_info)
    return car_info

car = make_car('stellantis', 'jeep', color='spitfire orange', four_wheel_drive = True)

print(car)
