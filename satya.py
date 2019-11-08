from tkinter import *
from tkinter import messagebox
def message():
    msg=messagebox.showinfo("THANK YOU","THANKS FOR YOUR FEEDBACK")
def developer1():
    dev.destroy()
    global dev1
    dev1=Tk()
    dev1.wm_attributes('-fullscreen','true')

    q2=Label(dev1,text="\t\t",bg="orange",width=80,height=100)
    q2.place(x=0,y=0)
    q2.configure(font=("Times New Roman",15,"bold"),foreground="white")

    q3=Label(dev1,text="\t",bg="blue",width=80,height=100)
    q3.place(x=800,y=0)
    q3.configure(font=("Times New Roman",15,"bold"),foreground="white")
    
    back = PhotoImage(file="back.png")
    B1 = Button(dev1, image=back,bd=0,relief="flat",bg="orange",activebackground="orange",command=dev_des1)
    B1.place(x=20, y=80)
    Label(dev1,relief="solid",width=162,height=48,bg="black").place(x=200,y=30)
    Label(dev1, relief="solid", width=160, height=47).place(x=205, y=38)
    Label(dev1, relief="solid", width=157, height=22).place(x=215, y=48)
    me=PhotoImage(file="reresizeme3.png")
    me1= PhotoImage(file="reresizeme4.png")
    Label(dev1,image=me,relief="solid", width=250, height=300).place(x=225, y=57)
    Label(dev1, relief="solid", width=157, height=22).place(x=215, y=400)
    Label(dev1,image=me1, relief="solid", width=250, height=300).place(x=225, y=409)
    YASH='''Name:Yash'''
    Pulkit='''Name:Pulkit'''
    Label(dev1,justify=LEFT,text=YASH, relief="flat", width=34, height=10,font=("Times New Roman", 20)).place(x=500, y=57)
    Label(dev1, justify=LEFT, text=Pulkit, relief="flat", width=30, height=10, font=("Times New Roman", 20)).place(x=500, y=409)
    dev1.mainloop()
def dev_des1():
    dev1.destroy()
    main()

def developer():
    first.destroy()
    global dev
    dev=Tk()
    dev.wm_attributes('-fullscreen','true')

    q2=Label(dev,text="\t\t",bg="orange",width=80,height=100)
    q2.place(x=0,y=0)
    q2.configure(font=("Times New Roman",15,"bold"),foreground="white")

    q3=Label(dev,text="\t",bg="blue",width=80,height=100)
    q3.place(x=800,y=0)
    q3.configure(font=("Times New Roman",15,"bold"),foreground="white")
    
    back1 = PhotoImage(file="back.png")
    B1 = Button(dev, image=back1,bd=0,relief="flat",bg="orange",activebackground="orange",command=dev_des)
    B1.place(x=20, y=80)
    back2 = PhotoImage(file="right.png")
    B2 = Button(dev, image=back2,bd=0,relief="flat",bg="orange",activebackground="orange",command=developer1)
    B2.place(x=20, y=250)
    Label(dev,relief="solid",width=162,height=48,bg="black").place(x=200,y=30)
    Label(dev, relief="solid", width=160, height=47).place(x=205, y=38)
    Label(dev, relief="solid", width=157, height=22).place(x=215, y=48)
    me=PhotoImage(file="resizeme1.png")
    me1= PhotoImage(file="me2.png")
    Label(dev,image=me,relief="solid", width=250, height=300).place(x=225, y=57)
    Label(dev, relief="solid", width=157, height=22).place(x=215, y=400)
    Label(dev,image=me1, relief="solid", width=250, height=300).place(x=225, y=409)
    ANKIT='''Name: Ankit

E mail: ankitdokania47@gmail.com'''
    Satya='''Name: Satya Sai Dirisala
        
E mail: satyasai272@gmail.com'''
    Label(dev,justify=LEFT,text=ANKIT, relief="flat", width=34, height=10,font=("Times New Roman", 20)).place(x=500, y=57)
    Label(dev, justify=LEFT, text=Satya, relief="flat", width=30, height=10, font=("Times New Roman", 20)).place(x=500, y=409)
    dev.mainloop()
def dev_des():
    dev.destroy()
    main()
