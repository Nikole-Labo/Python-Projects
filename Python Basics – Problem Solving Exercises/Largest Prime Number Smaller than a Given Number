""""
Generate the largest prime number smaller than a given natural number n. If such a number does not exist, a message should be displayed.
"""
def prim(a):
    if a<3:
        return 0
    for i in range(2,a//2+1):
        if a%i==0:
               return 0
    return 1

print("choose the number: ")
n=input()
n=int(n)
if n<3:
    print("this type of number does not exist")
if n==3:
   print(n-1)
else:
    for i in range(n-1, 2, -1):
        if prim(i):
            print(i)
            break
