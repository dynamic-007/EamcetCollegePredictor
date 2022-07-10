from select import select
from tkinter import *
import pyodbc
import pandas as pd
sr=""
sb=""
sc=""
sg=""
v1=0
v2=0
v3=0

from tkinter.ttk import *

window = Tk()

window.title("Welcome to LikeGeeks app")

window.geometry('500x500')
lbl = Label(window, text="Enter your rank")

lbl.grid(column=0, row=0)

txt = Entry(window,width=20)

txt.grid(column=2, row=0)

def clicked():

    lbl.configure(text="Seletced rank is: ")
    global sr
    sr=txt.get()

btn = Button(window, text="set", command=clicked)

btn.grid(column=0, row=19)

lbl1 = Label(window, text="Enter your branch")

lbl1.grid(column=0, row=3)


combo = Combobox(window)

combo['values']= ("None","CIV","CSE","ECE","EEE","INF","MEC")

combo.current(0) #set the selected item
def month_changed(event):
    global sb
    sb=combo.get()
    
combo.bind('<<ComboboxSelected>>', month_changed)


combo.grid(column=2, row=3)

lbl3 = Label(window, text="Caste")
lbl3.grid(column=0, row=6)



combo2 = Combobox(window)

combo2['values']= ('OC','BC_A','BC_B','BC_C','BC_D','BC_E','SC','ST' )

combo2.current(0) #set the selected item

combo2.grid(column=0, row=7)
def month_changed1(event):
    global sc
    sc=combo2.get()
    
combo2.bind('<<ComboboxSelected>>', month_changed1)

###########
lbl4 = Label(window, text="Gender")
lbl4.grid(column=0, row=12)
combo1 = Combobox(window)

combo1['values']= ('BOY','GIRL')

combo1.current(0) #set the selected item
def month_changed(event):
    global sg
    sg=combo1.get()
    
combo1.bind('<<ComboboxSelected>>', month_changed)

combo1.grid(column=0, row=18)


def click_me():
    global v1,v2,v3
    v1=i.get()
    v2=i1.get()
    v3=i2.get()
 

i=IntVar()
c = Checkbutton(window, text = "Branch", variable=i)
c.grid(column=0, row=20)
i1=IntVar()
c1 = Checkbutton(window, text = "Caste", variable=i1)
c1.grid(column=0, row=21)
i2=IntVar()
c2 = Checkbutton(window, text = "Gender", variable=i2)
c2.grid(column=0, row=22)

b = Button(window,text="Set filter",command=click_me)
b.grid(column=0, row=23)



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

print("The selected rank is :"+sr)
print("The selected branch is "+sb)
print("The selected gender "+sg)
print("The selected caste "+sc)

sql_query=''
if(v1==1 and v2==0 and v3==0):
    print("Branch is selected")
    sql_query='select * from rankdb where branch='+sb
elif(v1==0 and v2==1 and v3==0):
    print("Caste is selected")
    sql_query='select inst_code,institute_name,place,dist,year_of_estb,branch,'+sc+' from rankdb where '+sc+'>='+str(sr)
elif(v1==0 and v2==0 and v3==1):
    print("Gender is selected")
    sql_query='select * from rankdb where code='+str(k)
elif(v1==1 and v2==1 and v3==0):
    print("Branch and Caste is selected")
    sql_query='select inst_code,institute_name,place,dist,year_of_estb,branch,'+sc+' from rankdb where branch='+sb+' and '+sc+'>='+str(sr)
elif(v1==0 and v2==1 and v3==1):
    print("Caste and Gender is selected")
    sql_query='select inst_code,institute_name,place,dist,year_of_estb,branch,'+sc+' from rankdb where '+sc+'>='+str(sr)+' and code='+str(k)
elif(v1==1 and v2==0 and v3==1):
    print("Branch and Gender is selected")
    sql_query='select * from rankdb where branch='+sb+' and '+'code='+str(k)
elif(v1==1 and v2==1 and v3==1):
    print("All are selected")
    sql_query='select inst_code,institute_name,place,dist,year_of_estb,branch,'+sc+' from rankdb where '+sc+'>='+str(sr)+' and code='+str(k) +' and branch='+sb
else:
    print("No filter is selected")

print(sql_query)

df=pd.read_sql(sql_query,conn)

print(df)