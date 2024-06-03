def countword():
    F=open("ParagraphParagraphs are the group of sen","r")
    Read=F.read()
    word=Read.split()
    for i in word:
        c=c+1
        print(c)
    F.close()
countword()
