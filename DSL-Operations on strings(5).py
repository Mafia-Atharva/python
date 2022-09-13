'''Write a Python program to compute following operations on String:
a) To display word with the longest length
b) To determines the frequency of occurrence of particular character in the string
c) To check whether given string is palindrome or not
d) To display index of first appearance of the substring
e) To count the occurrences of each word in a given string
'''

#Function to check longest string
def longest():
    n=int(input("Enter number of strings:"))
    main=[]
    for i in range(n):
        word=input("Enter string "+str(i+1)+":")
        main.append(word)
    
    def len(main):
        cnt=0
        for i in main:
            cnt=cnt+1
        return cnt
    
    submain=[]
    for i in range(n):
        x=len(main[i])
        submain.append(x)
   
    max=submain[0]
    i=0
    index=i
    for i in range(n):
        if(submain[i]>max):
            max=submain[i]
            index=i
    print("The longest string is",main[index],"\n")

#Function to check longest string
def length():
    n=int(input("Enter number of strings:"))
    main=[]
    for i in range(n):
        word=input("Enter string "+str(i+1)+":")
        main.append(word)
    
    def len(main):
        cnt=0
        for i in main:
            cnt=cnt+1
        return cnt
    
    submain=[]
    for i in range(n):
        x=len(main[i])
        submain.append(x)
    
    max=submain[0]
    for i in range(n):
        if(submain[i]>max):
            max=submain[i]
    print("The length of longest string is",max,"\n")

#Function to frequency
def frequency():
    string=input("Enter string to check frequency of occurence:")
    char=input("Enter the alphabet to check:")
    freq=0
    for i in string:
        if(char==i):
            freq+=1
    if(freq==0):
        print("The given alphabet appears 0 times")
    else:
        print(char,"appears",freq,"times\n")

#Function to check palindrome
def palindrome():
    str1=input("Enter string to check for palindrome:")
    str2=str1[::-1]
    if(str1==str2):
        print(str1,"is a palindrome\n")
    else:
        print(str1,"is not a palindrome\n")

#Function to check first appearance
def first_appearance():
    index=0
    string=input("Enter string to check for first occurence:")
    substring=input("Enter substring:")
    for i in string:
        index+=1
        if(i==substring):
            print(substring,"first found at position",index,"\n")
            break;
        
while True:
    print("*******************Menu*******************")
    choice=int(input(("1.Display longest string\n2.Check the length of longest string\n3.Check frequency of occurence\n4.Check for palindrome\n5.Check for first appearance of substring\n6.Exit\nEnter your choice(1/2/3/4/5/6):")))
    if choice==1:
        longest()
    elif choice==2:
        length()
    elif choice==3:
        frequency()
    elif choice==4:
        palindrome()
    elif choice==5:
        first_appearance()
    elif choice==6:
        print("Thank you for using this program!")
        break
    else:
        print("Please enter a valid choice")
