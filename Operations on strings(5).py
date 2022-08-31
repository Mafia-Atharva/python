#Function to check lengths of string
def length(main):
    cnt=0
    for i in main:
        cnt=cnt+1
    return cnt

#Main program to get strings from user
n=int(input("Enter number of strings:"))
main=[]
word=""
for i in range(n):
    word=input("Enter string "+str(i+1)+":")
    main.append(word)

#To create a list of length of strings
submain=[]
for i in range(n):
    x=length(main[i])
    submain.append(x)

#To calculate the index of the largest string
max=submain[0]
i=0
index=i
for i in range(n):
    if(submain[i]>max):
        max=submain[i]
        index=i
print("The longest word among the given strings is",main[index])

#To determine the frequency of occurrence of particular character in the string
print(main)
x=int(input("Enter the number of string to check frequency of occurence:"))
char=input("Enter the alphabet to check:")
freq=0
for i in main[x-1]:
    if(char==i):
        freq+=1
if(freq==0):
    print("The given alphabet appears 0 times")
else:
    print("The given alphabet appears",freq,"times")

#To check whether given string is palindrome or not 
print(main)
x=int(input("Enter the number of string to check for palindrome:"))
str1=main[x-1]
str2=str1[::-1]
if(str1==str2):
    print(str1,"is a palindrome")
else:
    print(str1,"is not a palindrome")

#To display index of first appearance of the substring
print(main)
index=0
x=int(input("Enter the number of string to check for first occurence:"))
substring=input("Enter substring:")
for i in main[x-1]:
    index+=1
    if(i==substring):
        print(substring,"first found at position",index)
        break;