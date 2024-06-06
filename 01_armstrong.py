# 370 ---> lenght =3 so, 3**3+7**3+0**3=370 it is a armstrong number
num=370
temp=num
length=len(str(num))
digit,sum=0,0
for i in range(length):
    digit=int(temp%10)
    temp=temp/10
    sum+=pow(digit,length)
    # print(sum)

if num==sum:
    print("Armstrong number")
else:
    print("normal number")

while temp>0:
    digit=int(temp%10)
    temp=temp//10
    sum+=digit**length
    # print(sum)

if num==sum:
    print("Armstrong number")
else:
    print("normal number")

