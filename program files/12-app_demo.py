import pandas_datareader as pdr
import sys
from time import sleep, time

# program logic
def display_menu():
    print("""
    StockTracker Menu
    _________________
    1. Track Watchlist
    2. Edit Watchlist
    3. Add Watchlist
    4. Delete Watchlist
    5. Exit
    """)

def show_lists():
    pass

def track(watchlist):
    start_time = time()
    while True:
        print(pdr.get_quote_yahoo(watchlist)['price'])
        sleep(1)
        if time() - start_time >= 10:
            prompt = input("Would you like to continue?")
            start_time = time()
            if prompt.isalpha():
                break

def edit_list():
    print("Let's edit a list!")

def add_list():
    print("Let's add a list!")

def delete_list():
    print("Let's delete a list!")

# program flow
action = {'2':edit_list, '3': add_list, '4': delete_list}
def main():
    while True:
        watchlist = "goog amzn aapl nvda".upper().split()
        display_menu()
        choice = input("Enter your choice: ")
        if choice == '1':
            track(watchlist)
        elif choice in '234':
            action[choice]()
        elif choice == '5':
            print("Thank you for using StockTracker")
            print("Goodbye!")
            sys.exit()
        else:
            print("Enter a valid choice.")

if __name__ == "__main__":
    main()