#in progress
from CSV_file.csvadd import *
from CSV_file.csvdisplay import *
from CSV_file.header import *
while True:
    print("1. Add Header")
    print("2. Add Data ")
    print("3. Display the data")
    ch=int(input("SELECT ONE OPTION FORM ABOVE OPTION "))
    if ch == 1:
        Header()
    elif ch ==2:
        Add_Data()
    elif ch==3:
        display()
    else:
        print("wrong input")
