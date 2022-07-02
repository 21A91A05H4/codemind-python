n=int(input())
alph="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
for i in range(n):
    for j in range(n-i-1):
        print(' ',end='')
    for j in range(i+1):
        print(alph[j],end='')
    for j in range(i,0,-1):
        print(alph[j-1],end='')
    print()