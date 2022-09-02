no=int(input("Enter number of students in class:"))
marks=[]

def average(marks):
    total=0
    abse=0
    for i in range(no):
        if(marks[i]!=0):
            total+=marks[i]
        else:
            abse+=1
    print("Average marks of class=",total/(no-abse))
    
def highest(main):
    highest=0
    for i in range(no):
        if(marks[i]>highest):
            highest=marks[i]
    print("Highest score in class=",highest)

def lowest(main):
    lowest=marks[0]
    for i in range(no):
        if(marks[i]<lowest):
            lowest=marks[i]
    print("Lowest score in class=",lowest)

def absent(main):
    absent_stu=0
    for i in range(no):
        if(marks[i]==0):
            absent_stu+=1
    print("Absent students=",absent_stu)
    
def frequency(marks):
    freq=0
    x=int(input("Enter marks to check frequency"))
    for i in range(no):
        if(marks[i]==x):
            freq+=1
    print("Frequency of entered marks=",freq)
    
for i in range(no):
    imarks=int(input("Enter marks of student "+str(i+1)+":"))
    marks.append(imarks)
average(marks)
highest(marks)
lowest(marks)
absent(marks)
frequency(marks)
