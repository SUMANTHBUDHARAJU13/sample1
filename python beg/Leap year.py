Year=int(input("Enter the year: "))
if(Year % 4) == 0:
    if(Year % 100) == 0:
        if(Year % 400) == 0:
            print("Leap year.")
        else:
            print( "not a leap year.")
    else:
        print("leap year.")
else:
    print("not a leap year.")