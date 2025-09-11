# A tuple is a collection which is ordered and unchangeable. In Python tuples are written with round brackets.
# Tuples are used to group together related data.
dimensions = (200, 50)
# 200
print(dimensions[0])
# 50
print(dimensions[1])

# dimensions[0] = 180 # This will raise an error because tuples are immutable

# dimensions is a tuple, but we can assign a new tuple to the same variable, no error
dimensions = (400, 100)
# 400
print(dimensions[0])
# 100
print(dimensions[1])

dimensions = (10, 20, 30, 40, 50)
for dimension in dimensions:
  print(dimension)

# Output:
# 10
# 20
# 30
# 40
# 50