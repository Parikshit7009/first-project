def long():
    f=open("line.txt","r")
    lines=f.readlines()
    for i in lines:
        line=i.split()
        if len(line) <= 10:
            print(i)
    f.close()
long()