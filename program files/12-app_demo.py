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
    pass

def add_list():
    pass

def delete_list():
    pass

# program flow
def main():
    while True:
        watchlist = "goog amzn aapl nvda".upper().split()
        display_menu()
        choice = input("Enter your choice: ")
        if choice == '1':
            track(watchlist)
        elif choice in '234':
            pass
        elif choice == '5':
            print("Thank you for using StockTracker")
            print("Goodbye!")
            sys.exit()

if __name__ == "__main__":
    main()