import math
def prime(n):
    for i in range(2,round(math.sqrt(n))+1):
        if n%i==0:
            return 0
    return 1
n=int(input())
m=int(input())
c=0
for i in range(n,m+1):
    if prime(i)==1 and i!=1:
        c+=1
print(c)