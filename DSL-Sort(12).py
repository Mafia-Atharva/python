#Ascending selection sort
def selection_sort_asc(numbers):
    for i in range(n-1):
        min_number=i
        for j in range(i+1,n):
            if numbers[j]<numbers[min_number]:
                min_number=j
        numbers[i],numbers[min_number]=numbers[min_number],numbers[i]
    print("Marks of students in ascending order:",numbers)
    top=input("\nDo you want to display top marks from the list (yes/no) : ")
    if top=='yes' or top=='y':
        top_five_marks_asc(numbers)
    else:
        print("\nThanks for using this program!")


#Descending selection sort
def selection_sort_desc(numbers):
    for i in range(n-1):
        min_number=i
        for j in range(i+1,n):
            if numbers[j]>numbers[min_number]:
                min_number=j
        numbers[i],numbers[min_number]=numbers[min_number],numbers[i]
    print("Marks of students in descending order:",numbers)
    top=input("\nDo you want to display top marks from the list (yes/no) : ")
    if top=='yes' or top=='y':
        top_five_marks_desc(numbers)
    else:
        print("\nThanks for using this program!")

#Ascending bubble sort
def bubble_sort_asc(numbers):
    for i in range(n-1):
        for j in range(0, n-i-1):
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
    print("Marks of students in ascending order:",numbers)
    top=input("\nDo you want to display top marks from the list (yes/no) : ")
    if top=='yes' or top=='y':
        top_five_marks_asc(numbers)
    else:
        print("\nThanks for using this program!")

#Descending bubble sort
def bubble_sort_desc(numbers):
    for i in range(n-1):
        for j in range(0, n-i-1):
            if numbers[j] < numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
    print("Marks of students in descending order:",numbers)
    top=input("\nDo you want to display top marks from the list (yes/no) : ")
    if top=='yes' or top=='y':
        top_five_marks_desc(numbers)
    else:
        print("\nThanks for using this program!")

def top_five_marks_asc(numbers):
    print("Top 5 Marks are:")
    print(*numbers[n:n-6:-1])

def top_five_marks_desc(numbers):
    print("Top 5 Marks are:")
    print(*numbers[0:5:])

#Accepting elements from user
numbers=[]
n=int(input("Enter number of students:"))
for i in range(n):
    number=int(input("Enter marks of student "+str(i+1)+":"))
    numbers.append(number)


#Menu
print("************MENU************")
print("1. Selection Sort\n2. Bubble sort")
choice=int(input("Enter your choice(1/2):"))
if choice==1:
    subchoice=int(input("1.Ascending\n2.Descending\nEnter your choice(1/2):"))
    if subchoice==1:
        selection_sort_asc(numbers)
    elif subchoice==2:
        selection_sort_desc(numbers)
elif choice==2:
    subchoice=int(input("1.Ascending\n2.Descending\nEnter your choice(1/2):"))
    if subchoice==1:
        bubble_sort_asc(numbers)
    elif subchoice==2:
        bubble_sort_desc(numbers)
else:
    print("Invalid choice")
