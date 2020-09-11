n = int(input('Enter Number : '))
f=n
if n==0 or n==1:
    print(n)

else:
    t=1
    while(n>1):
        t=t*(n)
        n -=1
    print('factorial of '+ str(f)+'! = '+str(t))    
