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



global entryList
global buttonList
global newMenuList


menuList = ['ssn', 'name','country', 'date', 'company']

def createType():
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
                    """ dataFrameGen = myDB.gen_dataframe(int(entRowsvalue), fields=entryListVals) """
                
                for value in buttonList:
                    buttonListVals.append(value)
                    """ for i in range(len(entryList)):
                        dataFrameGen.rename(columns = {menuList[i] : entryListVals[i]}, inplace = True)
                        datagenlabel = Label(r, text = dataFrameGen)
                        print(datagenlabel)
                        datagenlabel.grid(column=0, row=1) """
                    canvas = Canvas(r)
                    canvas = Canvas(r, width=300, height=600, bg='#afeeee')
                    dafaFrameGen = myDB.gen_dataframe(100, ['ssn', 'name', 'country', 'date', 'company'])
                    canvas.create_text(0, 0, fill="darkblue", font="Times 12 italic bold", text=dafaFrameGen)
                    canvas.grid(column=0, row=0)
                    ys = Scrollbar(r, orient='vertical', command=canvas.yview)
                    ys.grid(row=0, column=70, sticky='NS')
                    # configure scrolling
                    canvas.configure(yscrollcommand=ys.set, scrollregion=canvas.bbox('all'))
                    # show bottom of canvas
                    canvas.yview_moveto(1)
                    xs = Scrollbar(r, orient='horizontal', command=canvas.xview)
                    xs.grid(row=50, column=0, sticky='WE')
                    # configure scrolling
                    canvas.configure(xscrollcommand=xs.set, scrollregion=canvas.bbox('all'))
                    # show bottom of canvas
                    canvas.xview_moveto(1)
                    
                    #dataFrameGen.to_excel('excel_test.xlsx', sheet_name = 'data') 
                    # *********** I still cant get this export to ecxel to work 

                    buttonListVals.clear()
                    entryListVals.clear()
                    r.update()
                    r.mainloop()
        except ValueError:
            messagebox.showerror(title = 'Error', message = 'Please enter a number between 1 and 1,000,000 for number of rows.')        

    def deleteRows():
        gridList = window.grid_size()
        cmbList = fldbuttonList.pop()
        eList = entryList.pop()

        cmbList.destroy()
        eList.destroy()
        entryListVals.clear()

        window.mainloop()
    
    def addRow():
        
        entryPointadd = Entry(window, width = 15)
        entryPointadd.grid(column = 0, row = window.grid_size()[1], pady = 3, padx = 3)
        entryList.append(entryPointadd)

        """ Combobox for the field types in the dropdown """
        cb = Combobox(window, values=menuList, state='readonly')
        cb.grid(column=2, row=window.grid_size()[1] - 1, pady=3, padx=3, sticky=E)
        cb.bind('<<ComboboxSelected>>', modified)
        fldbuttonList.append(cb)

        buttonListVals.append(cb.get())
        entryListVals.append(entryPointadd)

        window.mainloop()


    def otherTypes():
        newMenuList = []
        window2 = Tk()
        
        for i in range(len(menuList)):
            global fakerButton
            fakerButton = Button(window2, text = menuList[i], width = 20, command = createType)
            fakerButton.grid(column = i + 1, row = 1)
            newMenuList.append(fakerButton.cget('text'))

            print(buttonList)

    def modified(window, event):
        print(window.cb.get())

    #window Config
    window = Tk()
    window.title("Test Data Gen")
    window.config(background = 'light blue')
    window.geometry('460x920+0+0')

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
    lblRows.grid(column = 0, row=1,  pady=5, padx = 5)
    lblRows.config(font=("Helvetica", 15), background = 'light blue')
    
    dataBtn = Button(window, text='Generate Data', command=buttonClick)
    dataBtn.grid(column = 1, row = 0, pady = 5, padx = 5, sticky = NSEW) 
    dataBtn.configure(takefocus = 0)    

    listLen = len(menuList)

    buttonList = []
    
    buttonListVals = []
    
    entryList = []
    
    entryListVals =[]

    fldbuttonList=[]

    fldoptionList=[]

    for i in range(listLen):

        entryPoint = Entry(window, width = 15)
        entryPoint.grid(column = 0, row = i + 3, pady = 3, padx = 3)
        entryPoint.configure(takefocus = 1)
        
        cb = Combobox(window, values=menuList, state='readonly')
        cb.grid(column=2, row=window.grid_size()[1] - 1, pady=3, padx=3, sticky=E)
        cb.bind('<<ComboboxSelected>>', modified)
        fldbuttonList.append(cb)



        addFieldBtn = Button(window, text = 'Add Field', command = addRow)
        addFieldBtn.configure(takefocus = 0)
        addFieldBtn.grid(column = 2, row = 1)

        deleteFieldBtn = Button(window, text = 'Delete Field', command = deleteRows)
        deleteFieldBtn.configure(takefocus=0)
        deleteFieldBtn.grid(column = 2, row = 0)

        
        # fieldButton.grid(column= 2, row = i + 3, pady = 3, padx = 3)

        # buttonList.append(fieldButton.cget('text'))
        buttonList.append(cb.get())
        entryList.append(entryPoint)


    window.mainloop()

createType()