a = int(input("Enter a year: "))

# Leap year should be fully divisible by 4 or divisble by 100 and divisible by 400

if(a % 4 == 0):
    if(a % 100 == 0):
        if(a % 400 == 0):
            print(f"{a} is a leap year")
        else:
            print(f"{a} is not a leap year")
    else:
        print(f"{a} is a leap year")
        
else:
    print(f"{a} is not a leap year")