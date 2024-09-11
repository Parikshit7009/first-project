def countword(fun4):
    try:
        with open(fun4,"r") as F:
            Read=F.read()
            word=Read.split()
            c=0
            for i in word:
               c=c+1
               print(c)
    except:
        print("file not available")