for number in range(0, 101):
    if number % 3 == 0 and number % 5 == 0:
        #divisible by 3 and 5
        print("FizzBuzz: %d" % number)

    elif number % 5 == 0:
        #divisible by 5
        print("Fizz: %d" % number)
    elif number % 3 == 0:
        #divisible by 3 and 5
        print("Buzz: %d" % number)
    else:
        print(number)
