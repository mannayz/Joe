from collections import Counter
from os import listdir

words_to_drop = ['the', 'to', 'you', 'I', 'a', 'and', 'of', 'that', 'it', 'is']
files = listdir('scripts/')

for name in files:

    with open('scripts/' + name) as file:

        print(name)

        words = file.read()

        split_it = words.split()

        print(len(split_it))

        for i in words_to_drop:
            split_it[:] = [x for x in split_it if x != i]

        print(len(split_it))

        counter = Counter(split_it)
        most_occur = counter.most_common()
        print(most_occur)


