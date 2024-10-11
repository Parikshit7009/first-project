import mysql.connector
def sql1():
    con=mysql.connector.connect(host='localhost',user='root',password='6618',database='FirstProject')
    cur=con.cursor()
    #cur.execute("create database FirstProject")
    #cur.execute("create table student(class Integer,Name varchar(20),rollno Integer,Section varchar(2))")
    while True:
       Class=int(input("Enter the class-:"))
       Name=input("enter the nane of student-: ")
       rollno=int(input("Enter the roll number"))
       section=input("Enter the section")
       obj="INSERT into student value({},'{}',{},'{}')".format("Class","Name","rollno","section")
       cur.execute(obj)
       ch=input("Want to add more data ENTER Y(YES)/N(No):-")
       if ch=="N":
            break
       elif ch=="Y":
            continue
       else:
            print("unknown Character enter -ERROR 404- ")
            break
    con.commit()
    con.close()
sql1()
