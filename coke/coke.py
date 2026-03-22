amount = 50

while amount > 0:
    print(f"Amount due: {amount}")
    coin = int(input("insert coin:"))
    if coin in [25, 10, 5]:
        amount -= coin

print(f"Change Owed: {-amount}")