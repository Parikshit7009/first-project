
def binary():
    F=open("Student.dat","wb")
    L={}
    while True:
       Class=int(input("Enter the class-:"))
       Name=input("enter the nane of student-: ")
       roll_no=int(input("Enter the roll number"))
       Section=input("Enter the section")
       L[Name]=[Class,Section,roll_no]
       pickle.dump(L,F)
       ch=input("Want to add more data ENTER Y(YES)/N(No):-")
       if ch=="N":
            break
       elif ch=="Y":
            continue
       else:
            print("unknown Character enter -ERROR 404- ")
            break
    F.close()


def bindisplay():
    F=open("Student.dat","rb")
    read=pickle.load(F)
    N=input("enter the name ")
    for i in read:
        c=i.split()
        if N in c:
            print()
    F.close()