from tkinter import *
from tkinter import messagebox
def message():
    msg=messagebox.showinfo("THANK YOU","THANKS FOR YOUR FEEDBACK")
def main():
    global first
    first=Tk()
    first.wm_attributes('-fullscreen','true')
    first.title('Travel Review System')
    
    s=PhotoImage(file="bcc.png")
    k=Label(first,image=s)
    k.place(x=0,y=0)

    q2=Label(first,text="TRAVEL REVIEW",bg="black",width=130,height=4)
    q2.place(x=0,y=0)
    q2.configure(font=("Times New Roman",15,"bold"),foreground="white")
    exit = Button(first, justify=LEFT,bg="black")
    ex = PhotoImage(file="icon.png")
    exit.config(image=ex, width="30", height="30", bd=0, command=first.destroy,activebackground="black")
    exit.place(x=1470,y=20)
    
    e1=Entry(first,bd=5)
    e1.place(x=950,y=300,width=500,height=100)
    
    b=Button(first,justify = LEFT)
    photo=PhotoImage(file="sub2.png")
    b.config(image=photo,width="200",height="40",bd=0,activebackground="black",command=message)
    b.place(x=1050,y=500)

    first.mainloop()
main()
