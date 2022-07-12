# EamcetCollegePredictor
This is a tool which helps you in predicting a list of colleges that you might get based on the Rank you obtained.
Here,we collected a database of colleges in .csv format with each college against it's closing rank for all the branches available.Then,we used microsoft sql to execute the queries written each time when the user try to find the colleges he would get based on his rank.We connected to the database(.csv file) using pyodbc(a open sourse  python module).

How to run the code:
You can see on youtube if you want how to attach the database to microsoft sql.
The following code snippet is used to connect you to the database:
 conn=pyodbc.connect(
    "Driver={SQL Server Native Client 11.0};"
    "Server=LAPTOP-6A1MGS32\SQLEXPRESS;"
    "Database=Clgrank;"
    "Trusted_Connection=yes;"
)

Modules used are as follows:

tkinter module is used to write the GUI for the user inpurt.

webbrowser module provides a high-level interface to allow displaying web-based documents to users.The open_new_tab() function from this module is used to give the expected colleges in new tab.

select module to write the queries.A filter is employed where the user can select caste,gender and branch that leaves us to 7 different choices with each attribute either added to the filter or not.
