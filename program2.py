#enter a number and check the number is prime or not
def checkprime(n):
    if(n<=1):
        return False
    for i in range(2,n):
        if(n%i==0):
            return False
    return True

a=int(input("Enter a number:"))
if(checkprime(a)):
    print("Number is prime!!")
else:
    print("Number is not prime!!")