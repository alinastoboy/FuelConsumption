def calculate_available_distance(fuel_consumption_per_100_km, the_amount_of_fuel_available):
    """
    >>> calculate_available_distance(4, 60)
    14.0
    """
    distance = (the_amount_of_fuel_available - fuel_consumption_per_100_km / 2) // fuel_consumption_per_100_km
    return distance

#print('введите расход топлива на 100 км и объём имеющегося топлива')
#consumption = int(input())
#amount = int(input())
#print(calculate_available_distance(consumption, amount))