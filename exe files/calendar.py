from tkinter import *
from tkinter import ttk
from tkcalendar import *
import datetime

root=Tk()
root.title("Calendar")

style = ttk.Style(root)
style.theme_use('clam')

today = datetime.datetime.now()
l=[int(i)for i in str(today).split()[0].split("-")]
print(l)
y,m,d=l

db = Calendar(root,day=d, month=m, year=y,
              #font=("",25,""),
              cursor="hand1",
              date_pattern="dd-mm-y",
              selectbackground='#7740ad',  #SELECTED DATE
              selectforeground='white',
              normalbackground='#202020',
              normalforeground='#FFFFFF',   #NORMAL DATE COLORS
              background='#171717',
              foreground='#FFFFFF',
              bordercolor='#171717',
              othermonthforeground='#D3D3D3',
              othermonthbackground='#171717',
              othermonthweforeground='#9F0000',
              othermonthwebackground='#171717',
              weekendbackground='#202020',
              weekendforeground='red',
              headersbackground='#171717',
              headersforeground='#606060')

db.pack()
root.mainloop()
