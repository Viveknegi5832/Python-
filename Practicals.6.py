'''
Ques.6 Consider a tuple t1 = {1,2,5,7,9,2,4,6,8,10}. Write a program to perform following operations: 
a) Print another tuple whose values are even numbers in the given tuple. 
b) Concatenate a tuple t2={11,13,15) with t1. 
c) Return maximum and minimum value from this tuple.

'''



t1 = (1,2,50,7,9,2,4,6,8,9)
t2 = (11,20,15)

print("1. Initial tuple one : ", t1)
print("2. Initial tuple two : ", t2)
tcon = t1 + t2
print()

print("3. After concatenation : ", tcon)
print()

print("4. Maximum value : ", max(tcon))
print("5. Minimum value : ", min(tcon))
print()

a = len(t1)
t3 = list(t1)
t4 = []
for i in range(a):
    if t3[i]%2==0 :
       t4.append(t3[i])
t1 = tuple(t4)
print()
print("6. Tuple with even no. of tuple 1 : ", t1)

        


    
    
