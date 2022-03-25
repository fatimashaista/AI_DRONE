# -*- coding: utf-8 -*-


from tkinter import *
from tkinter import messagebox


class MainWindow:
 
    def __init__(self, master):
        self.master = master
        self.master.geometry("1200x750+0+0")
        self.master.title("COVID-19")
        self.master.config(bg="#009FBF")

        f = Frame(self.master, height=1080, width=1920, bg="azure", relief="ridge", bd=20)
        f.propagate(0)
        f.pack()

        self.mainTitle = Label(f, text="COVID-19 System", fg="red" ,bg="azure", font=("Helvetica", 30, "bold italic")).place(
            x=500, y=200)
        self.regi = Button(f, text="Face Mask Detection", width=20, height=5, fg="royalblue4", bg="lavender",
                           font=("Helvetica", 10, "bold italic"), command=self.c_reg)
        self.login = Button(f, text="Persons Detection", width=20, height=5, fg="royalblue4", bg="lavender",
                            font=("Helvetica", 10, "bold italic"), command=self.c_login)
        self.sda = Button(f, text="Social Distancing", width=20, height=5, fg="royalblue4", bg="lavender",
                            font=("Helvetica", 10, "bold italic"), command=self.sd)
        
        self.sv = Button(f, text="Control Room", width=20, height=5, fg="royalblue4", bg="lavender",
                            font=("Helvetica", 10, "bold italic"), command=self.svm)
        self.regi.place(x=200, y=300)
        self.login.place(x=400, y=300)
        self.sda.place(x=600, y=300)
        self.sv.place(x=800, y=300)
        

    def c_reg(self):
        import detect_mask

    def c_login(self):
        import person
    
    def sd(self):
        import sd

    def svm(self):
        self.newWindow = Toplevel(self.master)
        self.newWindow.resizable(0, 0)
        self.app = Register(self.newWindow)

class Register:

    def __init__(self, master):
        global mReg
        mReg = master
        self.master = master
        self.master.geometry("1200x750+0+0")
        self.master.title("COVID-19")
        self.master.config(bg="azure")
        global f1
        f1 = Frame(self.master, height=1080, width=1920, bg="azure", relief="ridge", bd=20)
        f1.propagate(0)
        f1.pack()

        self.mainTitle = Label(f1, text="Control Room", fg="red" ,bg="azure", font=("Helvetica", 30, "bold italic")).place(
            x=400, y=200)
        

        self.cancel = Button(f1, text="Persons Count", width=20, height=5, fg="royalblue4", bg="lavender",
                             font=("Helvetica", 10, "bold italic"), command=self.check)
        self.check = Button(f1, text="Video Streaming", width=20, height=5, fg="royalblue4", bg="lavender",
                             font=("Helvetica", 10, "bold italic"), command=self.c_cancel)
        self.cancel.place(x=400, y=300)
        self.check.place(x=600, y=300)

    def check(self):
        import pcount


    def c_cancel(self):
        import cvediostream      
        


root = Tk()
root.resizable(0, 0)
RegObj = MainWindow(root)
root.mainloop()