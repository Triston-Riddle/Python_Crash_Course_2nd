# define my_foods with a list of foods
# copy my_foods to another list using slices

my_foods = ["pizza ", "falafel ", "carrot cake "]
friend_foods = my_foods[:]

my_foods.append("jello")
friend_foods.append("pudding")

# print to console

for my_loop in my_foods:
    print(my_loop)

for friend_loop in friend_foods:
    print(friend_loop)