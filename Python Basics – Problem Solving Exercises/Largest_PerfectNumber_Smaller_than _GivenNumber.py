"""
Generate the largest perfect number smaller than a given natural number n.
If such a number does not exist, a message should be displayed. A number is perfect
 if it is equal to the sum of its divisors, except itself. (e.g. 6 is a perfect number,
  as 6=1+2+3).
"""
def perfect(a):
    perf=0
    for i in range(1, a//2+1):
        if a%i==0:
            perf=perf+i
    if a!=perf :
        return 0
    return 1
print("choose the number: ")
n=input()
n=int(n)
cont=0
print ("the largest perfect number is: ")
for i in range(n-1, 1, -1):
    if perfect(i)==1:
        cont=1
        break
if cont==0:
    print("such number does not exist")
else:
    print(i)
