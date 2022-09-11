#Ascending selection sort
def selection_sort_asc(numbers):
    for i in range(n-1):
        min_number=i
        for j in range(i+1,n):
            if numbers[j]<numbers[min_number]:
                min_number=j
        numbers[i],numbers[min_number]=numbers[min_number],numbers[i]
    print(numbers)

#Descending selection sort
def selection_sort_desc(numbers):
    for i in range(n-1):
        min_number=i
        for j in range(i+1,n):
            if numbers[j]>numbers[min_number]:
                min_number=j
        numbers[i],numbers[min_number]=numbers[min_number],numbers[i]
    print(numbers)

#Ascending bubble sort
def bubble_sort_asc(numbers):
    for i in range(n-1):
        for j in range(0, n-i-1):
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
    print("Elements sorted using bubble sort:\n",numbers)

#Ascending bubble sort
def bubble_sort_desc(numbers):
    for i in range(n-1):
        for j in range(0, n-i-1):
            if numbers[j] < numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
    print("Elements sorted using bubble sort:\n",numbers)


#Accepting elements from user
numbers=[]
n=int(input("Enter number of numbers to sort:"))
for i in range(n):
    number=int(input("Enter number "+str(i+1)+":"))
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
