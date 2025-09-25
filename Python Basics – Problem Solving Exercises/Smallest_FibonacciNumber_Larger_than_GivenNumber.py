"""
Find the smallest number m from the Fibonacci sequence, defined by f[0]=f[1]=1, f[n]=f[n-1] + f[n-2],
for n > 2, larger than the given natural number n. (e.g. for n = 6, m = 8).
"""
# 1 1 2 3 5 8 13 21 34.....

def Fibonacci(number):
    fibonacci1, fibonacci2, auxiliar = 1, 1, 0
    while number >= fibonacci2:
        auxiliar = fibonacci1
        fibonacci1 = fibonacci2
        fibonacci2 = fibonacci2 + auxiliar
    return fibonacci2

def main():
    print("Give the number: ")
    number = int(input())
    if(number < 3):
        print("The number must be greater than 2!")
        return
    print("The smallest number from Fibonacci sequence greater than {number} is: ", Fibonacci(number))

main()
