from lib.outPutPrint import outPutPrint

# First solution - not all case passing
# def validStartingCity(distances, fuel, mpg):
#     # Write your code here.
#     fuel_index = fuel.index(max(fuel))
#     return fuel_index

# Passed all cases but Time: O(n) || Space: O(n)
# def validStartingCity(distances, fuel, mpg):
#     # Write your code here.
#     fuel_remains = []
#     remaining_fuel = 0
#     for i in range(len(fuel)):
#         fuel_remains.append(remaining_fuel)
#         remaining_fuel += (fuel[i] * mpg) - distances[i]
#     return fuel_remains.index(min(fuel_remains))

# Passed all cases Time: O(n) || Space: O(1)
def validStartingCity(distances, fuel, mpg):
    no_of_cities = len(distances)
    miles_remaining = 0

    index_of_starting_city = 0
    miles_remaining_at_staring_city = 0

    for i in range(1, no_of_cities):
        distance_from_prev_city = distances[i - 1]
        fuel_from_prev_city = fuel[i - 1]
        miles_remaining += fuel_from_prev_city * mpg - distance_from_prev_city

        if miles_remaining < miles_remaining_at_staring_city:
            miles_remaining_at_staring_city = miles_remaining
            index_of_starting_city = i

    return index_of_starting_city



# data = dict(
#     distances=[5, 25, 15, 10, 15],
#     fuel=[1, 2, 1, 0, 3],
#     mpg=10
# )

data = dict(
    distances=[1, 3, 10, 6, 7, 7, 2, 4],
    fuel=[1, 1, 1, 1, 1, 1, 1, 1],
    mpg=5
)
'''
mpg = 10

i = 4
fuel = 3
cover distance = 30
remaining fuel = 30 - 15 = 15

i = 0
fuel = 1
cover distance = 10 + 15 = 25
remaining fuel = 25 - 5 = 20

i = 1
fuel = 2
cover distance = 20 + 20 = 40
remaining fuel = 40 - 25 = 15


i = 2
fuel = 1
cover distance = 10 + 15 = 25
remaining fuel = 25 - 15 = 10

i = 3
fuel = 0
cover distance = 0 + 10 = 10
remaining fuel = 10 - 10 = 0

'''
output = validStartingCity(data["distances"], data["fuel"], data["mpg"])

outPutPrint(data, output)
