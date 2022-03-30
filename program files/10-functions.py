# user defined functions

# make a watch list
def watchlist():
    watch = []
    while True:
        symbol = input("Enter symbol symbol: ").upper()
        if symbol == "":
            break
        watch.append(symbol)
    watch.sort()
    watch = list(set(watch))
    return watch

# print(watchlist())

# clean a string

string = "They're selling postcards of a hanging;.  " \
         "They're painting? the passports brown!"
def clean_string(string):
    punctuation = '.,?!";:*'
    for mark in punctuation:
        string = string.replace(mark, "")
    return string
#print(clean_string(string))


# vowel replacer

def replace_vowel(string):
    replacements = {'a': 4, 'e': 3, 'i': 1, 'o': 0, 'u': 8}
    revised = ''
    for letter in string:
        if letter in 'aeiou':
            revised += str(replacements[letter])
        else:
            revised += letter
    return revised

# print(replace_vowel("Desolation"))

# is anagram #1
def is_anagram(str1, str2):
    s1 = sorted(str1.lower())
    s2 = sorted(str2.lower())
    if s1 == s2:
        return True
    else:
        return False

def is_anagram(str1, str2):
    str1 = [letter.lower() for letter in str1 if letter != " "]
    str2 = [letter.lower() for letter in str2 if letter != " "]
    str1.sort()
    str2.sort()
    if str1 == str2:
        return True
    else:
        return False


print(is_anagram('Debit card', "Bad Credit"))



















