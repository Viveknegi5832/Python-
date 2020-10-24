'''
Ques.4 Write a function that takes a number (>=10) as an input and return the digits of the number as a set.

'''


def func(n):
    _set = set() #Creating an empty set
    if n >= 10 :
        
       while n != 0:
            _set.add(n%10)
            n = int(n/10)
    return _set
       
def main():
    n = int(input("Enter a two or more digit number : "))
    print("Digits are : " ,  func(n))
   
main()
   