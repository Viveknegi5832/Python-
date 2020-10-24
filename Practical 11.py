'''
11. Write a menu-driven program to accept a list of student names and perform
    the following
 a. search an element using linear search / binarysearch.
 b. Sort the elements using bubble sort / insertion sort / selection sort
'''

def linearsearch(l,s):
    flag = 1
    print("Entered list is : ",l)
    a = input("Enter the Name to search : ")
    for i in range(s):
        if a == l[i]:
            flag = 0 
            break
    if flag == 0:
        print(f"Element found at {i+1} ")
    else:
        print("Element Not Found ")

def binarysearchl(l,s):
    a = input("Enter the element to search : ")
    bubblesort(l,s)
    low  = 0
    high = s - 1
    flag = 0
    while low <= high:
        mid = (high + low)//2
        if l[mid] == a:
            flag = 1
            break
        elif len(a) < len(l[mid]):
            high = mid - 1
        else:
            low = mid + 1
    if flag == 1:
        print(f"\nElement found at {mid+1} position")
    else:
        print("\nElement Not Found ")

def bubblesort(l,s):
    print("\nEntered list is : " , l)
    for j in range(s):
        for i in range(s-j-1):
            if len(l[i])  > len(l[i+1]):
                temp = l[i]
                l[i] = l[i+1]
                l[i+1] = temp

    print("\nSorted list is : " , l)

def insertionsort(l,s):
    print("\nEntered list is : " , l)
    for i in range(1,s):
        k = l[i]
        j = i-1
        while j >= 0 and len(k) < len(l[j]): #Not working when not using length for strings
            l[j+1] = l[j]
            j-=1
        l[j+1] = k
    print("\nSorted list is : " , l)

def selectionsort(l,s):
    print("Entered list is : " , l)
    for i in range(s):
        min_indx = i
        for j in range(i+1,s):
            if len(l[min_indx]) > len(l[j]):
                min_indx = j
        l[i], l[min_indx] = l[min_indx], l[i]
        ''' temp = l[i]
        l[i] = l[min_indx]
        l[min_indx] = temp
        '''
    print("\nSorted list is : " , l)

def main():
    ch = 'y'
    l = []
    s = int(input("Enter the size of list : "))
    for i in range(1,s+1):
        a = input(f"Enter Name of student  {i} : ")
        l.append(a)
    while ch == 'y' or ch == 'Y':
        print("-"*20)
        print("1. Linear Search ")
        print("2. Binary search ")
        print("3. Sort a list using Bubble sort ")
        print("4. Sort a list using insertion sort ")
        print("5. sort a list using selection sort ")
        print("-"*20)
        print()
        choice = int(input("Enter your choice : "))

        if choice == 1:
            linearsearch(l,s)
        elif choice == 2:
            binarysearchl(l,s)
        elif choice == 3:
            bubblesort(l,s)
        elif choice == 4:
            insertionsort(l,s)
        elif choice == 5:
            selectionsort(l,s)
        else:
            print("\nInvalid choice ")
        ch = input("\nWant to continue (y/n) : ")

main()

