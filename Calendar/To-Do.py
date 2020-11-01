from tkinter import *
from tkinter import ttk
from tkcalendar import *
import tkinter.scrolledtext as scrolledtext
import datetime as date
import smtplib
import re

#----------------------------------Tkinter Window Configurations-----------------------------------
root=Tk()
root.title("To-do List")
root.geometry("774x650")
root.resizable(False, False)
root.configure(background="#171717")
root.rowconfigure(12, {'minsize': 30})
root.columnconfigure(12, {'minsize': 30})

#--------------------------------------Styling for tkcalendar--------------------------------------
style = ttk.Style(root)
style.theme_use('clam')
style.configure('my.DateEntry', fieldbackground='#202020',foreground="white")

#------------------------Storing date in Variables & Initialising variables------------------------
today = date.datetime.now()
l=[int(i)for i in str(today).split()[0].split("-")]
y,m,d=l
no=1
lst=[]

#-----------------------Classes for Dropdown Calendar and Hover feature----------------------------
class MyDateEntry(DateEntry):
    def __init__(self, master=None, **kw):
        DateEntry.__init__(self, master=None, **kw)
        self._top_cal.configure(bg='#151515', bd=10)
        self.configure(justify='center')
        self.configure(style='my.DateEntry')
        Label(self._top_cal, bg='#202020', anchor='w',
                 text='Today: %s' % date.datetime.today().strftime('%d-%b-%Y'),fg="white").pack(fill='x')
class HoverButton(Button):
    def __init__(self, master, **kw):
        Button.__init__(self,master=master,**kw)
        self.defaultBackground = self["background"]
        self.bind("<Enter>", self.on_enter)
        self.bind("<Leave>", self.on_leave)
    def on_enter(self, e):
        self['background'] = self['activebackground']
    def on_leave(self, e):
        self['background'] = self.defaultBackground

#----------------------------------Verifying and Sending Mail--------------------------------------
def MailMe():
	global reciv
	subject="To do list"
	descript=""
	for i in range(0,len(lst)):
		descript+="{}. --{}--    ->{}\n{}\n\n".format(lst[i]["no"],lst[i]["SUBJ"],lst[i]["DATE"],lst[i]["DESC"])
	
	sendr="gooklebot0@gmail.com"
	passw="salikmalik941"
	msg=f'Subject: {subject}\n\n{descript}'
	server = smtplib.SMTP('smtp.gmail.com',587)
	server.ehlo()
	server.starttls()
	server.ehlo()
	server.login(sendr,passw)
	server.sendmail(sendr,reciv,msg)
	server.quit()

def verify():
	global reciv
	global pophd,popen,popfnl,popchk
	reciv=popen.get()
	regex = r'^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
	if re.search(regex,reciv):
		popfnl.configure(state=NORMAL,bg="#7740ad",fg="black")
		popchk.configure(state=DISABLED,bg="#202020")
	else:
		pophd=Label(popup,bg="#202020",fg="#D3D3D3",text="Enter a VALID id:",font=("",24,"bold"))
		pophd.place(relx=0.5,rely=0.25,anchor=CENTER)
		
		popen=Entry(popup,bg="#171717",justify="center",fg="#FFFFFF",insertbackground="#FFFFFF",bd=0,highlightthickness=0,width=23,font=("",15,""))
		popen.place(relx=0.5,rely=0.5,anchor=CENTER)
		popfnl=Button(popup,bg="#202020",fg="#FFFFFF",text="Confirm",font=("",10,"bold"),command=confirm,height=2,width=8,bd=0,highlightthickness=0)
		popfnl.place(relx=0.55,rely=0.65)

def confirm():
	coverFR.grid_forget()  #Remove Email Entry frame
	popup.place_forget()   #Remove Email Entry prompt


#-------------------------Storing To Do task into initialized variables----------------------------
def Save():
	global row,dlt
	global TodoSUBJ,TodoDESC,no
	global lst,Ldict

	TodoSUBJ=Ehead.get()
	TodoDESC=Edesc.get("1.0",END)
	TodoDATE=db.get()
	Ldict=dict()
	Ldict["no"]=no
	Ldict["SUBJ"]=TodoSUBJ
	Ldict["DESC"]=TodoDESC.rstrip()
	Ldict["DATE"]=TodoDATE
	lst.append(Ldict)
	no+=1

	db.configure(state=DISABLED)
	if row>=5:
		button.configure(state=DISABLED,activebackground="#7740ad")
	else:
		button.configure(state=NORMAL,bg="#7740ad",activebackground="#7750ad")
	sav.configure(state=DISABLED,text="SAVED",activebackground="#7740ad")

	Ehead.configure(state=DISABLED)
	Edesc.configure(state=DISABLED,bg="#202020")
	Edesc.vbar.pack_forget()

