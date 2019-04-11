from faker import Faker
from pydbgen import pydbgen
import pandas
from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
import os
import random
import openpyxl

class TestDataGen(Frame):

    newMenuList = ['Select','ssn', 'name','country', 'date', 'company','state','city', 'real_(US)_cities',
    'US_state', 'zipcode', 'latitude', 'longitude','Month', 'weekday', 'year', 'time', 'date',  
    'Personal_email', 'official_email', 'Job_title', 'phone_number', 'license_plate']
    
    menuList = ['ssn', 'name', 'country', 'date', 'company']

    categoriesList = ['Categories', 'Personal', 'Geographic', 'Address']

    buttonList = []

    entryList = []

    buttonListVals = []  

    entryListVals = []

    gridList = []
    
    dropDownVals = []

    dropDownValsUpdate = []

    myDB = pydbgen.pydb()

    def __init__(self, master=None):
        Frame.__init__(self,master)
        self.master = master
        self.init_window()

    def init_window(self):
        self.master.title("Test Data Generator")
        self.master.config(background = 'light blue')
        self.master.geometry('420x400+0+0')

        self.master.lbl1 = Label(self.master, text='Field Types')
        self.master.lbl1.grid(column=2, row=2, pady=10, padx = 15)
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

        # self.master.dataBtn = Button(self.master, text = 'Generate', command = self.buttonClick)
        # self.master.dataBtn.grid(column = 2, row = 0, pady = 5, padx = 5, sticky = NSEW) 
        # self.master.dataBtn.configure(takefocus = 0)          

        self.master.listLen = len(TestDataGen.menuList)

        for i in range(self.master.listLen):
                    
            self.master.entryPoint = Entry(self.master, width = 13)
            self.master.entryPoint.grid(column = 0, row = i + 3, pady = 3, padx = 3)
            self.master.entryPoint.configure(takefocus = 1)

            self.master.dataBtn = Button(self.master, text = 'Generate', command = self.buttonClick)
            self.master.dataBtn.grid(column = 2, row = 0, pady = 5, padx = 5) 
            self.master.dataBtn.configure(takefocus = 0)     

            self.master.addFieldBtn = Button(self.master, text = 'Add Field', command = self.addRow)   
            self.master.addFieldBtn.configure(takefocus = 0)
            self.master.addFieldBtn.grid(column = 2, row = 1)

            self.master.destroyRow = Button(self.master, text = 'X', command = self.deleteRows)
            self.master.destroyRow.config(width = 2)
            self.master.destroyRow.grid(column = 3, row =  i + 3) 
            self.master.destroyRow.configure(takefocus = 0)           

            self.master.cat1 = StringVar(self.master)
            self.master.cat1.set("Categories")
            self.master.dropDownCat = OptionMenu(self.master, self.master.cat1, '', TestDataGen.categoriesList[0], TestDataGen.categoriesList[1], TestDataGen.categoriesList[2], TestDataGen.categoriesList[3])
            self.master.dropDownCat.grid(column = 1, row = i + 3)
            self.master.dropDownCat.configure(takefocus = 0)

            self.master.fieldButtonVar = StringVar(self.master)
            self.master.fieldButtonVar.set(TestDataGen.newMenuList[0])
            self.master.fieldButton = OptionMenu(self.master, self.master.fieldButtonVar, '',  TestDataGen.newMenuList[0], TestDataGen.newMenuList[1], TestDataGen.newMenuList[2], TestDataGen.newMenuList[3], TestDataGen.newMenuList[4], TestDataGen.newMenuList[5], TestDataGen.newMenuList[6], TestDataGen.newMenuList[7], TestDataGen.newMenuList[8], TestDataGen.newMenuList[9], TestDataGen.newMenuList[10], TestDataGen.newMenuList[11], TestDataGen.newMenuList[12], TestDataGen.newMenuList[13], TestDataGen.newMenuList[14], TestDataGen.newMenuList[15], TestDataGen.newMenuList[16], TestDataGen.newMenuList[17], TestDataGen.newMenuList[18], TestDataGen.newMenuList[19], TestDataGen.newMenuList[20], TestDataGen.newMenuList[21])
            self.master.fieldButton.grid(column = 2, row = i + 3, pady = 3, padx = 3)
            self.master.fieldButton.configure(takefocus = 0)

            TestDataGen.dropDownVals.append(self.master.fieldButtonVar)
            TestDataGen.entryList.append(self.master.entryPoint) 

        self.master.mainloop

    def addRow(self):

        self.master.fieldButtonVarAdd = StringVar(self.master)
        self.master.fieldButtonVarAdd.set(TestDataGen.newMenuList [0])
        self.master.fieldButtonAdd = OptionMenu(self.master, self.master.fieldButtonVarAdd, '', TestDataGen.newMenuList[0], TestDataGen.newMenuList[1], TestDataGen.newMenuList[2], TestDataGen.newMenuList[3], TestDataGen.newMenuList[4], TestDataGen.newMenuList[5], TestDataGen.newMenuList[6], TestDataGen.newMenuList[7], TestDataGen.newMenuList[8], TestDataGen.newMenuList[9], TestDataGen.newMenuList[10], TestDataGen.newMenuList[11], TestDataGen.newMenuList[12], TestDataGen.newMenuList[13], TestDataGen.newMenuList[14], TestDataGen.newMenuList[15], TestDataGen.newMenuList[16], TestDataGen.newMenuList[17], TestDataGen.newMenuList[18], TestDataGen.newMenuList[19], TestDataGen.newMenuList[20], TestDataGen.newMenuList[21] )

        self.master.entryPointadd = Entry(self.master, width = 13)
        self.master.entryPointadd.grid(column = 0, row = self.master.grid_size()[1], pady = 3, padx = 3)

        self.master.fieldButtonAdd.grid(column= 2, row = self.master.grid_size()[1] - 1, pady = 3, padx = 3)
        self.master.fieldButtonAdd.configure(takefocus = 0) 

        self.master.cat1Add = StringVar(self.master)
        self.master.cat1Add.set("Categories")
        self.master.dropDownCatAdd = OptionMenu(self.master, self.master.cat1Add, '', TestDataGen.categoriesList[0], TestDataGen.categoriesList[1], TestDataGen.categoriesList[2], TestDataGen.categoriesList[3] )
        self.master.dropDownCatAdd.grid(column = 1, row =self.master.grid_size()[1] - 1)
        self.master.dropDownCatAdd.configure(takefocus = 0)


        self.master.destroyRow = Button(self.master, text = 'X')
        self.master.destroyRow.config(width = 2)
        self.master.destroyRow.grid(column = 3, row =  self.master.grid_size()[1] - 1) 
        self.master.destroyRow.configure(takefocus = 0)  

        TestDataGen.entryList.append(self.master.entryPointadd)   
        TestDataGen.dropDownVals.append(self.master.fieldButtonVarAdd)

    def buttonClick(self):
        try:
            if self.master.entRows.get() == '':
                messagebox.showerror(title = 'Error', message = 'Please enter number of rows.')

            elif not (1 <= int(self.master.entRows.get()) <= 1000000):
                messagebox.showerror(title = 'Error', message = 'Please enter a number between 1 and 1,000,000 for number of rows.')

            elif self.master.entryPoint.get() == '':
                messagebox.showerror(title = 'Error', message = 'Please enter field names for all fields.')

            # elif self.master.entryPointAdd.get() == '':
            #     messagebox.showerror(title = 'Error', message = 'Please enter field names for all fields.')                This Don't Work

            elif len(self.master.entryPoint.get()) > 20:
                messagebox.showerror(title = 'Error', message = 'Max 20 characters allowed.')

            elif self.master.fieldButtonVar.get() == 'Select':
                messagebox.showerror(title = 'Error', message = 'Please choose field types for all option menus.')

            # elif self.master.fieldButtonVarAdd.get() == 'Select':
            #     messagebox.showerror(title = 'Error', message = 'Please choose field types for all option menus.')        This Don't Work

            else:
                self.r = Tk()    
                self.master.entRowsvalue = self.master.entRows.get()

                for entry in TestDataGen.entryList:
                    TestDataGen.entryListVals.append(entry.get())
                print(TestDataGen.entryListVals)

                for value in TestDataGen.dropDownVals:
                    TestDataGen.dropDownValsUpdate.append(value.get())
                print(TestDataGen.dropDownValsUpdate)
                    
                self.master.dataFrameGen = self.myDB.gen_dataframe(int(self.master.entRowsvalue), fields = TestDataGen.dropDownValsUpdate)      
                                    
                for i in range(len(TestDataGen.dropDownVals)):
                    self.master.dataFrameGen.rename(columns = {TestDataGen.dropDownValsUpdate[i] : TestDataGen.entryListVals[i]}, inplace = True)
                    print(TestDataGen.dropDownValsUpdate)
                    print(TestDataGen.entryListVals)

                self.master.datagenlabel = Label(self.r, text = self.master.dataFrameGen)
                self.master.datagenlabel.grid(column = 0) 
                self.master.dataFrameGen.to_excel('excel_test.xlsx', sheet_name = 'data')
                TestDataGen.dropDownValsUpdate.clear()
                TestDataGen.entryListVals.clear()             
                self.r.mainloop()
        
        except ValueError:
            messagebox.showerror(title = 'Error', message = 'Please enter a number between 1 and 1,000,000 for number or rows.')
    
    def deleteRows(self):
        if self.master.destroyRow.grid_size()[1] == self.master.destroyRow.grid_size()[1]:
            self.master.destroyRow.grid_size()[1].destroy()
        TestDataGen.buttonList.pop()
        TestDataGen.entryList.pop()
        
        print(TestDataGen.gridList)
        print(TestDataGen.buttonList)
        print(TestDataGen.entryList.pop)

        self.master.mainloop()


root = Tk()
gui = TestDataGen(root)
root.resizable(0, 0)
root.mainloop()

