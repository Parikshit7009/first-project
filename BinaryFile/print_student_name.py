import pickle
F=open("Student.dat","rb")
read=pickle.load(F)
N=input("enter the name ")
for i in read:
    c=i.split()
    if N in c:
        print()
F.close()

 