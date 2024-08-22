
def Add_Data():
    f=open("Student1.csv","a",newline='')
    obj=csv.writer(f)
    while True:
        Std=input("enter the student name:-")
        rollno=int(input("enter the roll no:-"))
        Class=int(input("enter the class:-"))
        Age=int(input("enter the age:-"))
        rec=[Std,rollno,Class,Age]
        obj.writerow(rec)
        ch=input("Want to add more data ENTER Y(YES)/N(No):-")
        if ch=="N":
            break
        elif ch=="Y":
            continue
        else:
            print("unknown Character enter -ERROR 404- ")
            break
    f.close()

