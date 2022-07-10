from cgitb import html
from select import select
from tkinter import *
import tkinter
import pyodbc
import pandas as pd
import os,webbrowser
import tkinter.font as tkFont
from PIL import Image,ImageTk
sr=""
sb=""
sc=""
sg=""
v1=0
v2=0
v3=0

from tkinter.ttk import *

window = Tk()

window.title("Predict your Dream College")

window.geometry('1920x1080')
bg=ImageTk.PhotoImage(file="p1.jpg")

# Show image using label
label1 = Label( window, image = bg)
label1.place(x = 0,y = 0)

def_font = tkinter.font.nametofont("TkDefaultFont")
def_font.config(size=20)

lbl = Label(window, text="Enter your rank")

lbl.grid(column=5, row=1,padx=100,pady=20)

txt = Entry(window,width=20,font=("Helvetica",20))

txt.grid(column=7, row=1,padx=100,pady=20,ipady=10)

def clicked():

    lbl.configure(text="Seletced rank is: ")
    global sr
    sr=txt.get()

btn = Button(window, text="Submit Your Details", command=clicked)

btn.grid(column=7, row=7,padx=100,pady=20)

lbl1 = Label(window, text="Enter your branch")

lbl1.grid(column=5, row=3,padx=100,pady=20)


combo = Combobox(window,font=("Helvetica",20))

combo['values']= ("None","CIV","CSE","ECE","EEE","INF","MEC")

combo.current(0) #set the selected item
def month_changed(event):
    global sb
    sb=combo.get()
    
combo.bind('<<ComboboxSelected>>', month_changed)


combo.grid(column=7, row=3,padx=100,pady=20)

lbl3 = Label(window, text="Caste")
lbl3.grid(column=5, row=4,padx=100,pady=20)



combo2 = Combobox(window,font=("Helvetica",20))

combo2['values']= ('None','OC','BC_A','BC_B','BC_C','BC_D','BC_E','SC','ST' )

combo2.current(0) #set the selected item

combo2.grid(column=7, row=4,padx=100,pady=20)
def month_changed1(event):
    global sc
    sc=combo2.get()
    
combo2.bind('<<ComboboxSelected>>', month_changed1)

###########
lbl4 = Label(window, text="Gender")
lbl4.grid(column=5, row=5,padx=100,pady=20)

combo1 = Combobox(window,font=("Helvetica",20))

combo1['values']= ('BOY','GIRL')

combo1.current(0) #set the selected item
def month_changed(event):
    global sg
    sg=combo1.get()
    
combo1.bind('<<ComboboxSelected>>', month_changed)

combo1.grid(column=7, row=5,padx=100,pady=20)


def click_me():
    global v1,v2,v3
    v1=i.get()
    v2=i1.get()
    v3=i2.get()
 

i=IntVar()
c = Checkbutton(window, text = "Branch", variable=i)
c.grid(column=7, row=8,padx=100,pady=20)
i1=IntVar()
c1 = Checkbutton(window, text = "Caste", variable=i1)
c1.grid(column=7, row=9,padx=100,pady=20)
i2=IntVar()
c2 = Checkbutton(window, text = "Gender", variable=i2)
c2.grid(column=7, row=10,padx=100,pady=20)

b = Button(window,text="Apply filter",command=click_me)
b.grid(column=7, row=11,padx=100,pady=20)


window.mainloop()


conn=pyodbc.connect(
    "Driver={SQL Server Native Client 11.0};"
    "Server=LAPTOP-OCH5SQE1\SQLEXPRESS;"
    "Database=Mainproject;"
    "Trusted_Connection=yes;"
)


sb="'"+sb+"'"

k=0
if(sg=="BOY"):
    k=1
else:
    k=2

# print("The selected rank is :"+sr)
# print("The selected branch is "+sb)
# print("The selected gender "+sg)
# print("The selected caste "+sc)

sql_query=''

if(v1==1 and v2==0 and v3==0):
    print("Branch is selected")
    sql_query='select * from rankdb where branch='+sb
elif(v1==0 and v2==1 and v3==0):
    print("Caste is selected")
    sql_query='select inst_code,institute_name,dist,year_of_est,branch,'+sc+',affiliated from rankdb where '+sc+'>='+str(sr)
elif(v1==0 and v2==0 and v3==1):
    print("Gender is selected")
    sql_query='select * from rankdb where code='+str(k)
elif(v1==1 and v2==1 and v3==0):
    print("Branch and Caste is selected")
    sql_query='select inst_code,institute_name,dist,year_of_est,branch,'+sc+',affiliated from rankdb where branch='+sb+' and '+sc+'>='+str(sr)
elif(v1==0 and v2==1 and v3==1):
    print("Caste and Gender is selected")
    sql_query='select inst_code,institute_name,dist,year_of_est,branch,'+sc+',affiliated from rankdb where '+sc+'>='+str(sr)+' and code='+str(k)
elif(v1==1 and v2==0 and v3==1):
    print("Branch and Gender is selected")
    sql_query='select * from rankdb where branch='+sb+' and '+'code='+str(k)
elif(v1==1 and v2==1 and v3==1):
    print("All are selected")
    sql_query='select inst_code,institute_name,dist,year_of_est,branch,'+sc+',affiliated from rankdb where '+sc+'>='+str(sr)+' and code='+str(k) +' and branch='+sb+'order by '+sc
else:
    sql_query='select * from rankdb where OC>='+str(sr)+'and BC_A>='+str(sr)+'and BC_B>='+str(sr)+'and BC_C>='+str(sr)+'and BC_D>='+str(sr)+' and BC_E>='+str(sr)+'and SC>='+str(sr)+'and ST>='+str(sr)+'order by OC'

print(sql_query)

df=pd.read_sql(sql_query,conn)
html=df.to_html()
file = open("index.html", "w")
file.write(html)
file.close()


filename = 'file:///'+os.getcwd()+'/' + 'index.html'
webbrowser.open_new_tab(filename)

print(df)