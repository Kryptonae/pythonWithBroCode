# fruits = ["apple", "banana", "orange", "coconut"]
# vegetables = ["celery", "carrots", "potatoes"]
# meats = ["chicken", "fish", "turkey"]

# groceries = [fruits, vegetables, meats]

# groceries = [["apple", "banana", "orange", "coconut"], 
# ["celery", "carrots", "potatoes"], 
# ["chicken", "fish", "turkey"]]

# groceries = [("apple", "banana", "orange"), 
# ("celery", "carrots", "potatoes"), 
# ("chicken", "fish", "turkey")]

# print(groceries[2][0])

""" for collection in groceries:
    for food in collection:
        print(food, end=" ")
    print() """
    
num_pad = (
(1, 2, 3), 
(4, 5, 6), 
(7, 8, 9), 
("*", 0, "#")
)

for collection in num_pad:
    for num in collection:
        print(num, end=" ")
    print()