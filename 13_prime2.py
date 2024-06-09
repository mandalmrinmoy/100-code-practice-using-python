# Find the Prime Numbers in a Given Interval in Python
start=9
end=20
for i in range(start,end+1):
    flag=0
    for j in range(2,i):
        if (i%j ==0):
            flag=1
    if flag==0:
        print(i,end=' ')
