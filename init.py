hello ="HELLO WORLD!"

print(hello.lower())
print(hello.upper())
print(hello.title())
print(hello.lower().count('l'))
print(hello.find('L'))

indexes = []
for index,value in enumerate(hello):
    if value == 'L':
        indexes.append(index)
        print(value,"is at index",index)

print(indexes)    