#program to print factorial of any number

n=int(input('enter a number'))

f=1
i=1
while(n>i):
    f=f*n
    n=n-1

print('factorial',f)
