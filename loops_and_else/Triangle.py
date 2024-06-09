#Triange made using loop
F="NnNOnoNo"#use this string in line 15
G="YyYESYesyes"#use this string in line 17
while True:
    s=int(input("Enter a Number which should be greater than 4"))
    if s<4:
        print("Error")
        break
    else:
        for i in range(0,s,1):
            for j in range(0,i+1,1):
                print(i,end="")
            print()
    n=input("want to continue or not Y OR N")
    if n in F:
        break
    elif n in G:
        continue
    else:
        print("Error")
        break
    