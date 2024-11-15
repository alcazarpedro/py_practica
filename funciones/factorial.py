
def factorial(x):
    if x ==0:
        return 1
    else :
        factor = 1
        for i in range(1,x+1):
            factor*=i
        return factor    
    
x=int(input('digita el numero >_ '))

output = factorial(x)
print(f'factorial de {x} = {output}')



