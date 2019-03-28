from faker import Faker
from pydbgen import pydbgen
import pandas
from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
import os
import random
import openpyxl

myDB = pydbgen.pydb()

global menuList 
global entryList
global buttonList
global newMenuList
newMenuList = ['ssn', 'name','country', 'date', 'company','state','city', 'real_(US)_cities',
 'US_state', 'zipcode', 'latitude', 'longitude','Month', 'weekday', 'year', 'time', 'date',  
'Personal_email', 'official_email', 'Job_title', 'phone_number', 'license_plate']
buttonList = []
buttonListVals = [] 
entryList = []    
entryListVals =[]

menuList = ['ssn', 'name','country', 'date', 'company',]

def createType():

    def addRow():
        
        
        for i in range(len(newMenuList)): 
            fieldButton = Button(window, text = newMenuList[i], command = otherTypes) 
            entryPointadd = Entry(window, width = 15)
        entryPointadd.grid(column = 0, row = window.grid_size()[1], pady = 3, padx = 3)
        
        fieldButton.grid(column= 2, row = window.grid_size()[1] - 1, pady = 3, padx = 3)
        fieldButton.configure(takefocus = 0)    
 
        entryList.insert(len(entryList)+ 1, entryPointadd)      
        buttonList.insert(len(buttonList) + 1, fieldButton.cget("text"))

        print(buttonList)
    def buttonClick():
        try:
            if entRows.get() == '':
                messagebox.showerror(title = 'Error', message = 'Please enter number of rows.')

            elif not (1 <= int(entRows.get()) <= 1000000):
                messagebox.showerror(title = 'Error', message = 'Please enter a number between 1 and 1,000,000 for number of rows.')

            elif entryPoint.get() == '':
                messagebox.showerror(title = 'Error', message = 'Please enter field names for all fields.')

            else:
                r = Tk()    
                entRowsvalue = entRows.get()
                 
                for entry in entryList:
                    entryListVals.append(entry.get())
                print(entryListVals)
                
                for value in buttonList:
                    buttonListVals.append(value)
                print(buttonListVals)
                    
                dataFrameGen = myDB.gen_dataframe(int(entRowsvalue), fields = buttonListVals)      
                
                for i in range(len(buttonListVals)):
                    dataFrameGen.rename(columns = {buttonListVals[i] : entryListVals[i]}, inplace = True)
                
                datagenlabel = Label(r, text = dataFrameGen)
                datagenlabel.grid(column=0) 
                dataFrameGen.to_excel('excel_test.xlsx', sheet_name = 'data') 
                buttonListVals.clear()
                entryListVals.clear()             
                r.mainloop()

        except ValueError:
            messagebox.showerror(title = 'Error', message = 'Please enter a number between 1 and 1,000,000 for number of rows.')        
    
    def deleteRows():
        gridList = window.grid_size()
        destroyButton = buttonList.pop()
        destroyEntry = entryList.pop()

        print(gridList)
        print(buttonList)
        print(entryList)
        entryPoint.destroy()
        fieldButton.destroy()
        window.mainloop()
    


    def otherTypes():
        
        window2 = Tk()
        
        for i in range(len(newMenuList)):
            global fakerButton
            fakerButton = Button(window2, text = newMenuList[i], width = 20, command = createType)
            fakerButton.pack()
            #newMenuList.append(fakerButton.cget('text'))

            print(newMenuList)


    #window Config
    window = Tk()
    window.title("Test Data Gen")
    window.config(background = 'light blue')
    window.geometry('450x400+0+0')

    
    lbl1 = Label(window, text='Field Types') #basic grid label
    lbl1.grid(column=2, row=2, pady=10, padx = 20)
    lbl1.config(font=("Hevetica", 15), background = 'light blue')

    lbl = Label(window, text='Field Names') #basic grid label
    lbl.grid(column=0, row=2)
    lbl.grid_columnconfigure((0,1,2), weight = 1)
    lbl.config(font=("helvetica", 15), background = 'light blue')

    entRows = Entry(window, width = 13)
    entRows.grid (column = 1, row = 1)
    entRows.focus_set()

    lblRows = Label(window, text = 'Number of rows:')
    lblRows.grid(column = 0, row=1,  pady=5, padx = 20)
    lblRows.config(font=("Helvetica", 15), background = 'light blue')
    
    dataBtn = Button(window, text='Generate Data', command=buttonClick)
    dataBtn.grid(column = 1, row = 0, pady = 5, padx = 5, sticky = NSEW) 
    dataBtn.configure(takefocus = 0)    
            
    listLen = len(menuList)

    for i in range(listLen):

        entryPoint = Entry(window, width = 15)
        
        entryPoint.grid(column = 0, row = i + 3, pady = 3, padx = 3)
        entryPoint.configure(takefocus = 1)
        
        fieldButton = Button(window, text = menuList[i], command = otherTypes)
        fieldButton.configure(takefocus = 0)
        
        addFieldBtn = Button(window, text = 'Add Field', command = addRow)   
        addFieldBtn.configure(takefocus = 0)
        addFieldBtn.grid(column = 2, row = 1)

        deleteFieldBtn = Button(window, text = 'Delete Field', command = deleteRows)
        deleteFieldBtn.grid(column = 2, row = 0)
        deleteFieldBtn.configure(takefocus = 0) 

        fieldButton.grid(column= 2, row = i + 3, pady = 3, padx = 3)
         
        buttonList.append(fieldButton.cget('text'))

        entryList.append(entryPoint) 
 
    window.mainloop()
            
createType()