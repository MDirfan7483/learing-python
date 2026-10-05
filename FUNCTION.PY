def factroil(n):
    if n==1 or n==0:
        return 1
    return n*factroil(n-1) 



n = int(input("Enter the number:"))

print(f"The factorial of number is : {factroil(n)} ")