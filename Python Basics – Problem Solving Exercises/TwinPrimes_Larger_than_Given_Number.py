"""
Determine the twin prime numbers p1 and p2 immediately larger than the given non-null natural number n. Two prime numbers p and q are called twin if q - p = 2.
"""
def prim(a):
    if a==2:
      return 1
    for i in range(2,a//2+1):
        if a%i==0:
               return 0
    return 1
print("choose the number: ")
n=input()
n=int(n)
if n<=0:
    print("this is not a valid number")
else:
    p2=n+1
    p1=p2+2
    while (prim(p2)==0 or prim(p1)==0):
        p2 = p2 + 1
        p1 = p2 + 2
    print("The twin prime numbers are: ",p1," and ",p2)
