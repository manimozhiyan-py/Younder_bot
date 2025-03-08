list_1 = [1,3,5,7,8]
list_2 = [3,4,6,7,10]

intersect = []

for element in list_1:
    for element2 in list_2:
        if element == element2:
            intersect.append(element)
            break

print(intersect)