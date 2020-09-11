p = int(input('Enter the Princepal amount : '))
r = float(input('Enter the Rate : '))
t = int(input('Enter the Time : '))

a = float(p*(pow((1+(r/100)),t)))

ci = float(a-p)

print('Compound interest : ',(ci))