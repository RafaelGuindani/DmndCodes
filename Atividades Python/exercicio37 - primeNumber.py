a = int(input('Insert a NUMBER: '))

def primeNumber(number):

    isPrime = True
    for i in range(2, number):
        if number % i == 0:
            isPrime = False

    if isPrime:
        print(f'{number} - It is a prime NUMBER.')
    else:
        print(f'{number} - It is not a prime NUMBER.')


primeNumber(number=a)