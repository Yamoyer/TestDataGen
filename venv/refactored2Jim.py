from pydbgen import pydbgen
import pandas
import tkinter as tk

class DataEntryWindow(tk.Frame):
    newMenuList = ['ssn', 'name', 'country', 'date', 'company', 'state', 'city', 'real_(US)_cities',
                   'US_state', 'zipcode', 'latitude', 'longitude', 'Month', 'weekday', 'year', 'time', 'date',
                   'Personal_email', 'official_email', 'Job_title', 'phone_number', 'license_plate']
    menuList = ['ssn', 'name', 'country', 'date', 'company']



    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.fields = Fields()
        self.initial_setup()


    def initial_setup(self):
        self.add_field_button = tk.Button(self)
        self.add_field_button["text"] = "Add Field"
        self.add_field_button["command"] = self.add_field("Select Field")
        self.add_field_button.pack(side="top")

        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)
        self.quit.pack(side="bottom")

        for listItem in self.menuList:
            self.add_field(listItem)

        for field in self.fields.get_Fields():
            self.master.fieldButton = tk.Button(self.master, text = field.get_field_type(), command = self.master.destroy)
            self.master.fieldButton.pack(side="top")
            print(field.get_field_type())

    def say_hi(self):
        print("hi there, everyone!")

    def add_field(self, type):
        new_field = Field(type)
        self.fields.append(new_field)

#container class for Field
class Fields():
    def __init__(self):

        self.FieldList = []
    def append(self,field):
        self.FieldList.append(field)

    def draw_fields(self):
        for field in self.FieldList:
            field.draw_self()
    def get_Fields(self):
        return self.FieldList

#Field class
class Field():
    def __init__(self,  field_type):
        self.field_type = field_type

    def get_field_type(self):
        return self.field_type


root = tk.Tk()
app = DataEntryWindow(master=root)
app.mainloop()