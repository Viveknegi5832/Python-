'''
Ques.5 Write a function that finds the sum of the n terms of the following series. 
Import the factorial function created in question 3. 

1–x2/2! + x4/4! – x6/6! + …xn/n!

'''



from Practicals3 import factorial

# Function to find sum of given series
def sum_series(x, n):
    sum = 0
    for i in range(1, n+1, 1):
        term = ((-1)**(i+1))*(x**(2*i-2)/factorial(2*i-2)) #Calculating nth term
        sum += term
    return sum

def main():
    n = int(input("Enter value of n: "))
    x = int(input("Enter value of x: "))
    sum = sum_series(x, n)
    print("Sum of " , str(n), "terms for x=" , str(x) , "is : " ,  sum)
main()
