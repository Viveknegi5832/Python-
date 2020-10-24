def func():
    str = input("Enter the Sentence : ")
    freq = {}
    l = []
    for i in str:
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1 
    print("\n\nThe frequency of each character is : " , freq)
func()

