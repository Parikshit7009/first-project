import pickle
F=open("Student.dat","wb")
L={}
c=int(input("how many student data you want to enter"))
for i in range(0,c,1):
    Class=int(input("Enter the class-:"))
    Name=input("enter the nane of student-: ")
    roll_no=int(input("Enter the roll number"))
    Section=input("Enter the section")
    L[Name]=[Class,Section,roll_no]
pickle.dump(L,F)

F.close()