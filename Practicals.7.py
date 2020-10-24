'''
Ques.7 Write a menu driven program to perform the following on strings :
a) Find the length of string. 
b) Return maximum of three strings.
c) Accept a string and replace all vowels with “#” 
d) Find number of words in the given string. 
e) Check whether the string is a palindrome or not.

'''

def len_str():
    str = input("Enter the string: ")
    print("Length of string: ", len(str))

def maximum():
    str1 = input("Enter string 1: ")
    str2 = input("Enter string 2: ")
    str3 = input("Enter string 3: ")

    if len(str1) > len(str2) and len(str1) > len(str3) :
       max = str1
    elif len(str2) > len(str1) and len(str2) > len(str3) :
       max = str2
    elif len(str3) > len(str1) and len(str3) > len(str2) :
       max = str3
    print("Maximum : " , max)


def replace_vowels():
    str = input("Enter the string: ")
    new_str = ""
    vowels = ['a','e','i','o','u']
    for i in range(0, len(str), 1):
        if str[i].lower() in vowels:
            new_str += "#"
        else:
            new_str += str[i]
    print("Replaced string: ", new_str)

def numofwords():
    str = input("Enter the string: ")
    str = str.strip() + " "
    count = 0
    for i in range(0, len(str), 1):
        if str[i] == " ":
            count += 1
    print("No of words: ", count)

def palindrome():
    str = input("Enter the string: ")
    new_str = str[::-1] #This will reverse the string
    if str == new_str:
        print(str," is palindrome ")
    else:
        print(str," is not palindrome")
    
def main():
  ch = 'y'
  while ch == 'y' or ch == 'Y':
    print("\nMenu")
    print("-"*30)
    print("1. Length of string")
    print("2. Maximum of three strings")
    print("3. Replace vowels with '#'")
    print("4. No. of words")
    print("5. Check Palindrome")
    print("6. Exit")
    print("-"*30)
    option = input("Your choice: ")

    switcher = {
        '1' : len_str,
        '2' : maxof_three,
        '3' : replace_vowels,
        '4' : numofwords,
        '5' : palindrome,
        '6' : quit
    }
    func = switcher.get(option, lambda: print("Invalid Choice!"))
    func()

    ch = input("\nWant to continue? (y/n) : ")
 
main()
       
        