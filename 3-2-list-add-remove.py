motorcycles = ['honda', 'yamaha', 'suzuki']
# ['honda', 'yamaha', 'suzuki']
print(motorcycles)

# Changing the first item in the list
motorcycles[0] = 'ducati'
# ['ducati', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles = ['honda', 'yamaha', 'suzuki']
# Appending an item to the end of the list
motorcycles.append('ducati')
# ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)

motorcycles = ['honda', 'yamaha', 'suzuki']
# Inserting an item to the head of the list
motorcycles.insert(0, 'ducati')
# ['ducati', 'honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles = ['honda', 'yamaha', 'suzuki']
# Removing an item at position 0
del motorcycles[0]
# ['yamaha', 'suzuki']
print(motorcycles)

motorcycles = ['honda', 'yamaha', 'suzuki']
# Removing the last item in a list using the pop() method
popped_motorcycle = motorcycles.pop()
# ['honda', 'yamaha']
print(motorcycles)
# suzuki
print(popped_motorcycle)

motorcycles = ['honda', 'yamaha', 'suzuki']
# Removing the first item in a list using the pop() method
first_owned = motorcycles.pop(0)
# ['yamaha', 'suzuki']
print(motorcycles)
# honda
print(first_owned)

motorcycles = ['honda', 'yamaha', 'suzuki']
# Removing an item by value
motorcycles.remove('yamaha')
# ['honda', 'suzuki']
print(motorcycles)