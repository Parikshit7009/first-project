
def Header():
    f=open("Student1.csv","a",newline='')
    obj=csv.writer(f)
    n=input("want to add header if no inter ")
    header=["Student Name","Roll_No","Class","Age"]
    obj.writerow(header)