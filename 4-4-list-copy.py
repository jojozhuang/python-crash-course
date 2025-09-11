my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]
# ['pizza', 'falafel', 'carrot cake']
print(my_foods)
# ['pizza', 'falafel', 'carrot cake']
print(friend_foods)


my_foods.append('cannoli')
# ['pizza', 'falafel', 'carrot cake', 'cannoli']
print(my_foods)

friend_foods.append('ice cream')
# ['pizza', 'falafel', 'carrot cake', 'ice cream']
print(friend_foods)

# my_foods and friend_foods are different lists