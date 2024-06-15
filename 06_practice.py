#               *
#               **
#               ***
#               ****
#               *****
#               ****
#               ***
#               **
#               *

num=int(input("Enter number: "))

for i in range(0,num):
    for j in range(i+1):
        print('*',end='')
    print()
for i in range(1,num):
    for j in range(num-i):
        print('*',end='')
    print()

