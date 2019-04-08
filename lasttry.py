
#from faker import Faker
from pydbgen import pydbgen
import pandas
from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
import os
import random
import openpyxl
 

class TestDataGen(Frame):
    newMenuList = ['ssn', 'name','country', 'date', 'company','state','city', 'real_(US)_cities',
    'US_state', 'zipcode', 'latitude', 'longitude','Month', 'weekday', 'year', 'time', 'date', 
    'Personal_email', 'official_email', 'Job_title', 'phone_number', 'license_plate']

    buttonList = []
    entryList = []
    buttonListVals = []   
    entryListVals =[]
    
    curRow = 2
    totRows = 0

    myDB = pydbgen.pydb()

    def __init__(self, master=None):
        Frame.__init__(self,master)
        self.master = master
        self.init_window()

    def init_window(self):
        self.master.title("Test Data Generator")
        self.master.config(background = 'light blue')
        self.master.geometry('400x400+0+0')

        self.master.lbl1 = Label(self.master, text='Field Types') #basic grid label
        self.master.lbl1.grid(column=2, row=2, pady=10, padx = 5)
        self.master.lbl1.config(font=("Hevetica", 15), background = 'light blue')

        self.master.lbl = Label(self.master, text='Field Names') #basic grid label
        self.master.lbl.grid(column=0, row=2, padx = 20)
        self.master.lbl.grid_columnconfigure((0,1,2), weight = 1)
        self.master.lbl.config(font=("helvetica", 15), background = 'light blue') 

        self.master.entRows = Entry(self.master, width = 8)
        self.master.entRows.grid (column = 1, row = 1)
        self.master.entRows.focus_set()
        self.master.lblRows = Label(self.master, text = 'Number of rows:')
        self.master.lblRows.grid(column = 0, row=1,  pady=5, padx = 5)
        self.master.lblRows.config(font=("Helvetica", 15), background = 'light blue')
 
        self.master.addRowButton = Button(self.master, text = 'Add Row', command = self.addEntryandButton)
        self.master.addRowButton.grid(column = 2, row = TestDataGen.curRow + 2)
        self.master.addRowButton.configure(takefocus = 0)
       
        self.master.destroyRow = Button(self.master, text = 'X', command = self.destroyButtonRow )
        self.master.destroyRow.config(width = 2)
        self.master.destroyRow.grid(column=3, row = TestDataGen.curRow + 1)

        self.master.entry1 = Entry(self.master, width = 13)
        self.master.entry1.grid(column = 0, row = TestDataGen.curRow + 1, pady = 5)
        self.master.entry1.configure(takefocus = 1)
 
        self.master.button1 = Button(self.master, text = TestDataGen.newMenuList[0], command = self.buttonChange)
        self.master.button1.grid(column = 2, row = TestDataGen.curRow + 1, pady = 5)
        self.master.button1.configure(takefocus = 0)

        self.master.dataBtn = Button(self.master, text='Generate Data', command = self.entryAndButtonListAppend)
        self.master.dataBtn.grid(column = 1, row = TestDataGen.curRow + 2, pady = 5, padx = 5, sticky = NSEW)
        self.master.dataBtn.configure(takefocus = 0)
    

    def buttonChange(self):
        buttonMenu = Tk()
        buttonMenu.title('Button Menu')
        buttonMenu.mainloop() 

    def entryAndButtonListAppend(self):
        TestDataGen.entryList.append(self.master.entry1.get())
        TestDataGen.buttonList.append(self.master.button1.cget('text'))

        print(self.master.entRows.get())
        print(TestDataGen.buttonList)
        print(TestDataGen.entryList)

       # TestDataGen.entryList.clear()
       # TestDataGen.buttonList.clear()

 
    def destroyButtonRow(self):
        self.master.entry1.destroy()
        self.master.button1.destroy()
        self.master.destroyRow.destroy()


    def generateData(self):
        generateWindow = Tk()

 
    def addEntryandButton(self):
        """Increment current row pointer"""
        TestDataGen.curRow = TestDataGen.curRow + 1

        """Destroy the Generate and AddRow buttons at the current position"""
        self.master.addRowButton.destroy()
        self.master.dataBtn.destroy()

        """Move the Generate and AddRow buttons down to add a new row on GUI window"""
        self.master.addRowButton = Button(self.master, text='Add Row', command=self.addEntryandButton)
        self.master.addRowButton.grid(column=2, row=TestDataGen.curRow + 2)
        self.master.addRowButton.configure(takefocus=0)

        self.master.dataBtn = Button(self.master, text='Generate Data', command=self.entryAndButtonListAppend)
        self.master.dataBtn.grid(column=1, row=TestDataGen.curRow + 2, pady=5, padx=5, sticky=NSEW)
        self.master.dataBtn.configure(takefocus=0)

        """Add the new row widgets"""
        # self.buttonVar = Button(self.master, text = 'ssn')
        # self.buttonVar.grid(column = 2, row = TestDataGen.curRow)
        # TestDataGen.buttonList.append(self.buttonVar.cget('text'))

        self.master.destroyRow = Button(self.master, text='X', command=self.destroyButtonRow)
        self.master.destroyRow.config(width=2)
        self.master.destroyRow.grid(column=3, row=TestDataGen.curRow + 1)

        self.master.entry1 = Entry(self.master, width=13)
        self.master.entry1.grid(column=0, row=TestDataGen.curRow + 1, pady=5)
        self.master.entry1.configure(takefocus=1)
        TestDataGen.entryList.append(self.master.entry1.get())

        self.master.button1 = Button(self.master, text=TestDataGen.newMenuList[0], command=self.buttonChange)
        self.master.button1.grid(column=2, row=TestDataGen.curRow + 1, pady=5)
        self.master.button1.configure(takefocus=0)
        TestDataGen.buttonList.append(self.master.button1.cget('text'))
        print(TestDataGen.buttonList)
        # print(self.buttonVar)
 
# def generateData():
#container class for buttons   
# class buttons():
#     def __init__(self, buttonListAct):
#         self.buttonListAct = []
#         self.button =  buttons
#     def addButton(self, button):
#         self.buttonListAct.append(button)

#button class
# class button():
#     Button(TestDataGen, text = TestDataGen.newMenuList, command = buttons.addButton)

 
root = Tk()
gui = TestDataGen(root)
root.resizable(0, 0)
root.mainloop()

 
