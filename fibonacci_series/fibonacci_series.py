print("Welcome to the Generator of Fibonacci Series!")
 
n = int(input("Enter the number of terms: "))

fib_list=[0,1]

for i in range(2,n):
    sum = fib_list[i-1]+fib_list[i-2]
    fib_list.append(sum)

print(fib_list)



