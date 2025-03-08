from collections import Counter

element_list = ['apple','banana','banana','orange']

counter = Counter(element_list)

for i in counter:
    if counter[i] == max(counter.values()):
        print(i)