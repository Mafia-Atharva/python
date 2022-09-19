'''
Write a pythonprogram to store first year percentage of students in array. Write function
for sorting array of floating point numbers in ascending order using
a) Selection Sort
b) Bubble sort and display top five scores.
'''

#Selection sort
def selection_sort(marks):
    for i in range(n-1):
        min_number=i
        for j in range(i+1,n):
            if marks[j]<marks[min_number]:
                min_number=j
        marks[i],marks[min_number]=marks[min_number],marks[i]
    print("Marks sorted using selection sort:")
    print(marks)

#Bubble sort
def bubble_sort(marks):
    for i in range(n-1):
        for j in range(0, n-i-1):
            if marks[j] > marks[j + 1]:
                marks[j], marks[j + 1] = marks[j + 1], marks[j]
    print("Marks sorted using bubble sort:",marks)
    reversed=marks[::-1]
    if len(marks)>=5:
        print("Top 5 scores:",reversed[0:5])
    print("Cannot display top 5 scores. Please enter more than 5 scores")
    
#Accepting elements from user
marks=[]
n=int(input("Enter number of students:"))
for i in range(n):
    percentage=int(input("Enter percentage of student "+str(i+1)+":"))
    marks.append(percentage)


#Menu and choice 
while True:
    print("************MENU************")
    print("1. Selection Sort\n2. Bubble sort")
    choice=int(input("Enter your choice(1/2):"))
    if choice==1:
        selection_sort(marks)
        break
    elif choice==2:
        bubble_sort(marks)
        break
    else:
        print("Please enter a valid choice")
