import random as r

friend = ['Ram','Shyam','Hari','Gita','Sita',]

# 1st Method
random_friend = r.choice(friend)
print(random_friend)

# 2nd Method
random_friend = r.randint(0,4)
print(friend[random_friend])