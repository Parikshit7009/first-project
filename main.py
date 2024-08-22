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
   shape()#loop
elif FUN==3:
   print("1. Want to enter book data ")
   print("2. want to enter the student data")
   fun3=int(input("select any one option form the above"))
   if fun3==1:
      print("1. Want to add data  ")
      print("2. want count the data")
      fun3=int(input("select any one option form the above"))
      if fun3==1:
         createbook()
      elif fun3==2:
         countrec()
      else:
         print("error ")

   elif fun3==2:
      print("1. Want to add data  ")
      print("2. want access the data")
      fun3=int(input("select any one option form the above"))
      if fun3==1:
         binary()
      elif fun3==2:
         bindisplay()
      else:
         print("error ")


elif FUN==4:
   print("coming soon")