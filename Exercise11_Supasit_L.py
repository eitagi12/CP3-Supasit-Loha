number = int(input())
for x in range(number):
    for y in range(number-x-1):
        print(end=" ")
    for y in range(x+1):
        print("*",end=" ")
    print()