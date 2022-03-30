from operator import itemgetter
import os


#print(os.getcwd())
file = open('desolation_row.txt', 'r')
 
data = file.read()
file.close()

# clean data of punctuation marks (tokenize)
punctuation = '.,;:!?"'

for mark in punctuation:
    data = data.replace(mark, '')

data = data.upper().split()
#print(data)

word_counts = dict()

for word in data:
    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1

#print(word_counts.items())
sorted_counts = sorted(word_counts.items(), key= itemgetter(1), reverse = True)
print(sorted_counts)
print(len(data)) # number of total words
print(len(word_counts)) # number of unique words
print(f"Proportion unique words: {len(word_counts) / len(data)}")

print(" Word frequencies ".center(35, "="))
for word in sorted_counts[:10]:
    print(f"{word[0]:15}{word[1]}")









