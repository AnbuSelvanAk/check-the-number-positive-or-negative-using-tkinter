from tkinter import*
from tkinter import messagebox as b
a=Tk()
a.title('+ve,-ve')
a.geometry('500x400')
def process():
    en=int(en_1.get())
    if en>0:
        la=Label(a,text='this is positive',font=('times new roman',16))
        la.place(x=50,y=150)
    else:
        la=Label(a,text='this is negative',font=('times new roman',16))
        la.place(x=50,y=150)
la_lb1=Label(a,text='positive negative',font=('times new roman',16))
la_lb1.pack()
la_lb1=Label(a,text='value',font=('times new roman',16)).place(x=20,y=50)
en_1=Entry(a,font=('times new roman',16),width=15)
en_1.place(x=100,y=52)
btn=Button(a,text='submit',font=('times new roman',16),command=process)
btn.place(x=50,y=100)
a.mainloop()
