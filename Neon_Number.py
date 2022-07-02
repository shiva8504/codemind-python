sh=int(input())
SH=sh*sh
Sh=0
while SH:
    Sh+=SH%10
    SH=SH//10
if sh==Sh:
    print('Neon Number')
else:
    print('Not Neon Number')