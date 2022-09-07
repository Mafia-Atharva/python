#Function to check average marks
def average(marks):
    total=0
    abse=0
    for i in range(no):
        if(marks[i]!=0):
            total+=marks[i]
        else:
            abse+=1
    print("\nAverage marks of class=",total/(no-abse),"\n")

#Function to check highest marks    
def highest(marks):
    highest=0
    for i in range(no):
        if(marks[i]>highest):
            highest=marks[i]
    print("\nHighest score in class=",highest,"\n")

#Function to check lowest marks    
def lowest(marks):
    lowest=marks[0]
    for i in range(no):
        if(marks[i]<lowest):
            lowest=marks[i]
    print("\nLowest score in class=",lowest,"\n")

#Function to check absent students    
def absent(marks):
    absent_stu=0
    for i in range(no):
        if(marks[i]==0):
            absent_stu+=1
    print("\nAbsent students=",absent_stu,"\n")

#Function to check frequency of marks    
def frequency(marks):
    freq=0
    x=int(input("Enter marks to check frequency"))
    for i in range(no):
        if(marks[i]==x):
            freq+=1
    print("\nFrequency of entered marks=",freq,"\n")

#Main       
marks=[]
no=int(input("Enter number of students:"))
for i in range(no):
    imarks=int(input("Enter marks of student "+str(i+1)+":"))
    marks.append(imarks)   
while True:
    print("****************Menu****************")
    choice=int(input("1.Calculate Average Marks\n2.Calculate highest marks\n3.Calculate lowest marks\n4.Calculate number of absent students\n5.Calculate frequency of marks\n6.Exit\nEnter your choice(1/2/3/4/5/6):"))
    if choice==1:
        average(marks)   
    elif choice==2:
        highest(marks)
    elif choice==3:
        lowest(marks)
    elif choice==4:
        absent(marks)
    elif choice==5:
        frequency(marks)
    elif choice==6:
        print("Thank you for using this program!")
        break
    else:
        print("Please enter a valid choice")
