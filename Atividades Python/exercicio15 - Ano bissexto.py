while True:
    
    try:

        year = int(input("\nWhich year do you want to check?\n >:"))
        if year % 4 == 0:
            if year % 100 == 0:
                if year % 400 == 0:
                    print("\nLeap year")
                else:
                    print("\nNot leap year")
            else:
                print("\nLeap year")        
        else:
            print("\nNot a leap year")
    
    except ValueError:
        print("\nEnter a valid year\nExample: 2022\n")
