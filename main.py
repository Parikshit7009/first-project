def list1():
    l=[]
    let=int(input("enter the range of list"))
    for i in range (0,let,1):
        a=int(input("enter the number"))
        l.append(a)
        l.append(a)
    print(l)

    return l