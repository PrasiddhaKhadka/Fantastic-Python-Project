import random as r

def mutatae(a_list:list):
    b_list = []
    new_item = 0
    for items in a_list:
        new_item += items * 2
        new_item += r.randint(1,5)
        print(new_item)
        new_item += items   
        b_list.append(new_item)
    print(b_list)


mutatae(a_list=[1,2,3,4,5])