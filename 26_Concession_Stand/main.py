menu = {
    "hotdog": 2.50,
    "hamburger": 3.00,
    "cheeseburger": 3.50,
    "fries": 1.50,
    "soda": 1.00,
    "water": 0.75,
    "pizza": 4.00,
    "taco": 2.00,
}

cart = [];
total = 0;

print("--------- Welcome to the Concession Stand! --------")

for key, value in menu.items():
    print(f"{key:43} : ${value:.2f}")
    
print("---------------------------------------------------")

while True:
    food = input("Select an item ('q' to quit): ").lower()
    if food == 'q':
        break
    elif menu.get(food) is not None:
        cart.append(food)
        
for food in cart:
    total += menu.get(food)
    print(food, end=" ")
        
print()
print(f"Total: ${total:.2f}")