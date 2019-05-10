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

    # Populated Lists

    newMenuList = ['Select','ssn', 'name','country', 'date', 'company','state','city', 'real_city', 'zipcode', 'latitude', 'longitude','name_month', 'weekday', 'year', 'time', 'date', 'email', 'phone_number_simple', 'license_plate','random_int']
    
    personalList =  ['Select', 'ssn', 'name', 'email', 'phone_number_simple', 'company', 'license_plate']

    geographicList = ['Select','country', 'state', 'city', 'real_city', 'zipcode', 'latitude', 'longitude']

    dateList = ['Select','name_month', 'weekday', 'year', 'time', 'date']

    menuList = ['ssn', 'name', 'country', 'date', 'company']
    
    numberList = ['random_int']

    categoriesList = ['Categories', 'Personal', 'Geographic', 'Date','Menu','Number']

    # Values Lists

    entryListInput = []

    entryListVals = []

    rowList = []

    dropDownVals = []

    dropDownValsUpdate = []
    
    MaxList = []
    
    MinList = []
    
    # Widgets Lists

    dropDownCatWidgList = []
    
    entryListWidgets = []
    
    deleteButtonWidgList = []
    
    fieldDDWidgList = []

    widgetRowsList = []

    myDB = pydbgen.pydb()

    def __init__(self, master=None):
        Frame.__init__(self,master)
        self.master = master
        self.init_window()

    def init_window(self):
        self.master.title("Test Data Generator")
        self.master.config(background = 'light blue')
        self.master.geometry('900x600+0+0')

        self.master.lbl1 = Label(self.master, text='Field Types')
        self.master.lbl1.grid(column=2, row=2, pady=10, padx = 30)
        self.master.lbl1.config(font=("Hevetica", 15), background = 'light blue')
        
        self.master.lbl1 = Label(self.master, text='Min')
        self.master.lbl1.grid(column=3, row=2, pady=10, padx = 30)
        self.master.lbl1.config(font=("Hevetica", 15), background = 'light blue')
        
        self.master.lbl1 = Label(self.master, text='Max')
        self.master.lbl1.grid(column=4, row=2, pady=10, padx = 30)
        self.master.lbl1.config(font=("Hevetica", 15), background = 'light blue')

        self.master.lbl = Label(self.master, text='Field Names')
        self.master.lbl.grid(column=0, row=2, padx = 40)
        self.master.lbl.grid_columnconfigure((0,1,2), weight = 1)
        self.master.lbl.config(font=("helvetica", 15), background = 'light blue')

        self.master.entRows = Entry(self.master, width = 8)
        self.master.entRows.grid (column = 1, row = 1)
        self.master.entRows.focus_set()

        self.master.lblRows = Label(self.master, text = 'Number of rows:')
        self.master.lblRows.grid(column = 0, row=1,  pady=5, padx = 5)
        self.master.lblRows.config(font=("Helvetica", 15), background = 'light blue')

        self.master.listLen = len(TestDataGen.menuList)
        
        c = 0

        while c <= 4:

            c += 1  
            
            self.master.Max = Entry(self.master, width = 7)
            self.master.Max.grid(column = 4, row = c + 3, pady = 3, padx = 3)
            self.master.Max.configure(takefocus = 0)
            #self.master.Max.set(4)
            
            self.master.Min = Entry(self.master, width = 7)
            self.master.Min.grid(column = 3, row = c + 3, pady = 3, padx = 3)
            self.master.Min.configure(takefocus = 0)
            
            self.master.entryPoint = Entry(self.master, width = 13)
            self.master.entryPoint.grid(column = 0, row = c + 3, pady = 3, padx = 3)
            self.master.entryPoint.configure(takefocus = 1)

            self.master.dataBtn = Button(self.master, text = 'Generate', command = self.buttonClick)
            self.master.dataBtn.grid(column = 2, row = 0, pady = 5, padx = 5) 
            self.master.dataBtn.configure(takefocus = 0)     

            self.master.addFieldBtn = Button(self.master, text = 'Add Field', command = self.addRow)   
            self.master.addFieldBtn.configure(takefocus = 0)
            self.master.addFieldBtn.grid(column = 2, row = 1)

            self.master.destroyRowButton = Button(self.master, text = 'X', command = self.deleteRows)  # How do I get the specific button that I clicked?
            self.master.destroyRowButton.config(width = 2)
            self.master.destroyRowButton.grid(column = 5, row =  c + 3) 
            self.master.destroyRowButton.configure(takefocus = 0)
            #self.master.destroyRowButton.config(command = lambda: self.deleteRows(c-1))            

            TestDataGen.rowList.append(self.master.destroyRowButton.grid_info()['row'])

            print(TestDataGen.rowList)

            self.master.cat1 = StringVar(self.master)
            self.master.cat1.set("Categories")
            self.master.dropDownCat = OptionMenu(self.master, self.master.cat1, '', TestDataGen.categoriesList[0], TestDataGen.categoriesList[1], TestDataGen.categoriesList[2], TestDataGen.categoriesList[3],TestDataGen.categoriesList[4],TestDataGen.categoriesList[5])
            self.master.dropDownCat.grid(column = 1, row = c + 3,sticky="ew")
            self.master.dropDownCat.configure(takefocus = 0)

            self.master.fieldDropDVar = StringVar(self.master)
            self.master.fieldDropDVar.set(TestDataGen.newMenuList[0])
            self.master.fieldDD = OptionMenu(self.master, self.master.fieldDropDVar, '',  TestDataGen.newMenuList[0],TestDataGen.newMenuList[1], TestDataGen.newMenuList[2], TestDataGen.newMenuList[3], TestDataGen.newMenuList[4], TestDataGen.newMenuList[5], TestDataGen.newMenuList[6], TestDataGen.newMenuList[7], TestDataGen.newMenuList[8], TestDataGen.newMenuList[9], TestDataGen.newMenuList[10], TestDataGen.newMenuList[11], TestDataGen.newMenuList[12], TestDataGen.newMenuList[13], TestDataGen.newMenuList[14], TestDataGen.newMenuList[15], TestDataGen.newMenuList[16], TestDataGen.newMenuList[17], TestDataGen.newMenuList[18], TestDataGen.newMenuList[19],TestDataGen.newMenuList[20])
            self.master.fieldDD.grid(column = 2, row = c + 3, pady = 3, padx = 3,sticky="ew")
            self.master.fieldDD.configure(takefocus = 0)
            
            # Value Appends

            TestDataGen.dropDownVals.append(self.master.fieldDropDVar)
            TestDataGen.entryListInput.append(self.master.entryPoint)
            TestDataGen.MaxList.append(self.master.Max)
            TestDataGen.MinList.append(self.master.Min)

            # Widget Appends

            TestDataGen.dropDownCatWidgList.append(self.master.dropDownCat)
            TestDataGen.fieldDDWidgList.append(self.master.fieldDD)
            TestDataGen.entryListWidgets.append(self.master.entryPoint)
            TestDataGen.deleteButtonWidgList.append(self.master.destroyRowButton)

        self.master.mainloop
        
        

    def addRow(self):
        print(self.master.Max.get())
        print(self.master.Min.get())
        self.master.fieldDropDVarAdd = StringVar(self.master)
        self.master.fieldDropDVarAdd.set(TestDataGen.newMenuList [0])
        self.master.fieldDDAdd = OptionMenu(self.master, self.master.fieldDropDVarAdd, '', TestDataGen.newMenuList[0], TestDataGen.newMenuList[1], TestDataGen.newMenuList[2], TestDataGen.newMenuList[3], TestDataGen.newMenuList[4], TestDataGen.newMenuList[5], TestDataGen.newMenuList[6], TestDataGen.newMenuList[7], TestDataGen.newMenuList[8], TestDataGen.newMenuList[9], TestDataGen.newMenuList[10], TestDataGen.newMenuList[11], TestDataGen.newMenuList[12], TestDataGen.newMenuList[13], TestDataGen.newMenuList[14], TestDataGen.newMenuList[15], TestDataGen.newMenuList[16], TestDataGen.newMenuList[17], TestDataGen.newMenuList[18], TestDataGen.newMenuList[19],TestDataGen.newMenuList[20])

        self.master.entryPointAdd = Entry(self.master, width = 13)
        self.master.entryPointAdd.grid(column = 0, row = self.master.grid_size()[1], pady = 3, padx = 3)
        
        self.master.MaxAdd = Entry(self.master, width = 7)
        self.master.MaxAdd.grid(column = 4, row = self.master.grid_size()[1] - 1, pady = 3, padx = 3)
        
        self.master.MinAdd = Entry(self.master, width = 7)
        self.master.MinAdd.grid(column = 3, row = self.master.grid_size()[1] - 1, pady = 3, padx = 3)        
        
        self.master.fieldDDAdd.grid(column= 2, row = self.master.grid_size()[1] - 1, pady = 3, padx = 3,sticky="ew")
        self.master.fieldDDAdd.configure(takefocus = 0) 

        self.master.cat1Add = StringVar(self.master)
        self.master.cat1Add.set("Categories")
        self.master.dropDownCatAdd = OptionMenu(self.master, self.master.cat1Add, '', TestDataGen.categoriesList[0], TestDataGen.categoriesList[1], TestDataGen.categoriesList[2], TestDataGen.categoriesList[3] )
        self.master.dropDownCatAdd.grid(column = 1, row =self.master.grid_size()[1] - 1,sticky="ew")
        self.master.dropDownCatAdd.configure(takefocus = 0)

        self.master.destroyRowButtonAdd = Button(self.master, text = 'X', command = lambda: self.master.grid_size()[1][1].destroy())
        self.master.destroyRowButtonAdd.config(width = 2)
        self.master.destroyRowButtonAdd.grid(column = 5, row =  self.master.grid_size()[1] - 1) 
        self.master.destroyRowButtonAdd.configure(takefocus = 0)  

        # Added Value Appends

        TestDataGen.dropDownVals.append(self.master.fieldDropDVarAdd)
        TestDataGen.entryListInput.append(self.master.entryPointAdd)
        TestDataGen.MaxList.append(self.master.MaxAdd)
        TestDataGen.MinList.append(self.master.MinAdd)
        # Added Widget Appends
        
        TestDataGen.dropDownCatWidgList.append(self.master.dropDownCatAdd)
        TestDataGen.fieldDDWidgList.append(self.master.fieldDDAdd)
        TestDataGen.entryListWidgets.append(self.master.entryPointAdd)
        TestDataGen.deleteButtonWidgList.append(self.master.destroyRowButtonAdd)

    def buttonClick(self):

        try:
            if self.master.entRows.get() == '':
                messagebox.showerror(title = 'Error', message = 'Please enter number of rows.')

            elif not (1 <= int(self.master.entRows.get()) <= 1000000):
                messagebox.showerror(title = 'Error', message = 'Please enter a number between 1 and 1,000,000 for number of rows.')

            elif self.master.entryPoint.get() == '':
                messagebox.showerror(title = 'Error', message = 'Please enter field names for all fields.')

            # elif self.master.entryPointAdd.get() == '':
            #     messagebox.showerror(title = 'Error', message = 'Please enter field names for all fields.')        This Don't Work

            elif len(self.master.entryPoint.get()) > 20:
                messagebox.showerror(title = 'Error', message = 'Max 20 characters allowed.')

            elif self.master.fieldDropDVar.get() == 'Select':
                messagebox.showerror(title = 'Error', message = 'Please choose field types for all option menus.')
            
            #elif self.master.fieldDropDVar.get() == 'random_int':
             #   messagebox.showerror(title = 'Error', message = 'Please choose  all option menus.')

                
            # elif self.master.fieldDropDVarAdd.get() == 'Select':
            #     messagebox.showerror(title = 'Error', message = 'Please choose field types for all option menus.')        This Don't Work

            else:
                self.r = Tk()    
                self.master.entRowsvalue = self.master.entRows.get()

                for entry in TestDataGen.entryListInput:
                    TestDataGen.entryListVals.append(entry.get())

                for value in TestDataGen.dropDownVals:
                    TestDataGen.dropDownValsUpdate.append(value.get())
                    
                self.master.dataFrameGen = self.myDB.gen_dataframe(int(self.master.entRowsvalue), fields = TestDataGen.dropDownValsUpdate)      
                                    
                for i in range(len(TestDataGen.dropDownVals)):
                    self.master.dataFrameGen.rename(columns = {TestDataGen.dropDownValsUpdate[i] : TestDataGen.entryListVals[i]}, inplace = True)

                self.master.datagenlabel = Label(self.r, text = self.master.dataFrameGen)
                self.master.datagenlabel.grid(column = 0) 
                self.master.dataFrameGen.to_excel('excel_test.xlsx', sheet_name = 'data')

                TestDataGen.dropDownValsUpdate.clear()
                TestDataGen.entryListVals.clear()             
                self.r.mainloop()
        
        except ValueError:
            messagebox.showerror(title = 'Error', message = 'Please enter a number between 1 and 1,000,000 for number or rows.')
        
    def deleteRows(self):
        
        # d = -1
        # for c in range(0,len(TestDataGen.rowList)):
        #     print(str(TestDataGen.rowList[c]) +" "+str(rownum))
        #     if rownum == TestDataGen.rowList[c]:
        #         print(c)
        #         d = c
    
        for i in range(0, len(TestDataGen.deleteButtonWidgList)):

            if TestDataGen.deleteButtonWidgList[i] == TestDataGen.deleteButtonWidgList[-1]:
                print(self.master.destroyRowButton.grid_info()['row'])
                TestDataGen.deleteButtonWidgList[i].destroy()            
                TestDataGen.dropDownCatWidgList[i].destroy()
                TestDataGen.entryListWidgets[i].destroy()
                TestDataGen.fieldDDWidgList[i].destroy()
                
                #TestDataGen.rowList.pop()
                TestDataGen.deleteButtonWidgList.pop()
                TestDataGen.dropDownCatWidgList.pop()
                TestDataGen.entryListWidgets.pop()
                TestDataGen.fieldDDWidgList.pop()
            print(TestDataGen.deleteButtonWidgList)
root = Tk()
gui = TestDataGen(root)
root.resizable(0, 0)
root.mainloop()