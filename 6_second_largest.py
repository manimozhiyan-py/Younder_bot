from django.forms.utils import pretty_name

int_list = [64,54,21,12,65,11]
first_largest = 0
second_largest = 0


for element in int_list:
    if element > first_largest:
        first_largest = element

for element in int_list:
    if element < first_largest:
        if element > second_largest:
            second_largest = element


print(second_largest)