def info():
    global info
    info=Tk()
    info.wm_attributes('-fullscreen','true')

    q2=Label(info,text="\t\t",bg="orange",width=80,height=100)
    q2.place(x=0,y=0)
    q2.configure(font=("Times New Roman",15,"bold"),foreground="white")

    q3=Label(info,text="\t",bg="blue",width=80,height=100)
    q3.place(x=800,y=0)
    q3.configure(font=("Times New Roman",15,"bold"),foreground="white")
    
    exit = Button(info, justify=LEFT,bg="blue")
    ex = PhotoImage(file="icon.png")
    exit.config(image=ex, width="30", height="30", bd=0, command=inf_des,activebackground="blue")
    exit.place(x=1470,y=20)
    Label(info,relief="solid",width=162,height=48,bg="black").place(x=200,y=30)
    Label(info, relief="solid", width=160, height=47).place(x=205, y=38)
    information='''dfghsijaokxni uadbwan ndivubhbjhc vwdiub hyuB dyhi o
cdeuc bi cwn kins
cw vb iubnucow'''
    Label(info,justify=LEFT,text=information, relief="flat", width=50, height=20,font=("Times New Roman", 20)).place(x=500, y=47)
    info.mainloop()
def inf_des():
    info.destroy()
    main()
def info1():
    first.destroy()
    info()
def main():
    global first
    first=Tk()
    first.wm_attributes('-fullscreen','true')
    first.title('Travel Review System')

    

    q2=Label(first,text="\t\t",bg="orange",width=80,height=100)
    q2.place(x=0,y=0)
    q2.configure(font=("Times New Roman",15,"bold"),foreground="white")

    q3=Label(first,text="\t",bg="blue",width=80,height=100)
    q3.place(x=800,y=0)
    q3.configure(font=("Times New Roman",15,"bold"),foreground="white")
    
    q4=Label(first,text="TRAVEL  REVIEW",bg="black",width=80,height=3)
    q4.place(x=0,y=0)
    q4.configure(font=("Times New Roman",25,"bold"),foreground="white")
    
    exit = Button(first, justify=LEFT,bg="black")
    ex = PhotoImage(file="icon.png")
    exit.config(image=ex, width="30", height="30", bd=0, command=first.destroy,activebackground="black")
    exit.place(x=1470,y=20)

    fdb= Button(first, justify=LEFT,bg="black")
    fd = PhotoImage(file="feedback.png")
    fdb.config(image=fd, width="270", height="100", bd=0, command=feedback1)
    fdb.place(x=660,y=400)

    ab= Button(first, justify=LEFT,bg="blue")
    abt = PhotoImage(file="info.png")
    ab.config(image=abt, width="150", height="150", bd=0, command=info1)
    ab.place(x=1350,y=600)
    
    dv = Button(first, justify=LEFT)
    pic3 = PhotoImage(file="develop.png")
    dv.config(image=pic3, width="150", height="150", bd=0,bg="orange",activebackground="orange",command=developer)
    dv.place(x=50, y=600)

    first.mainloop()
def feedback1():
    first.destroy()
    feedback()
    
def feedback():
    global second
    second=Tk()
    second.wm_attributes('-fullscreen','true')
    second.title('Travel Review System')

    

    q2=Label(second,text="\t\t",bg="orange",width=80,height=100)
    q2.place(x=0,y=0)
    q2.configure(font=("Times New Roman",15,"bold"),foreground="white")

    q3=Label(second,text="\t",bg="blue",width=80,height=100)
    q3.place(x=800,y=0)
    q3.configure(font=("Times New Roman",15,"bold"),foreground="white")
    
    q4=Label(second,text="FEED BACK",bg="black",width=130,height=4)
    q4.place(x=0,y=0)
    q4.configure(font=("Times New Roman",15,"bold"),foreground="white")
    
    exit = Button(second, justify=LEFT,bg="black")
    ex = PhotoImage(file="icon.png")
    exit.config(image=ex, width="30", height="30", bd=0, command=second.destroy,activebackground="black")
    exit.place(x=1470,y=20)
    
    e1=Entry(second,bd=5)
    e1.place(x=950,y=300,width=500,height=100)
    
    b=Button(second,justify = LEFT)
    photo=PhotoImage(file="submit.png")
    b.config(image=photo,width="180",height="40",bd=0,activebackground="blue",command=message)
    b.place(x=1050,y=500)
    def help():
        help1='''Please comment about the
travelling on the right side
and press the submit button 
'''

        lb=Label(second, bg="black",height="500",width="60")
        lb.place(x=170,y=95)
        lb1=Label(second,text=help1,height="20",width="33",justify=LEFT,fg="white",font=("Verdana", 14), bg="black")
        lb1.place(x=175,y=100)
        def lb_dest():
            lb.destroy()
            lb1.destroy()
            exit1.destroy()

        exit1 = Button(second,text="X",fg="white",font=(20),justify=CENTER, bg="red",bd=0, activebackground="red",command=lb_dest,height="1",width="2",relief="flat")
        exit1.place(x=550, y=115)
    hp = Button(second, justify=LEFT, bg="orange", activebackground="orange",command=help)
    pic1 = PhotoImage(file="help1.png")
    hp.config(image=pic1, width="130", height="130", bd=0)
    hp.place(x=20, y=280)

    second.mainloop()
main()
