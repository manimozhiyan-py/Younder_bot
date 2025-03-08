int_list = [1,2,3,4,5,6,7,8,10]

def missing_num(int_list):
    for i in range(len(int_list)-1):
        if int_list[i+1] == int_list[i] +1:
            pass
        else:
            return int_list[


            ] +1

print(f"The Missing Number is : {
missing_num(int_list)}")

