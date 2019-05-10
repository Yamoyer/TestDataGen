from faker import Faker
from pydbgen import pydbgen
import pandas as pd
from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
import os
import random
import openpyxl

myDB = pydbgen.pydb()
window = Tk()
global count


window.title("Test Data Gen")
window.config(background = 'light blue')
Label.config(window, background = 'light blue')
   
def firstwind():
    #need create an additional button to add another field name and type 
    lbl1 = Label(window, text='Type') #basic grid label
    lbl1.grid(column=2, row=0, pady=10)
    
    lbl = Label(window, text='Field Name') #basic grid label
    lbl.grid(column=0, row=0)

    var1 = StringVar(window) 
    var1.set('ssn')
    ent1 = Entry(window, width=15) #stores the Entry variable to display after the get data button is clicked
    ent1.grid(column=0, row=1)      
    dropDown1 = OptionMenu(window, var1, '','', 'ssn','name','country','date', 'company' )
    dropDown1.config(width=10)
    dropDown1.grid(column=2, row=1, sticky=W, pady = 3) 

    ent2 = Entry(window, width = 15)  #stores the Entry variable to display after the get data button is clicked
    ent2.grid(column=0, row=2) 
    var2 = StringVar(window)
    var2.set('name')
    dropDown2 = OptionMenu(window, var2, '', '', 'ssn','name','country','date', 'company' )
    dropDown2.config( width=10)
    dropDown2.grid(column=2, row=2, sticky=W, pady = 3)

    ent3 = Entry(window, width=15) #stores the Entry variable to display after the get data button is clicked
    ent3.grid(column=0, row=3)
    var3 = StringVar(window)
    var3.set('country')
    dropDown3 = OptionMenu(window, var3, '', '', 'ssn','name','country','date', 'company' )
    dropDown3.config(width=10)
    dropDown3.grid(column=2, row=3, sticky=W, pady = 3)

    ent4 = Entry(window, width=15) #stores the Entry variable to display after the get data button is clicked
    ent4.grid(column=0, row=4)
    var4 = StringVar(window)
    var4.set('date')
    dropDown4 = OptionMenu(window, var4, '', '', 'ssn','name','country','date', 'company' )
    dropDown4.config(width=10)
    dropDown4.grid(column=2, row=4, sticky=W, pady = 3)

    ent5 = Entry(window, width=15) #stores the Entry variable to display after the get data button is clicked
    ent5.grid(column=0, row=5)
    var5 = StringVar(window)
    var5.set("company")
    dropDown5 = OptionMenu(window, var5, '', '', 'ssn','name','country','date', 'company' )
    dropDown5.config(width=10)
    dropDown5.grid(column=2, row=5, sticky=W, pady = 3)
    #get rid of the zero at the beginning of the output
    
    

    entRows = Entry(window, width = 8)
    entRows.grid (column = 1, row = 7)
    lblRows = Label(window, text = 'Number of Rows?')
    lblRows.grid(column = 0, row=7, pady=20)
    def clear():
        
        list = window.grid_slaves()
        for l in list:
            
            l.destroy()
    
    def buttonWindow():

        optionsWindow = Tk()
        optionbutton1 = Button(optionsWindow, text = "all", command = optionbuttonWindow)
        optionbutton1.grid(column = 0, row = 0)
        window.mainloop()

    def optionbuttonWindow():

        btn2Window = Button(window, text = "ssn", command = buttonWindow)
        

    def addDataType():
        ent6 = Entry(window, width=15) #stores the Entry variable to display after the get data button is clicked
        ent6.grid(column=0, row=6)
        var6 = StringVar(window)
        var6.set("company")
        dropDown6 = OptionMenu(window, var6, '', '', 'ssn','name','country','date', 'company' )
        dropDown6.grid(column=2, row=6, sticky=W)


        #be able to print the input entry


        window.mainloop()  

    def insertdata():
        r = Tk()
        
        ent1var = ent1.get() #these variables place the entry data usable
        ent2var = ent2.get()
        ent3var = ent3.get()
        ent4var = ent4.get()
        ent5var = ent5.get()
        entRowsvalue = entRows.get()
        optionch1 = var1.get() #This gets the var for the main window from the option menu to be displayed in the insert data function
        optionch2 = var2.get()
        optionch3 = var3.get()
        optionch4 = var4.get()
        optionch5 = var5.get()
        
        dataFrameGen = myDB.gen_dataframe(int(entRowsvalue), fields= [optionch1, optionch2, optionch3, optionch4, optionch5])
        dataFrameGen.rename(columns ={optionch1 : ent1var, optionch2 : ent2var, optionch3 : ent3var, optionch4 : ent4var, optionch5 : ent5var }, inplace = True)
        dataFrameGen.to_excel('excel_test.xlsx', sheet_name = 'data')
        
        datagenlabel = Label(r, text = dataFrameGen)
        
        datagenlabel.grid(column=0, row=1)
        print(optionch1)

        #be able to print the input entry
        r.mainloop()



    #Buttons for Days    

    btn2Window = Button(window, text = "ssn", command = buttonWindow)
    btn2Window.grid(column=2, row = 7)   

    #optionbutton1 = Button(optionsWindow, text = "all", command = optionbuttonWindow)

    btn2 = Button(window, text='Add Another Field', command=addDataType)
    btn2.grid(column = 2, row = 8, pady = 5, padx = 5)    
    btn = Button(window, text='Get Data', command=insertdata)
    btn.grid(column = 0, row = 8, pady = 5, padx = 5)
    destroyButton = Button(window, text = 'Clear', command = clear).grid(column = 2, row = 7 )
firstwind()
window.mainloop()     
