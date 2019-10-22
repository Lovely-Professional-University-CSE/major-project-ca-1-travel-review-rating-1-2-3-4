from tkinter import *
import tkfontchooser

def landing():
    root = Tk()
    
    def userChange(event):
        name_entry.delete(0, END)
        
    def go():
        print("Approved");
    
    w = root.winfo_screenwidth()
    h = root.winfo_screenheight()
    l = int(350)
    t = int(80)
    size = "690x510" + "+" + str(l) + "+" + str(t)
    root.geometry(size)
    root.title("Matta Travels")
    #root.iconbitmap(r'lp.ico')
    root.resizable(False, False)
    
    back = Frame(root, bg="#4b5162", height=510, width=690)
    back.pack()
    
    font = tkfontchooser.Font(family="Calibri", size=22)
    title = Label(back, text="Matta Travels", width=60, height=50, font=font, bg="#4b5162", fg="#383c4a")
    title.place(x=10, y=-200)
                  
    name = Label(back, text="Full Name", width=30, height=1, bg="#4b5162", fg="#383c4a")
    name.place(relx=0.5, rely=0.5, x=-201, y=-23)
    name_entry = Entry(back, width=40)
    name_entry.insert(0, "Full Name")
    name_entry.place(relx=0.5, rely=0.5, x=-120, y=0)
    name_entry.bind("<Button-1>", userChange)
    
    goButton = Button(back, text="Go", bg="#323741", fg="#222025", bd="0", width=15, height=1,
                         anchor=N,
                         command=go)
    goButton.place(x=135, y=445)
 
    root.mainloop()   

landing()