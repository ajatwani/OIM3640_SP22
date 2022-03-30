from random import randint

print("Welcome to the dice simulator")
iterations = int(input("Enter number of rolls: "))

twos = 0
threes = 0
fours = 0
fives = 0 
six = 0
sevens = 0
eights = 0
nines = 0
tens = 0
elevens = 0
twelves = 0


for iteration in range(iterations):
    roll = randint(1,6) + randint(1,6)

    if roll == 2:
        twos += 1
    elif roll == 3:
        threes += 1
    elif roll == 4:
        fours += 1
    elif roll == 5:
        fives += 1
    elif roll == 6:
        six += 1
    elif roll == 7:
        sevens += 1
    elif roll == 8:
        eights += 1
    elif roll == 9:
        nines += 1
    elif roll == 10:
        tens += 1
    elif roll == 11:
        elevens += 1
    elif roll == 12:
        twelves += 1
    else:
        print("I wasn't expecting that") 

print("-" * 30)
print(f"2:    {twos * '|'}")
print(f"3:    {threes * '|'}")
print(f"4:    {fours * '|'}")
print(f"5:    {fives * '|'}")
print(f"6:    {six * '|'}")
print(f"7:    {sevens * '|'}")
print(f"8:    {eights * '|'}")
print(f"9:    {nines* '|'}")
print(f"10:   {tens * '|'} ")
print(f"11:   {elevens * '|'}")
print(f"12:   {twelves * '|'}")                                   
print("-" * 30)