#-----------------------------------Add another ToDo task-----------------------------------------
def Createlabl():
	global row
	global lb,db,sav
	global head,desc,Ehead,Edesc
	global no,mmBUT,mm

	lb=Canvas(root,bg="#202020",width=755,height=100, bd=0, highlightthickness=0,)  #202020
	lb.grid(row=row,column=0,padx=10,pady=6)

	if no<1:
		mmBUT.configure(state=DISABLED,activebackground="#7740ad")
	else:
		mmBUT.configure(state=NORMAL,activebackground="#7750ad")

	db = MyDateEntry(lb,day=d, month=m, year=y,
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
	db.grid(row=row, column=0, sticky=NE, padx=17,pady=10)
	button.configure(state=DISABLED,bg="#252525",activebackground="#7740ad")

	sav=HoverButton(root,text="SAVE",command=Save,width=10,height=3,bg="#7740ad",fg="black",
		disabledforeground="grey80",relief="flat",activebackground="#7750ad",font=("",10,"bold"))
	sav.grid(row=row,column=0, sticky=SE,padx=18,pady=10)

	head=Frame(root,bg="#202020")
	head.grid(row=row,column=0,sticky=NW,padx=15,pady=10)
	Dhead=Label(head,text="To do SUBJECT : ",fg="#FFFFFF",bg="#202020").pack(side=LEFT)
	Ehead=Entry(head,width=78,insertbackground="#FFFFFF",bd=0,highlightthickness=0,
		bg="#191919",fg="#FFFFFF",font=("",10,"bold"),disabledbackground="#202020")
	Ehead.pack(side=RIGHT)

	desc=Frame(root,bg="#202020")
	desc.grid(row=row,column=0,sticky=SW,padx=15,pady=10)
	Ddesc=Label(desc,text="To do DESCRIPTION : ",fg="#FFFFFF",bg="#202020").pack(side=LEFT,anchor=NW)
	Edesc=scrolledtext.ScrolledText(desc,insertbackground="#FFFFFF",bd=0,highlightthickness=0,
		height=4,width=71,undo=True,font=("comicsans 9"),bg="#171717",fg="#FFFFFF")
	Edesc.pack(expand=True,fill="both",side=RIGHT)

	if row<5:
		row+=1

#-----------------------------------------ADD BUTTON----------------------------------------------
row=1
col=0
button=HoverButton(root,text="+",width=46,bg="#7740ad",   #252525  ,width=24,height=1
		font=("",20,""),command=Createlabl,relief="ridge",
		activebackground="#7750ad",disabledforeground="grey80")
button.grid(row=0,column=0,padx=10,pady=10)

#---------------------------------------Mail Me BUTTON-------------------------------------------
mm = Frame(root,bg="white")
mm.grid(row=12,column=0,sticky=S,pady=8)
mmBUT = HoverButton(mm,text="M a i l   M e",bg="#7740ad",relief="ridge",width=40,
		font=("",20,"bold"),command=MailMe,activebackground="#7750ad")
mmBUT.pack()
mmBUT.configure(state=DISABLED,activebackground="#7740ad")

#-------------------------------------Email Entry Prompt-----------------------------------------
coverFR=Frame(root,height=650,width=774,bg="#171717")
coverFR.grid(row=0,column=0)
popup=Label(coverFR,bg="#202020",bd=0,highlightthickness=0,width=50,height=14)  #height=180,width=600)
popup.place(relx=0.5,rely=0.45,anchor=CENTER)
pophd=Label(popup,bg="#202020",fg="#D3D3D3",text="Enter your gmail:",font=("",24,"bold"))
pophd.place(relx=0.5,rely=0.25,anchor=CENTER)
popen=Entry(popup,bg="#171717",justify="center",fg="#FFFFFF",insertbackground="#FFFFFF",bd=0,highlightthickness=0,width=23,font=("",15,""))
popen.place(relx=0.5,rely=0.5,anchor=CENTER)

popchk=Button(popup,bg="#7740ad",text="Verify",font=("",10,"bold"),command=verify,height=2,width=8,bd=0,highlightthickness=0)
popchk.place(relx=0.25,rely=0.65)
popfnl=Button(popup,bg="#7740ad",fg="#FFFFFF",text="Confirm",font=("",10,"bold"),command=confirm,height=2,width=8,bd=0,highlightthickness=0)
popfnl.place(relx=0.55,rely=0.65)
popfnl.configure(state=DISABLED,bg="#202020",disabledforeground="#FFFFFF")

root.mainloop()
