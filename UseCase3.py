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

global menuList 
global entryList
global buttonList
global newMenuList

menuList = ['ssn', 'name','country', 'date', 'company']

def createType():
    def buttonClick():
        r = Tk()
        entRowsvalue = entRows.get()

        dataFrameGen = myDB.gen_dataframe(int(entRowsvalue), fields = menuList)        
        for entry in entryList:
            entryListVals.append(entry.get())
        print(entryListVals)
        
        for value in buttonList:
            buttonListVals.append(value)
        print(buttonListVals)


        for i in range(len(menuList)):
            dataFrameGen.rename(columns = {menuList[i] : entryListVals[i]}, inplace = True)
        
        datagenlabel = Label(r, text = dataFrameGen)
        datagenlabel.grid(column=0, row=1) 
        dataFrameGen.to_excel('excel_test.xlsx', sheet_name = 'data')
       
        r.mainloop()
   

    
    def addRow():
        
        entryPoint = Entry(window, width = 15)
        fieldButton = Button(window, text = menuList[4], command = (otherTypes, buttonClick))       
        entryPoint.grid(column = 0, row = window.grid_size()[1], pady = 3, padx = 3)
        
        fieldButton.grid(column= 2, row = window.grid_size()[1] - 1, pady = 3, padx = 3)
        fieldButton.configure(takefocus = 0)    

        buttonList.append(fieldButton.cget('text'))
        entryList.append(entryPoint)
        window.mainloop()
             
    def otherTypes():
        newMenuList = []
        window2 = Tk()
        
        for i in range(len(menuList)):
            global fakerButton
            fakerButton = Button(window2, text = menuList[i], command = createType)
            fakerButton.grid(column = i + 1, row = 1)
            newMenuList.append(fakerButton.cget('text'))
            print(newMenuList)


    #window Config
    window = Tk()
    window.title("Test Data Gen")
    window.config(background = 'light blue')
    window.geometry('500x920+0+0')

    lbl1 = Label(window, text='Type') #basic grid label
    lbl1.grid(column=2, row=2, pady=10)
    
    lbl = Label(window, text='Field Name') #basic grid label
    lbl.grid(column=0, row=2)
    lbl.grid_columnconfigure((0,1,2), weight = 1)
    entRows = Entry(window, width = 8)
    entRows.grid (column = 1, row = 1)
    
    lblRows = Label(window, text = 'Number of rows: ', width = 15)
    lblRows.grid(column = 0, row=1,  pady=50, padx = 5)
    
    dataBtn = Button(window, text='Generate Data', command=buttonClick)
    dataBtn.grid(column = 1, row = 0, pady = 5, padx = 5, sticky = NSEW) 
    dataBtn.configure(takefocus = 0)    
    
    #addFieldBtn = Button(window, text = 'Add Field', command = addRow)
    #addFieldBtn.grid(column = 2, row = 8)
    
    #One way to move the buttons down the the grid would be to window.grid_size()[1] - 1 in someway too
    #Lists
    
    listLen = len(menuList)

    buttonList = []
    
    buttonListVals = []
    
    entryList = []
    
    entryListVals =[]

    for i in range(listLen):

        entryPoint = Entry(window, width = 15)
        
        entryPoint.grid(column = 0, row = i + 3, pady = 3, padx = 3)
        entryPoint.configure(takefocus = 1)
        
        fieldButton = Button(window, text = menuList[i], command = otherTypes)
        fieldButton.configure(takefocus = 0)
        
        addFieldBtn = Button(window, text = 'Add Field', command = addRow)   
        addFieldBtn.configure(takefocus = 0)
        addFieldBtn.grid(column = 2, row = 1)
        
        fieldButton.grid(column= 2, row = i + 3, pady = 3, padx = 3)
         
        buttonList.append(fieldButton.cget('text'))

        entryList.append(entryPoint) 
           
    window.mainloop()        
    
createType()