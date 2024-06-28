import csv
def display():
    f=open("Student.csv","r")
    name=input("enter the student name")
    obj=csv.reader(f)
    next(f)
    for i in obj:
        if i[0]==name:
            print(i)
            print(len(str(i))*"-")
        else:
            print("No such data available by this name") 
    f.close()
display()
