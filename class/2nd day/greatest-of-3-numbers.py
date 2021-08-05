input1 = int(input("Enter a number: "))
input2 = int(input("Enter a number: "))
input3 = int(input("Enter a number: "))

if(input1 >= input2 and input1 >= input3):
    greatest = input1
elif(input2 >= input1 and input2 >= input3):
    greatest = input2
else:
    greatest = input3
    
print("Greatest number of 3 inputs is ", greatest)