#in progress
from CSV_file.csvadd import *
from CSV_file.csvdisplay import *
from CSV_file.header import *
from LoopAndCondition.Triangle import *
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
elif FUN==2:
   shape()
elif FUN==3:
   