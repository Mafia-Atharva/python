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
            rows.append(0))
        matrix.append(rows)
    return matrix

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
    if len(m1)==len(m2) and len(m1[0])==len(m2[0]):
        result=nullmx(len[m1],len(m1[0]))
        for i in range(len(m1)):
            for j in range(len(m1[0])):
                result[i][j]=m1[i][j]+m2[i][j]
    
