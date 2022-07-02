n=int(input())
s=0
h=1
while n:
    s+=n%10
    h*=n%10
    n=n//10
if s==h:
    print('Spy Number')
else:
    print('Not Spy Number')