while True:

    x = int(input("\nEnter a number and we'll find out if it's even or odd : \n>: "))
    y = x%2

    if y == 0:
        print('\nEven')
    else:
        print('\nOdd')