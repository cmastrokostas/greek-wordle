import tkinter as tk
from functools import partial
from tkinter.constants import CENTER, RIGHT, VERTICAL,END,BOTTOM
from turtle import bgcolor
from unittest import result
from Solver import *

class App():
    def __init__(self,main):
        
        main.geometry('500x500-40-30')  
        main.title('GREEKΛE Solver')


        self.topFrame=tk.Frame(main,background='green')
        self.topFrame.grid(row=0, sticky='nsew')
        

        self.midFrame1=tk.Frame(main,background='gray30')
        self.midFrame1.grid(row=1,sticky="nswe")

        self.midFrame2=tk.Frame(main,background='gray50')
        self.midFrame2.grid(row=2,sticky="nswe")

        self.botFrame=tk.Frame(main,background='gray80')
        self.botFrame.grid(row=3,sticky="nswe")

     
        main.grid_rowconfigure(0, weight=8)
        main.grid_rowconfigure(1, weight=8)
        main.grid_rowconfigure(2, weight=8)
        main.grid_rowconfigure(3, weight=1)
        main.grid_columnconfigure(0, weight=1)
        
        self.Logo=tk.Label(self.topFrame,text="GREEKΛE Solver",bd=5,bg='green',font=('Brush Script MT',14,'')).place(relx=0.2,rely=0.5,anchor=CENTER)
        self.text=tk.Text(self.botFrame)
        self.text.pack(fill=tk.Y)
    

        #Labels & Entries
        self.Word=tk.Label(self.midFrame1,borderwidth='218',text='Word:',bd=5,bg='gray30',font=('Adobe Arabic',14,''))
        self.Word.place(relx=0.1,rely=0.5,anchor=CENTER)
        self.word=tk.StringVar(self.midFrame1)
        self.wordEntry=tk.Entry(self.midFrame1,bd=4,textvariable=self.word).place(relx=0.2,rely=0.2)
        
        self.Colors=tk.Label(self.midFrame2,borderwidth='218',text='Colors:',bd=5,bg='gray50',font=('Adobe Arabic',14,''))
        self.Colors.place(relx=0.1,rely=0.5,anchor=CENTER)
        self.color=tk.StringVar(self.midFrame2)
        self.colorEntry=tk.Entry(self.midFrame2,bd=4,textvariable=self.color).place(relx=0.2,rely=0.2)

        self.enterButton=tk.Button(self.midFrame2,text='Enter',width=10,bg='gray50',command=self.findPossibleResults).place(relx=0.85,rely=0.35)

    def findPossibleResults(self):
        results=possibleMatches(self.word.get(),self.color.get())
        count=0
        for word in results:
            if count==len(results)-1:self.text.insert(tk.END,word+'\n')
            else: self.text.insert(tk.INSERT,word+'\n')
            count+=1

    def mainf(self,main):
        App(main)
        main.mainloop()


if __name__=='__main__':
    root = tk.Tk()
    app=App(root)
    root.mainloop()