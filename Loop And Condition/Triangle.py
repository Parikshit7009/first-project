#Triange AND Square  made using loop
F="NnNOnoNo"# this string is in use in line 15
G="YyYESYesyes"#this string is in use in line 17
D="rectangle square"#this string is in use in line 13
while True:
    o=input("Select your shape Triangle or (square/ rectangle) ")
    m=input("enter the design")
    s=int(input("Enter a Number which should be greater than 4-:"))
    if s<4:
        print("Error")
        break
    else:
        if o in D:
            v=int(input("enter the value"))
            for i in range(0,s,1):
                for j in range(0,v,1):
                    print(m,end="")
                print()
        else:
            for i in range(0,s,1):
                for j in range(0,i+1,1):
                    print(m,end="")
                print()
    n=input("want to continue or not Y OR N")
    if n in F:
        break
    elif n in G:
        continue
    else:
        print("Error")
        break