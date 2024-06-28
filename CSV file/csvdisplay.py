import csv
def display():
    f=open("Student.csv","r")
    
    obj=csv.reader(f)
    next(f)
    while True:
        name=input("enter the student name")
        for i in obj:
            if i[0]==name:
                print(i)
                print(len(str(i))*"-")
            else:
                print("No such data available by this name") 
        ch=input("want to read more data")
        if ch =="n":
            break
    f.close()
display()
