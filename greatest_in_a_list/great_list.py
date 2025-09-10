list = [10,20,30,5,2,5,1,7,50]

high_num = list[0]

for i in range(len(list)):
    if list[i] > high_num:
        high_num = list[i]

print(high_num)