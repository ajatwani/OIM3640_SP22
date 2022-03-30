# piglatin

text =       """Darkness at the break of noon 
          Shadows even the silver spoon 
          The handmade blade, the child's balloon 
          Eclipses both the sun and moon"""

text_list = text.lower().replace(',', '').replace("'", "").split()
pig_latin = []

for word in text_list:
    word = word[1:] + word[0] + "ay"
    pig_latin.append(word)

print(" ".join(pig_latin))

# calculate average word length

word_count = len(text_list)
total_letters = 0

for word in text_list:
    total_letters += len(word)
    
average_word = total_letters / word_count
print(f"Average word length: {average_word:.2f}")

# find longest word
longest_word = ''

for word in text_list:
    if len(word) > len(longest_word):
        longest_word = word

print(longest_word)













