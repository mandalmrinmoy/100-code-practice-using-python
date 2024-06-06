low=10
high=1000

for i in range(low,high+1):
    length=len(str(i))
    temp=i
    sum=0

    while temp>0:
        digit=temp % 10
        sum+=digit**length
        temp=temp//10
    
    if i==sum:
        print(i,end='\n')