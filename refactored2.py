#from faker import Faker
from pydbgen import pydbgen
import pandas
from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
import os
import random
import openpyxl

myDB = pydbgen.pydb()


class TestDataGen(Frame):
    newMenuList = ['ssn', 'name','country', 'date', 'company','state','city', 'real_(US)_cities',
    'US_state', 'zipcode', 'latitude', 'longitude','Month', 'weekday', 'year', 'time', 'date',  
    'Personal_email', 'official_email', 'Job_title', 'phone_number', 'license_plate']
    buttonList = []
    entryList = []
    buttonListVals = []    
    entryListVals =[]

    def __init__(self, master=None):
        Frame.__init__(self,master)
        self.master = master
        self.init_window()

    def init_window(self):
        self.master.title("Test Data Generator")
        self.master.config(background = 'light blue')
        self.master.geometry('450x400+0+0')

        lbl1 = Label(self.master, text='Field Types') #basic grid label
        lbl1.grid(column=2, row=2, pady=10, padx = 20)
        lbl1.config(font=("Hevetica", 15), background = 'light blue')

        lbl = Label(self.master, text='Field Names') #basic grid label
        lbl.grid(column=0, row=2)
        lbl.grid_columnconfigure((0,1,2), weight = 1)
        lbl.config(font=("helvetica", 15), background = 'light blue')

        entRows = Entry(self.master, width = 13)
        entRows.grid (column = 1, row = 1)
        entRows.focus_set()

        lblRows = Label(self.master, text = 'Number of rows:')
        lblRows.grid(column = 0, row=1,  pady=5, padx = 20)
        lblRows.config(font=("Helvetica", 15), background = 'light blue')


        addRowButton = Button(self.master, text = 'Add Row', command = self.generateData)
        addRowButton.grid(column = 2, row = 8)        
        
        self.master.entry1 = Entry(self.master, width = 13)
        self.master.entry1.grid(column = 0, row = 3, pady = 5)

        self.master.entry2 = Entry(self.master, width = 13)
        self.master.entry2.grid(column = 0, row = 4, pady = 5)

        button1 = Button(self.master, text = '', command = self.buttonChange)
        button1.grid(column = 2, row = 3, pady = 5)

        button2 = Button(self.master, text = '', command = self.buttonChange)
        button2.grid(column = 2, row = 4, pady = 5)
          

        dataBtn = Button(self.master, text='Generate Data', command= self.entryListAppend)
        dataBtn.grid(column = 1, row = 8, pady = 5, padx = 5, sticky = NSEW) 
        dataBtn.configure(takefocus = 0) 
    
 
    
    def buttonChange(self):
        buttonMenu = Tk()
        buttonMenu.title('Button Menu')

        buttonMenu.mainloop()

    def entryListAppend(self):
        TestDataGen.entryList.append(self.master.entry1.get())
        TestDataGen.entryList.append(self.master.entry2.get())
        
        print(TestDataGen.entryList)

    def generateData(self):
        generateWindow = Tk()

           
root = Tk()
gui = TestDataGen(root)
root.mainloop()
