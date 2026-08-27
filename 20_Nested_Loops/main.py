""" for i in range(3):
    for j in range(1, 11):
        print(j, end=" ")
    print() """
    
row = int(input("Enter the # of rows: "))
columns = int(input("Enter the # of columns: "))
symbol = input("Enter a symbol to use: ");

for x in range(row):
    for y in range(columns):
        print(f"{symbol}", end= " ")
    print()