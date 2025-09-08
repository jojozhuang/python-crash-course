bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)

# trek
print(bicycles[0])

# cannondale
print(bicycles[1])

# redline
print(bicycles[2])

# specialized
print(bicycles[3])

# specialized, -1 refers to the last item in the list
print(bicycles[-1])

# redline, -2 refers to the second last item in the list
print(bicycles[-2])

# cannondale, -3 refers to the third last item in the list
print(bicycles[-3])

# trek, -4 refers to the fourth last item in the list
print(bicycles[-4])

# Trek
print(bicycles[0].title())

# Specialized
print(bicycles[3].title())

message = f"My first bicycle was a {bicycles[0].title()}."

# My first bicycle was a Trek.
print(message)