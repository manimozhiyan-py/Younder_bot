dup_list  = ['apple','banana','banana','orange','banana','watermelon']
unique_list = []

for element in dup_list:
    if element in unique_list:
        pass
    else:
        unique_list.append(element)

print(unique_list)
