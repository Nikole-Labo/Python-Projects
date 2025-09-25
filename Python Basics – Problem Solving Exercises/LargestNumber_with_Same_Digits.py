"""
For a given natural number n find the
largest natural number written with the same digits. (e.g. n=3658, m=8653).
"""

def findLargest(digitsList, numberDigits):
    finalNumber = 0
    largestDigit = 0
    digitByDigit = 1
    while numberDigits != 0:
        for element in digitsList:
            if element > largestDigit:
                largestDigit = element
        digitsList.remove(largestDigit)
        for index in range(1, numberDigits):
            digitByDigit *= 10
        finalNumber += largestDigit * digitByDigit
        numberDigits -= 1
        digitByDigit = 1
        largestDigit = 0


    return finalNumber
def main():
    print("number= ")
    number = int(input())
    numberDigits = 0
    digitsList = []
    while(number != 0):
        digitsList.append(number % 10)
        number //= 10
        numberDigits += 1
    print("\nThe largest number is: ", findLargest(digitsList, numberDigits))

if __name__ == '__main__':
    main()
