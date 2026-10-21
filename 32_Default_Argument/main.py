# net_price formula: net_price = price * (1 - discount) * (1 + tax)

def netPrice(price, discount=0, tax=0.05):
    return price * (1 - discount) * (1 + tax)

# print(f"Net price of item with price $500, discount 0% and tax 5% is: ${netPrice(500):.2f}")
# print(f"Net price of item with price $500, discount 10% and tax 5% is: ${netPrice(500, 0.1):.2f}")
# print(f"Net price of item with price $500, discount 10% and tax 0% is: ${netPrice(500, 0.1, 0):.2f}")

import time

def count(end, start=0):
    for x in range(start, end + 1):
        print(x)
        time.sleep(1)
    print("Done!")
    
count(10, 5)