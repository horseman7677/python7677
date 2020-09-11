x = int(input('Enter the Number : '))
s=x
t=0
length = (len(str(x)))

while(x>0):
    remen = x%10
    t=t+(pow(remen,length))
    x=int(x/10)

print(t)

if t==s:
    print('Is Armstrong ',t)
else:
    print('Not Armstrong')


