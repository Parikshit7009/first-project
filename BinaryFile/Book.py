
def createbook():
    fobj=open("book.dat","wb")
    bookno=int(input("enter the book number"))
    book_name=input("enter the book name")
    author=input("enter the author nanme")
    price=int(input("enter the price of book"))
    rec=[bookno,book_name,author,price]
    pickle.dump(rec,fobj)
    fobj.close()



def countrec():
    fobj=open("book.dat","rb")
    num=0
    while True:
        rec=pickle.load(fobj)
    if author==rec[2]:
        num=mum+1
    fobj.close()


