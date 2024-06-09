# Check Whether a Number is a Prime or Not
num=17
for i in range(2,num):
    if num%i!=0:
        print('prime number')
        break
    else:
        print('not prime number')
        break