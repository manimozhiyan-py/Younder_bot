string = 'hheello is '
dic={}
unique = ""

for char in string:
    if char != " ":
        if char not in dic.keys():
            dic[char] = 1
        else:
            dic[char] += 1

for char in string:
    if dic[char] == 1:
        unique = char
        break

print(f" string : {string}")
print(f" First Non-repeating character : {unique}" )