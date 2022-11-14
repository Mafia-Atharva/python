def input():
    r=int(input("Enter number of rows:"))
    c=int(input("Enter number of columns:"))
    matrix=[]
    for i in range(r):
        rows=[]
        for j in range(c):
            rows.append(int(input("Enter element:")))
        matrix.append(rows)
    return matrix

def nullmx(r,c):
    matrix=[]
    for i in range(r):
        rows=[]
        for j in range(c):
            rows.append((0))
        matrix.append(rows)
    return matrix
    
def display(m):
    for i in range(len(m)):
        for j in range(len(m[0])):
            print(m[i][j]," ",end="")

def add(m1,m2):
    if len(m1)==len(m2) and len(m1[0])==len(m2[0]):
        result=nullmx(len[m1],len(m1[0]))
        for i in range(len(m1)):
            for j in range(len(m1[0])):
                result[i][j]=m1[i][j]+m2[i][j]
        return result
    else:
        print("Cannot add matrices with unequal dimensions!")

def sub(m1,m2):
    if len(m1)==len(m2) and len(m1[0])==len(m2[0]):
        result=nullmx(len[m1],len(m1[0]))
        for i in range(len(m1)):
            for j in range(len(m1[0])):
                result[i][j]=m1[i][j]-m2[i][j]
        return result
    else:
        print("Cannot subtract matrices with unequal dimensions!")
        
def multiply(m1,m2):
    if len(m1[0])==len(m2):
        result=nullmx(len[m1],len(m1[0]))
        for i in range(len(m1)):
            for j in range(len(m2[0])):
                for k in range(len(m2)):
                    result[i][j]=m1[i][K]+m2[K][j]
        return result
    else:
        print("Cannot multiply matrices with unequal number of columns and rows")
        
def transpose(m):
    result=nullmx(len[m],len(m[0]))
    for i in range(len(m)):
        for j in range(len(m[0])):
            result[j][i]=m[i][j]
    return result
    
def menu():
    print("*************MENU*************")
    print("1.Add\n2.Subtract\n3.Multiply\n4.Transpose")
    print("Enter your choice:")
    
m1=input()
m2=input()
operations={1:add,2:sub,3:multiply,4:transpose}

while True:
    menu()
    choice=int(input())
    operations.get(choice,"Incorrect input. Please try again!")
