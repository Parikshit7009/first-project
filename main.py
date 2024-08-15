#in progress
from MAIN.Import import*
FUN=int(input("Select one option from above="))
if FUN==1:
    print("1. Add Header")
    print("---------------")
    print("2. Add Data ")
    print("---------------")
    print("3. Display the data")
    print("---------------")
    ch=int(input("SELECT ONE OPTION FORM ABOVE OPTION "))
    while True:
        if ch == 1:
           Header()
        elif ch ==2:
           Add_Data()
        elif ch==3:
           display()
        else:
           print("wrong input")
           break
        n="noNONo"
        y="yesYesYES"
        ch=input("want to enter more data")
        if ch in n:
           break
        elif ch in y:
           continue
        else:
           break

elif FUN==2:
   shape()
elif FUN==3:
   print("no")