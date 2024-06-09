#Triange AND Square  made using loop
F="NnNOnoNo"#use this string in line 15
G="YyYESYesyes"#use this string in line 17
d="rectangle square"
while True:
    o=input("Select your shape Triangle or (square/ rectangle) ")
    s=int(input("Enter a Number which should be greater than 4-:"))
    m=input("enter the design")
    if s<4:
        print("Error")
        break
    else:
        if o in d:
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