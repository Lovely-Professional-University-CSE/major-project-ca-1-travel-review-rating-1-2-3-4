import pandas as pd
from nltk.corpus import stopwords
def popupmsg(msg):
    popup = tk.Tk()
    popup.wm_title("!")
    label = ttk.Label(popup, text=msg)
    label.pack(side="top", fill="x", pady=10)
    B1 = ttk.Button(popup, text="Okay", command = popup.destroy)
    B1.pack()
    popup.mainloop()
stop_words = set(stopwords.words("english"))
from sklearn.feature_extraction.text import CountVectorizer

vector = CountVectorizer()
review = pd.read_csv("G:/project/ww.csv", encoding='unicode_escape')
table = str.maketrans("!@#$%^&*().,", 12 * " ")
data = []
answer = []

for index, row in review.iterrows():
    data.append(row["Review"])
    answer.append(row["Rating"])

for i in range(len(data)):
    data[i] = data[i].translate(table)

from nltk.stem.snowball import SnowballStemmer

dat = []
stemmer = SnowballStemmer("english")
for i in (data):
    if (stemmer.stem(i) not in stop_words):
        dat.append(stemmer.stem(i))
print(stemmer.stem("this is not a very appriated"))
vector.fit(dat)
bag_of_words = vector.transform(dat)
from sklearn.feature_extraction.text import TfidfTransformer

vectorizer = TfidfTransformer()
poo = vectorizer.fit_transform(bag_of_words)
from sklearn.naive_bayes import MultinomialNB

clf = MultinomialNB().fit(poo, answer)
abc = [" terribly disappointed bad ugly disgusting", "beautiful good ugly "]
tex = vector.transform(abc)
textc = vectorizer.transform(tex)
print(clf.predict(textc))
print(clf)




import sys

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk

    py3 = False
except ImportError:
    import tkinter.ttk as ttk

    py3 = True

import unknown_support


def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    top = Toplevel1(root)
    unknown_support.init(root, top)
    root.mainloop()


w = None


