def add(*args):
    total = 0
    for arg in args:
        total += arg
    return total

# print(add(1, 2, 3, 4, 5))  # Output: 15

def displayName(*names):
    for name in names:
        print(f"Hello, {name}!")
        
# displayName("Alice", "Bob", "Charlie")

def printAddress(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")
        
# printAddress(street="123 Main St", 
#             city="Anytown", 
#             state="CA", 
#             zip="12345")

def shippingLabel(*args, **kwargs):
    for arg in args:
        print(arg, end=" ")
    print()
    for value  in kwargs.values():
        print(f"{value}", end=" ")
    print()

shippingLabel("Mr.",
              "Ashwani",
              "Kumar",
              street="123 Main St",
              city="Anytown",
              state="CA",
              zip="12345")

shippingLabel("Mr.",
              "Abhinav",
              "Kumar",
              street="123 Main St",
              city="Fartown",
              state="DC",
              zip="67890")