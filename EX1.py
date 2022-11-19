row = int(input("Insert Number of rows : "))
num = int(input("Insert Number of Diamond : "))

def diamond(num,row):
    for k in range(num):

        for i in range(row):
            print(" "*(row-i)+" *"*(i+1))

        for j in range(row-1):
            print(" "*(j+2)+" *"*(row-1-j))

diamond(num,row)