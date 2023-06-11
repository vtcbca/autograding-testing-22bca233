#take a number in input and return it's all digits sum
def sumofdigit(n):
    n=str(n)
    sum=0
    for i in n:
        sum=sum+int(i)
    return sum

a=int(input("Enter a number:"))
print(f'Sum of all digit is {sumofdigit(a)}.')