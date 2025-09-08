cars = ['bmw', 'audi', 'toyota', 'subaru']
# sort the list in alphabetical order permanently
cars.sort()
# ['audi', 'bmw', 'subaru', 'toyota']
print(cars)

cars = ['bmw', 'audi', 'toyota', 'subaru']
# sort the list in reverse alphabetical order permanently
cars.sort(reverse=True)
# ['toyota', 'subaru', 'bmw', 'audi']
print(cars)

cars = ['bmw', 'audi', 'toyota', 'subaru']
# ['audi', 'bmw', 'subaru', 'toyota']
print(sorted(cars)) # sort the list in alphabetical order temporarily
# ['bmw', 'audi', 'toyota', 'subaru']
print(cars)

cars = ['bmw', 'audi', 'toyota', 'subaru']
# reverse() doesn’t sort backward alphabetically; it simply reverses the order of the list
cars.reverse()
# ['subaru', 'toyota', 'audi', 'bmw']
print(cars)

# find the length of a list, 4
print(len(cars))