import csv
def display():
    f=open("Student1.csv","r")
    obj=csv.reader(f) 
    next(f)
    while True:  
        name=input("enter the student name")
        for i in obj:
            if i[0]==name:
                print(i)
                print(len(str(i))*"-")
        ch=input("want to read more data")
        if ch =="n":
            break
    f.close()
