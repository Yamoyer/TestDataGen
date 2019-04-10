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
    menuList = ['ssn', 'name', 'country', 'date', 'company']
    buttonList = []
    entryList = []
    newMenuList = []
    buttonListVals = []    
    entryListVals = []
    gridList = []
    myDB = pydbgen.pydb()
    

    def __init__(self, master=None):
        Frame.__init__(self,master)
        self.master = master
        self.init_window()

    def init_window(self):
        self.master.title("Test Data Generator")
        self.master.config(background = 'light blue')
        self.master.geometry('400x400+0+0')

        self.master.lbl1 = Label(self.master, text='Field Types')
        self.master.lbl1.grid(column=2, row=2, pady=10, padx = 5)
        self.master.lbl1.config(font=("Hevetica", 15), background = 'light blue')

        self.master.lbl = Label(self.master, text='Field Names')
        self.master.lbl.grid(column=0, row=2, padx = 20)
        self.master.lbl.grid_columnconfigure((0,1,2), weight = 1)
        self.master.lbl.config(font=("helvetica", 15), background = 'light blue')

        self.master.entRows = Entry(self.master, width = 8)
        self.master.entRows.grid (column = 1, row = 1)
        self.master.entRows.focus_set()

        self.master.lblRows = Label(self.master, text = 'Number of rows:')
        self.master.lblRows.grid(column = 0, row=1,  pady=5, padx = 5)
        self.master.lblRows.config(font=("Helvetica", 15), background = 'light blue')

        self.master.dataBtn = Button(self.master, text = 'Generate Data', command = self.buttonClick)
        self.master.dataBtn.grid(column = 1, row = 0, pady = 5, padx = 5, sticky = NSEW) 
        self.master.dataBtn.configure(takefocus = 0)          

        self.master.listLen = len(TestDataGen.menuList)

        for i in range(self.master.listLen):
            
            self.master.entryPoint = Entry(self.master, width = 15)

            self.master.entryPoint.grid(column = 0, row = i + 3, pady = 3, padx = 3)
            self.master.entryPoint.configure(takefocus = 1)
            
            self.master.fieldButton = Button(self.master, text = TestDataGen.menuList[i], command = self.otherTypes)
            self.master.fieldButton.configure(takefocus = 0)
                
            self.master.addFieldBtn = Button(self.master, text = 'Add Field', command = self.addRow)   
            self.master.addFieldBtn.configure(takefocus = 0)
            self.master.addFieldBtn.grid(column = 2, row = 1)

            self.master.deleteFieldBtn = Button(self.master, text = 'Delete Field', command = self.deleteRows)
            self.master.deleteFieldBtn.grid(column = 2, row = 0)
            self.master.deleteFieldBtn.configure(takefocus = 0) 

            self.master.fieldButton.grid(column= 2, row = i + 3, pady = 3, padx = 3)
            
            TestDataGen.buttonList.append(self.master.fieldButton.cget('text'))

            TestDataGen.entryList.append(self.master.entryPoint) 

    def addRow(self):

        for i in range(len(TestDataGen.newMenuList)):
            self.master.fieldButton = Button(self.master, text = TestDataGen.newMenuList[i], command = self.otherTypes)
            entryPointadd = Entry(self.master, width = 15)

        entryPointadd.grid(column = 0, row = self.master.gridsize()[1], pady = 3, padx = 3)

        fieldButton.grid(column= 2, row = self.master.grid_size()[1] - 1, pady = 3, padx = 3)
        fieldButton.configure(takefocus = 0) 

        TestDataGen.entryList.insert(len(TestDataGen.entryList) + 1, self.master.entryPointadd)   
        TestDataGen.buttonList.insert(len(TestDataGen.buttonList) + 1, self.master.fieldButton.cget("text"))

        print(TestDataGen.buttonList)

    def buttonClick(self):
        try:
            if self.master.entRows.get() == '':
                self.master.messagebox.showerror(title = 'Error', message = 'Please enter number of rows.')

            elif not (1 <= int(self.master.entRows.get()) <= 1000000):
                self.master.messagebox.showerror(title = 'Error', message = 'Please enter a number between 1 and 1,000,000 for number of rows.')

            elif self.master.entryPoint.get() == '':
                self.master.messagebox.showerror(title = 'Error', message = 'Please enter field names for all fields.')

            elif len(self.master.entryPoint.get()) > 20:
                self.master.messagebox.showerror(title = 'Error', message = 'Max 20 characters allowed.')

            else:
                self.r = Tk()    
                self.master.entRowsvalue = self.master.entRows.get()
                 
                for entry in TestDataGen.entryList:
                    TestDataGen.entryListVals.append(self.master.entry.get())
                print(TestDataGen.entryListVals)
                
                for value in TestDataGen.buttonList:
                    TestDataGen.buttonListVals.append(value)
                print(TestDataGen.buttonListVals)
                    
                self.dataFrameGen = self.myDB.gen_dataframe(int(self.master.entRowsvalue), fields = TestDataGen.buttonListVals)      
                
                for i in range(len(TestDataGen.buttonListVals)):
                    self.dataFrameGen.rename(columns = {TestDataGen.buttonListVals[i] : TestDataGen.entryListVals[i]}, inplace = True)
                    print(TestDataGen.buttonListVals)
                    print(TestDataGen.entryListVals)

                datagenlabel = Label(self.r, text = self.dataFrameGen)
                datagenlabel.grid(column=0) 
                self.dataFrameGen.to_excel('excel_test.xlsx', sheet_name = 'data') 
                TestDataGen.buttonListVals.clear()
                TestDataGen.entryListVals.clear()             
                self.r.mainloop()
        
        except ValueError:
            messagebox.showerror(title = 'Error', message = 'Please enter a number between 1 and 1,000,000 for number or rows.')
    
    def deleteRows(self):
        self.gridList = self.master.gridsize()
        for row in range(len(TestDataGen.gridList)):
            row.destroyButton.destroy()

            TestDataGen.buttonList.pop()
            TestDataGen.entryList.pop()
        
        print(TestDataGen.gridList)
        print(TestDataGen.buttonList)
        print(TestDataGen.entryList.pop)

        self.master.mainloop()

    def otherTypes(self):
        
        self.window2 = Tk()

        for i in range(len(TestDataGen.newMenuList)):
            self.master.fakerButton = Button(self.window2, text = TestDataGen.newMenuList[i], width = 20)
            self.master.fakerButton.pack()

            print(TestDataGen.newMenuList)
root = Tk()
gui = TestDataGen(root)
root.resizable(0, 0)
root.mainloop()