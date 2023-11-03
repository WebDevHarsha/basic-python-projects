
import numpy
n=int(input("enter an odd number"))

def magic_square(n):
    l=[[0]*n]*n
    i=int(n/2)
    j=n-1
    l=numpy.array(l)
    l[i][j]=1
    numb=2
    visited=set({})
    while True:
        visited.add((i,j))    
        
        i-=1
        j+=1
        if (i,j) in visited:
            i+=1
            j-=2
        elif i==-1 and j==n:
            i=0
            j=n-2
        elif i==-1:
            i=n-1
        elif j==n:
            j=0 
        l[i][j]=numb
        
        numb+=1
        if numb==n**2+1:
            break
    return l

print(magic_square(n))