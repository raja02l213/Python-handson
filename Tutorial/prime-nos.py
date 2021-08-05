a = int(input("Enter a no: "))
flag = False

if a > 1:
    for i in range(2, a+1):
        print(f"no is {i}")
        if((a % i) == 0):
            print(f"{a} is a prime no")
            flag = True
            break
            
if(flag):
    print(f"{a} is a prime no")
else:
    print(f"{a} is not a prime no")
    
            