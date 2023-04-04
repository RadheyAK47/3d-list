import random
from tkinter import*
root=Tk()

root.title("list")
root.geometry("400x400")
root.configure(bg="#856232")

label=Label(root)
arra=[[["1","2","3","4","5","6"],["a","b","c","d","e","f"],["!","@","#","$","%","^"]]]

def password():
    r1=random.randint(0,6)
    r2=random.randint(0,6)
    r3=random.randint(0,6)
    
    l1=str(arra[0][0][r1])
    l2=str(arra[0][1][r2])
    l3=str(arra[0][2][r3])
    label["text"]=l1+" "+l2+" "+l3

    
btn=Button(root,bg="#946789",command=password,text="password")
btn.place(relx=0.5,rely=0.5,anchor=CENTER)
label.place(relx=0.5,rely=0.7,anchor=CENTER)
root.mainloop()
