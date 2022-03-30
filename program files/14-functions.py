import os
"""
read directory
make directory

"""
path = 'watchlists/'
default = "AAPL NFLX FB GOOG AMZN".split()
with open(path + 'default.list', 'w') as file:
    for symbol in default:
        file.write(symbol + " ")
file.close()

def read_directory():
    if not os.path.exists('watchlists/'):
        print("No saved watchlists")
        os.mkdir('watchlists')
    else:
        files = os.listdir('watchlists')
        if not files:
            print("No saved watchlists")
        for number, file in enumerate(files, 1):
            print(f"{number} - {file[:-5]}")
        return files

def choose_list():
    watchlists = read_directory()
    choice = int(input("Enter watchlist number: "))
    watchlist_file = watchlists[choice - 1]
    watchlist = open(f'watchlists/{watchlist_file}', 'r').read().split()
    return watchlist



print(choose_list())