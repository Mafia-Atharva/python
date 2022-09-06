numbers=[]
n=int(input("Enter number of numbers to sort:"))
for i in range(n):
    number=int(input("Enter number "+str(i+1)+":"))
    numbers.append(number)

def selection_sort_asc(numbers):
    for i in range(n-1):
        min_number=i
        for j in range(i+1,n):
            if numbers[j]<numbers[min_number]:
                min_number=j
        numbers[i],numbers[min_number]=numbers[min_number],numbers[i]
    print(numbers)

def selection_sort_desc(numbers):
    for i in range(n-1):
        min_number=i
        for j in range(i+1,n):
            if numbers[j]>numbers[min_number]:
                min_number=j
        numbers[i],numbers[min_number]=numbers[min_number],numbers[i]
    print(numbers)

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
    bubble_sort(numbers)
else:
    print("Wrong choice")
    
