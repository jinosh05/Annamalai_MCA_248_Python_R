num = input("Enter number to check for Armstrong:")
result = 0
temp = int(num)
while(temp > 0):
    remainder = int(temp % 10)
    temp = temp/10
    result = result+(remainder*remainder*remainder)
if(int(result) == int(num)):
    print("Given number " + num + " is an Armstrong number.")
else:
    print("Given number " + num + " is not an Armstrong number.")
