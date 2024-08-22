
def binary():
    F=open("Student.dat","wb")
    L={}
    c=int(input("how many student data you want to enter"))
    while True:
       Class=int(input("Enter the class-:"))
       Name=input("enter the nane of student-: ")
       roll_no=int(input("Enter the roll number"))
       Section=input("Enter the section")
       L[Name]=[Class,Section,roll_no]
       pickle.dump(L,F)
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