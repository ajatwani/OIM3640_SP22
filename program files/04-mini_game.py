"""mini game calculator"""
print("Welcome to the savings calculator!")
print("Tell me how much you will deposit and I will tell you what")
print("it's worth in five years")

initial_deposit = float(input("Enter initial deposit: "))
RATE = .015
print(f"{'Year':12} {'Balance'}")
print("-" * 20)

for year in range(1, 6):
    balance = f'$ {initial_deposit * (1 + RATE ) ** year:>4,.2f}'
    print(f" {year:<8} {balance}")