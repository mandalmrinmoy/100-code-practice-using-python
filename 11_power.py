# num=int(input("enter number: "))
# power=int(input("enter power: "))
# print(num**power)
def power(a,b):
    if b!=0:
        return a**b
    else:
        return 1
    
print(power(2,3))

def pow(a,b):
    if b==0:
        return 1
    else:
        return a*pow(a,b-1)
    
print(pow(2,4))