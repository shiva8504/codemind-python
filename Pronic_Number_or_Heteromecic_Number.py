n=int(input())
a=0
for i in range(1,(n//2)+1,1):
    if i*(i+1)==n:
        a+=1
if a!=0:
    print('YES')
else:
    print('NO')