def create_Toplevel1(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = tk.Toplevel(root)
    top = Toplevel1(w)
    unknown_support.init(w, top, *args, **kwargs)
    return (w, top)


def destroy_Toplevel1():
    global w
    w.destroy()
    w = None


class Toplevel1:
    def doit(self):
        self.Message1_5.configure(text="Na")
        a = self.Entry1.get()
        b=self.Entry1_12.get()
        c=self.Entry1_13.get()
        d=self.Entry1_14.get()
        count=0
        e=[a,b,c,d]

        f=0
        ee=[]
        for i in (e):
            if (stemmer.stem(i) not in stop_words):
                ee.append(stemmer.stem(i))


        print(ee)
        tex = vector.transform(ee)
        textc = vectorizer.transform(tex)
        y=(clf.predict(textc))
        for i in range(4):
            if(y[i]==4 and ee[i]==''):
                ans="N.A"
                y[i]=0
            else:
                f=f+1
                ans=y[i]
            print(i)
            if(i==2):
                self.Message1_3.configure(text=ans)
            elif(i==1):
                self.Message1_11.configure(text=ans)
            elif(i==3):
                self.Message1_4.configure(text=ans)
            elif(i==0):
                self.Message1_51.configure(text=ans)
        if(f!=0):
            self.Message1_7.configure(text=(sum(y)//f))
        else:
            self.Message1_7.configure(text=("N.A."))

    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9'  # X11 color: 'gray85'
        _ana1color = '#d9d9d9'  # X11 color: 'gray85'
        _ana2color = '#ececec'  # Closest X11 color: 'gray92'
        font12 = "-family {Sitka Display} -size 19 -weight bold -slant" \
                 " roman -underline 0 -overstrike 0"
        font13 = "-family {Segoe UI Black} -size 14 -weight bold " \
                 "-slant roman -underline 0 -overstrike 0"
        font14 = "-family {Segoe UI Black} -size 24 -weight bold " \
                 "-slant roman -underline 1 -overstrike 0"
        font16 = "-family {Segoe UI} -size 19 -weight bold -slant " \
                 "roman -underline 0 -overstrike 0"

        top.geometry("930x619+259+53")
        top.minsize(120, 1)
        top.maxsize(1370, 749)
        top.resizable(1, 1)
        top.title("Review System")
        top.configure(background="#a33a47")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")

        self.Message1_7 = tk.Message(top)
        self.Message1_7.place(relx=0.417, rely=0.84, relheight=0.086
                              , relwidth=0.174)
        self.Message1_7.configure(background="#a33a47")
        self.Message1_7.configure(borderwidth="5")
        self.Message1_7.configure(font=font16)
        self.Message1_7.configure(foreground="#ffffff")
        self.Message1_7.configure(highlightbackground="#d9d9d9")
        self.Message1_7.configure(highlightcolor="#ffffff")
        self.Message1_7.configure(justify='center')
        self.Message1_7.configure(text='''..''')
        self.Message1_7.configure(width=150)

        self.Button1 = tk.Button(top, command=self.doit)
        self.Button1.place(relx=0.799, rely=0.872, height=44, width=137)
        self.Button1.configure(activebackground="#ececec")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#a33a47")
        self.Button1.configure(borderwidth="5")
        self.Button1.configure(cursor="pirate")
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(font=font13)
        self.Button1.configure(foreground="#ffffff")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''Get Review''')

        self.menubar = tk.Menu(top, font="TkMenuFont", bg=_bgcolor, fg=_fgcolor)
        top.configure(menu=self.menubar)

        self.Canvas1 = tk.Canvas(top)
        self.Canvas1.place(relx=0.0, rely=0.129, relheight=0.683, relwidth=0.999)

        self.Canvas1.configure(background="#e1cf79")
        self.Canvas1.configure(borderwidth="2")
        self.Canvas1.configure(highlightbackground="#d9d9d9")
        self.Canvas1.configure(highlightcolor="black")
        self.Canvas1.configure(insertbackground="#ffffff")
        self.Canvas1.configure(relief="ridge")
        self.Canvas1.configure(selectbackground="#c86931")
        self.Canvas1.configure(selectforeground="black")

        self.Message1_11 = tk.Message(self.Canvas1)
        self.Message1_11.place(relx=0.846, rely=0.118, relheight=0.102
                               , relwidth=0.116)
        self.Message1_11.configure(background="#e1cf7f")
        self.Message1_11.configure(font=font12)
        self.Message1_11.configure(foreground="#ffffff")
        self.Message1_11.configure(highlightbackground="#d9d9d9")
        self.Message1_11.configure(highlightcolor="black")
        self.Message1_11.configure(justify='center')
        self.Message1_11.configure(text='''..''')
        self.Message1_11.configure(width=100)

        self.Entry1 = tk.Entry(self.Canvas1)
        self.Entry1.place(relx=0.023, rely=0.733, height=60, relwidth=0.711)
        self.Entry1.configure(background="white")
        self.Entry1.configure(disabledforeground="#a3a3a3")
        self.Entry1.configure(font="-"
                                   "family {Sitka Display} -size 15 -weight bold")
        self.Entry1.configure(foreground="#000000")
        self.Entry1.configure(highlightbackground="#d9d9d9")
        self.Entry1.configure(highlightcolor="black")
        self.Entry1.configure(insertbackground="black")
        self.Entry1.configure(selectbackground="#c4c4c4")
        self.Entry1.configure(selectforeground="black")

        self.Entry1_12 = tk.Entry(self.Canvas1)
        self.Entry1_12.place(relx=0.023, rely=0.095, height=60, relwidth=0.711)
        self.Entry1_12.configure(background="white")
        self.Entry1_12.configure(disabledforeground="#a3a3a3")
        self.Entry1_12.configure(font="-family {Sitka Display} -size 15 -weight bold")
        self.Entry1_12.configure(foreground="#000000")
        self.Entry1_12.configure(highlightbackground="#d9d9d9")
        self.Entry1_12.configure(highlightcolor="black")
        self.Entry1_12.configure(insertbackground="black")
        self.Entry1_12.configure(selectbackground="#c4c4c4")
        self.Entry1_12.configure(selectforeground="black")

        self.Entry1_13 = tk.Entry(self.Canvas1)
        self.Entry1_13.place(relx=0.023, rely=0.307, height=60, relwidth=0.711)
        self.Entry1_13.configure(background="white")
        self.Entry1_13.configure(disabledforeground="#a3a3a3")
        self.Entry1_13.configure(font="-family {Sitka Display} -size 15 -weight bold")
        self.Entry1_13.configure(foreground="#000000")
        self.Entry1_13.configure(highlightbackground="#d9d9d9")
        self.Entry1_13.configure(highlightcolor="black")
        self.Entry1_13.configure(insertbackground="black")
        self.Entry1_13.configure(selectbackground="#c4c4c4")
        self.Entry1_13.configure(selectforeground="black")

        self.Entry1_14 = tk.Entry(self.Canvas1)
        self.Entry1_14.place(relx=0.023, rely=0.52, height=60, relwidth=0.711)
        self.Entry1_14.configure(background="white")
        self.Entry1_14.configure(disabledforeground="#a3a3a3")
        self.Entry1_14.configure(font="-family {Sitka Display} -size 15 -weight bold")
        self.Entry1_14.configure(foreground="#000000")
        self.Entry1_14.configure(highlightbackground="#d9d9d9")
        self.Entry1_14.configure(highlightcolor="black")
        self.Entry1_14.configure(insertbackground="black")
        self.Entry1_14.configure(selectbackground="#c4c4c4")
        self.Entry1_14.configure(selectforeground="black")

        self.Message1_3 = tk.Message(self.Canvas1)
        self.Message1_3.place(relx=0.846, rely=0.307, relheight=0.102
                              , relwidth=0.116)
        self.Message1_3.configure(background="#e1cf7f")
        self.Message1_3.configure(font="-family {Sitka Display} -size 19 -weight bold")
        self.Message1_3.configure(foreground="#ffffff")
        self.Message1_3.configure(highlightbackground="#d9d9d9")
        self.Message1_3.configure(highlightcolor="black")
        self.Message1_3.configure(justify='center')
        self.Message1_3.configure(text='''..''')
        self.Message1_3.configure(width=100)

        self.Message1_4 = tk.Message(self.Canvas1)
        self.Message1_4.place(relx=0.846, rely=0.52, relheight=0.102
                              , relwidth=0.116)
        self.Message1_4.configure(background="#e1cf7f")
        self.Message1_4.configure(font="-family {Sitka Display} -size 19 -weight bold")
        self.Message1_4.configure(foreground="#ffffff")
        self.Message1_4.configure(highlightbackground="#d9d9d9")
        self.Message1_4.configure(highlightcolor="black")
        self.Message1_4.configure(justify='center')
        self.Message1_4.configure(text='''..''')
        self.Message1_4.configure(width=100)

        self.Message1_51 = tk.Message(self.Canvas1)
        self.Message1_51.place(relx=0.846, rely=0.733, relheight=0.102
                              , relwidth=0.116)
        self.Message1_51.configure(background="#e1cf7f")
        self.Message1_51.configure(font="-family {Sitka Display} -size 19 -weight bold")
        self.Message1_51.configure(foreground="#ffffff")
        self.Message1_51.configure(highlightbackground="#d9d9d9")
        self.Message1_51.configure(highlightcolor="black")
        self.Message1_51.configure(justify='center')
        self.Message1_51.configure(text='''..''')
        self.Message1_51.configure(width=100)

        self.Message1_5 = tk.Message(self.Canvas1)
        self.Message1_5.place(relx=0.694, rely=1.262, relheight=0.102
                              , relwidth=0.116)
        self.Message1_5.configure(background="#d9d9d9")
        self.Message1_5.configure(font="-family {Sitka Display} -size 19 -weight bold")
        self.Message1_5.configure(foreground="#000000")
        self.Message1_5.configure(highlightbackground="#d9d9d9")
        self.Message1_5.configure(highlightcolor="black")
        self.Message1_5.configure(text='''NA''')
        self.Message1_5.configure(width=100)

        self.Canvas1_1 = tk.Canvas(top)
        self.Canvas1_1.place(relx=0.0, rely=0.0, relheight=0.134, relwidth=0.999)

        self.Canvas1_1.configure(background="#a33a47")
        self.Canvas1_1.configure(borderwidth="2")
        self.Canvas1_1.configure(highlightbackground="#d9d9d9")
        self.Canvas1_1.configure(highlightcolor="black")
        self.Canvas1_1.configure(insertbackground="#ffffff")
        self.Canvas1_1.configure(relief="ridge")
        self.Canvas1_1.configure(selectbackground="#c86931")
        self.Canvas1_1.configure(selectforeground="black")

        self.Message1_2 = tk.Message(self.Canvas1_1)
        self.Message1_2.place(relx=0.29, rely=0.12, relheight=0.759
                              , relwidth=0.406)
        self.Message1_2.configure(background="#a33a47")
        self.Message1_2.configure(font=font14)
        self.Message1_2.configure(foreground="#ffffff")
        self.Message1_2.configure(highlightbackground="#d9d9d9")
        self.Message1_2.configure(highlightcolor="#ffffff")
        self.Message1_2.configure(justify='center')
        self.Message1_2.configure(text='''Travel Review Rating''')
        self.Message1_2.configure(width=350)

        self.Entry1_16 = tk.Entry(self.Canvas1_1)
        self.Entry1_16.place(relx=0.657, rely=7.265, height=64, relwidth=0.074)
        self.Entry1_16.configure(background="white")
        self.Entry1_16.configure(disabledforeground="#a3a3a3")
        self.Entry1_16.configure(font="-family {Sitka Display} -size 15 -weight bold")
        self.Entry1_16.configure(foreground="#000000")
        self.Entry1_16.configure(highlightbackground="#d9d9d9")
        self.Entry1_16.configure(highlightcolor="black")
        self.Entry1_16.configure(insertbackground="black")
        self.Entry1_16.configure(selectbackground="#c4c4c4")
        self.Entry1_16.configure(selectforeground="black")




####################################################################################################33



#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 4.26
#  in conjunction with Tcl version 8.6
#    Nov 01, 2019 11:49:10 PM IST  platform: Windows NT

import sys

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

import kkk_support

def vp_start_guii():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    top = Toplevel1z(root)
    kkk_support.init(root, top)
    root.mainloop()

w = None
def create_Toplevel1z(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = tk.Toplevelz(root)
    top = Toplevel1z(w)
    kkk_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Toplevel1z():
    global w
    w.destroy()
    w = None

class Toplevel1z:
    def start(self):
        root.destroy()
        vp_start_guin()



    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'

        top.geometry("930x619+175+68")
        top.minsize(120, 1)
        top.maxsize(1370, 749)
        top.resizable(1, 1)
        top.title("Front Page")
        top.configure(background="#e1cf79")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")

        self.Canvas1 = tk.Canvas(top)
        self.Canvas1.place(relx=0.266, rely=0.242, relheight=0.764
                , relwidth=0.733)
        self.Canvas1.configure(background="#a33a47")
        self.Canvas1.configure(borderwidth="2")
        self.Canvas1.configure(highlightbackground="#d9d9d9")
        self.Canvas1.configure(highlightcolor="black")
        self.Canvas1.configure(insertbackground="black")
        self.Canvas1.configure(relief="ridge")
        self.Canvas1.configure(selectbackground="#c4c4c4")
        self.Canvas1.configure(selectforeground="black")

        self.Canvas2 = tk.Canvas(top)
        self.Canvas2.place(relx=0.0, rely=0.0, relheight=0.457, relwidth=0.64)
        self.Canvas2.configure(background="#a33a47")
        self.Canvas2.configure(borderwidth="2")
        self.Canvas2.configure(highlightbackground="#d9d9d9")
        self.Canvas2.configure(highlightcolor="black")
        self.Canvas2.configure(insertbackground="black")
        self.Canvas2.configure(relief="ridge")
        self.Canvas2.configure(selectbackground="#c4c4c4")
        self.Canvas2.configure(selectforeground="black")

        self.Label1 = tk.Label(self.Canvas2)
        self.Label1.place(relx=0.217, rely=0.212, height=151, width=264)
        self.Label1.configure(activebackground="#8683b9")
        self.Label1.configure(activeforeground="black")
        self.Label1.configure(background="#a33a47")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(font="-family {Segoe UI} -size 28 -weight bold")
        self.Label1.configure(foreground="#e1cf79")
        self.Label1.configure(highlightbackground="#d9d9d9")
        self.Label1.configure(highlightcolor="black")
        self.Label1.configure(text='''Travel Review''')

        self.Canvas3 = tk.Canvas(top)
        self.Canvas3.place(relx=0.417, rely=0.468, relheight=0.522
                , relwidth=0.582)
        self.Canvas3.configure(background="#e1cf79")
        self.Canvas3.configure(borderwidth="2")
        self.Canvas3.configure(highlightbackground="#d9d9d9")
        self.Canvas3.configure(highlightcolor="black")
        self.Canvas3.configure(insertbackground="black")
        self.Canvas3.configure(relief="ridge")
        self.Canvas3.configure(selectbackground="#c4c4c4")
        self.Canvas3.configure(selectforeground="black")

        self.Button1 = tk.Button(self.Canvas3,command=self.start)
        self.Button1.place(relx=0.358, rely=0.402, height=54, width=187)
        self.Button1.configure(activebackground="#ececec")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#e1cf79")
        self.Button1.configure(borderwidth="9")
        self.Button1.configure(cursor="tcross")
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(font="-family {Segoe UI} -size 28 -weight bold")
        self.Button1.configure(foreground="#a33a47")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''Let's Go''')





##############################################################################33









#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 4.26
#  in conjunction with Tcl version 8.6
#    Nov 03, 2019 03:44:47 PM IST  platform: Windows NT

import sys

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

import second_support

def vp_start_guin():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    top = Toplevel1m (root)
    second_support.init(root, top)
    root.mainloop()
word=None
w = None
def create_Toplevel1m(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = tk.Toplevelm(root)
    top = Toplevel1m(w)
    second_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Toplevel1m():
    global w
    w.destroy()
    w = None


class Toplevel1m:

    def last(self):
        a=self.Entry2.get()
        if(a!=''):
            root.destroy()
            vp_start_gui()
        else:
            popupmsg("Please Enter Destination")

    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'
        font10 = "-family {Segoe UI} -size 14 -weight bold -slant "  \
            "roman -underline 0 -overstrike 0"
        font12 = "-family {Segoe UI} -size 12 -weight bold -slant "  \
            "roman -underline 0 -overstrike 0"
        font13 = "-family {Segoe UI Black} -size 13 -weight bold "  \
            "-slant roman -underline 0 -overstrike 0"
        font9 = "-family {Segoe UI} -size 20 -weight bold -slant roman"  \
            " -underline 0 -overstrike 0"

        top.geometry("930x619+194+65")
        top.minsize(120, 1)
        top.maxsize(1370, 749)
        top.resizable(1, 1)
        top.title("New Toplevel")
        top.configure(background="#e1cf79")

        self.Frame1 = tk.Frame(top)
        self.Frame1.place(relx=0.023, rely=0.016, relheight=0.961
                , relwidth=0.446)
        self.Frame1.configure(relief='groove')
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief="groove")
        self.Frame1.configure(background="#a33a47")

        self.Entry1 = tk.Entry(self.Frame1)
        self.Entry1.place(relx=0.208, rely=0.353,height=20, relwidth=0.556)
        self.Entry1.configure(background="white")
        self.Entry1.configure(disabledforeground="#a3a3a3")
        self.Entry1.configure(font=font13)
        self.Entry1.configure(foreground="#000000")
        self.Entry1.configure(insertbackground="black")

        self.Entry1_2 = tk.Entry(self.Frame1)
        self.Entry1_2.place(relx=0.156, rely=0.639,height=20, relwidth=0.66)
        self.Entry1_2.configure(background="white")
        self.Entry1_2.configure(disabledforeground="#a3a3a3")
        self.Entry1_2.configure(font=font13)
        self.Entry1_2.configure(foreground="#000000")
        self.Entry1_2.configure(highlightbackground="#d9d9d9")
        self.Entry1_2.configure(highlightcolor="black")
        self.Entry1_2.configure(insertbackground="black")
        self.Entry1_2.configure(selectbackground="#c4c4c4")
        self.Entry1_2.configure(selectforeground="black")

        self.Message1 = tk.Message(self.Frame1)
        self.Message1.place(relx=0.234, rely=0.218, relheight=0.123
                , relwidth=0.468)
        self.Message1.configure(background="#a33a47")
        self.Message1.configure(font=font9)
        self.Message1.configure(foreground="#ffffff")
        self.Message1.configure(highlightbackground="#d9d9d9")
        self.Message1.configure(highlightcolor="black")
        self.Message1.configure(text='''* Name :''')
        self.Message1.configure(width=180)

        self.Message2 = tk.Message(self.Frame1)
        self.Message2.place(relx=0.182, rely=0.941, relheight=0.022
                , relwidth=0.571)
        self.Message2.configure(background="#a33a47")
        self.Message2.configure(font=font10)
        self.Message2.configure(foreground="#ffffff")
        self.Message2.configure(highlightbackground="#d9d9d9")
        self.Message2.configure(highlightcolor="black")
        self.Message2.configure(text='''* => optional''')
        self.Message2.configure(width=220)

        self.Message1_7 = tk.Message(self.Frame1)
        self.Message1_7.place(relx=0.208, rely=0.471, relheight=0.156
                , relwidth=0.571)
        self.Message1_7.configure(background="#a33a47")
        self.Message1_7.configure(font="-family {Segoe UI} -size 20 -weight bold")
        self.Message1_7.configure(foreground="#ffffff")
        self.Message1_7.configure(highlightbackground="#d9d9d9")
        self.Message1_7.configure(highlightcolor="black")
        self.Message1_7.configure(text='''* Email :''')
        self.Message1_7.configure(width=220)

        self.Frame2 = tk.Frame(top)
        self.Frame2.place(relx=0.544, rely=0.016, relheight=0.961
                , relwidth=0.434)
        self.Frame2.configure(relief='groove')
        self.Frame2.configure(borderwidth="2")
        self.Frame2.configure(relief="groove")
        self.Frame2.configure(background="#a33a47")

        self.Button1_6 = tk.Button(self.Frame2,command=self.last)
        self.Button1_6.place(relx=0.32, rely=0.756, height=44, width=157)
        self.Button1_6.configure(activebackground="#ececec")
        self.Button1_6.configure(activeforeground="#ffffff")
        self.Button1_6.configure(background="#a33a47")
        self.Button1_6.configure(borderwidth="5")
        self.Button1_6.configure(cursor="boat")
        self.Button1_6.configure(disabledforeground="#a3a3a3")
        self.Button1_6.configure(font="-family {Segoe UI} -size 20 -weight bold")
        self.Button1_6.configure(foreground="#ffffff")
        self.Button1_6.configure(highlightbackground="#d9d9d9")
        self.Button1_6.configure(highlightcolor="black")
        self.Button1_6.configure(pady="0")
        self.Button1_6.configure(text='''Proceed''')

        self.Entry2 = tk.Entry(self.Frame2)
        self.Entry2.place(relx=0.213, rely=0.538,height=20, relwidth=0.571)
        self.Entry2.configure(background="white")
        self.Entry2.configure(disabledforeground="#a3a3a3")
        self.Entry2.configure(font=font12)
        self.Entry2.configure(foreground="#000000")
        self.Entry2.configure(insertbackground="black")

        self.Message1_8 = tk.Message(self.Frame2)
        self.Message1_8.place(relx=0.187, rely=0.319, relheight=0.173
                , relwidth=0.613)
        self.Message1_8.configure(background="#a33a47")
        self.Message1_8.configure(font="-family {Segoe UI} -size 20 -weight bold")
        self.Message1_8.configure(foreground="#ffffff")
        self.Message1_8.configure(highlightbackground="#d9d9d9")
        self.Message1_8.configure(highlightcolor="black")
        self.Message1_8.configure(text='''Travel Destination :''')
        self.Message1_8.configure(width=230)

    @staticmethod
    def popup1(event, *args, **kwargs):
        Popupmenu1 = tk.Menu(root, tearoff=0)
        Popupmenu1.configure(activebackground="#f9f9f9")
        Popupmenu1.configure(activeborderwidth="1")
        Popupmenu1.configure(activeforeground="black")
        Popupmenu1.configure(background="#d9d9d9")
        Popupmenu1.configure(borderwidth="1")
        Popupmenu1.configure(disabledforeground="#a3a3a3")
        Popupmenu1.configure(font="{Segoe UI} 9")
        Popupmenu1.configure(foreground="black")
        Popupmenu1.post(event.x_root, event.y_root)









if __name__ == '__main__':
    vp_start_guii()
