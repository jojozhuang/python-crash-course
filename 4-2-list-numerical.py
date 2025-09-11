for value in range(1, 5):
  print(value)

# Output:
# 1
# 2
# 3
# 4

# off-by-one behavior, 5 is not included

# Using range() to Make a List of Numbers
numbers = list(range(1, 6))
# [1, 2, 3, 4, 5]
print(numbers)

even_numbers = list(range(2, 11, 2))
# [2, 4, 6, 8, 10]
print(even_numbers)

squares = []
for value in range(1, 11):
  squares.append(value ** 2)
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
print(squares)

# List Comprehensions
squares = [value**2 for value in range(1, 11)]
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
print(squares)

tens = [value*10 for value in range(1, 11)]
# [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
print(tens)

digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
# 0
print(min(digits))
# 9
print(max(digits))
# 45
print(sum(digits))

