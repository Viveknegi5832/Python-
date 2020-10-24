'''
Ques.3 Write a Python function to find the nth term of Fibonacci sequence and its factorial.  

'''



def factorial(n):
    if n <= 1:
        return 1
    return n*factorial(n-1)

def func(n):
    if n <= 0:
        return 0
    if n == 1:
        return 1
    return func(n-1) + func(n-2)
 
def main():

    n = int(input("Enter the number : "))
    
    print("nth term : " , func(n))
    print("Factorial : " , factorial(n))
    

main()
