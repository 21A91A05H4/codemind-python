n=int(input())
alph="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
while n>0:
    for i in range(n):
        print(alph[n-1],end=' ')
    n-=1
    print()