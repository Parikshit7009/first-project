import csv
N="NOnoNo"
Y="yesYesYES"
def create():
    f=open("Student.csv","w",newline='')
    obj=csv.writer(f)
    header=["Student Name","Roll_No","Class","Age"]
    obj.writerow(header)
    while True:
        Std=input("enter the student name:-")
        rollno=int(input("enter the roll no:-"))
        Class=int(input("enter the class:-"))
        Age=int(input("enter the age:-"))
        rec=[Std,rollno,Class,Age]
        obj.writerow(rec)
        ch=input("Want to add more data or not Yes/NO:-")
        if ch in N:
            break
        elif ch in Y:
            continue
        else:
            print("unknown Character enter -ERROR 404-")
            break
    f.close()
create()
