# TestDataGen
Test Data Generator
Use Case 1 – Generate random Data for given data type <Name> **Completed**

Get acquainted with using Python as well as get toes wet for use of data generation and faker data package. Test Data Generator will be used by clients to generate data for specific purposes. Eventually they will be able to use their own data for which they may create their own mock data for their own models. 
Features Use Case
•	User Friendly UI to provide inputs for random data generation
o	5 User input Data Fields
	Allows the user to name the columns for the generated data.
o	Functionality Buttons
	Generate data button
	Option menu
	Generates 1000 rows of data by default
Technology
Visual Studio Code - https://code.visualstudio.com/
Faker Data Package - https://github.com/stympy/faker
Pydbgen - https://github.com/tirthajyoti/pydbgen
Pandas data frames - https://pandas.pydata.org/
Tkinter Python Module - https://wiki.python.org/moin/TkInter

Design
Functions used to display all of entry windows and option menus
-	Entry menus are set in columns and rows with in the UI
-	Field names are not limited to type of character
-	Entry values are set to variables to be called anywhere
-	Option menu options are set to variables to be called anywhere

Error Log
-	Column names were not set via entry menu – resolved
-	Column names from entry and option menu were not set as variables – resolved
-	First option menu would not change to other types inside the printed tables – resolved
-	Data types would only stay in their own columns – resolved

 
Use Case 2 – Generate random Data for given data type cont.

Provides an even greater UI for users to input the amount of rows as well as be able to add more data types. Starts grouping datatypes in a separate window so that users can easily select what data types they need. Exports to excel spreadsheet. Faker used as the main source of random items use the delete method to get rid of rows not needed. Define window size and length for the type and field names. Background color of the window needs changing. Delete rows button.
*Include All faker data types.
***Highlighted Items are needed to be done.
Features Use Case
•	User Friendly UI to provide inputs for random data generation
o	5 User input Data Fields - Complete
	Allows the user to name the columns for the generated data. - Complete
o	Scrollable window, to allow the user to view the extra fields. - Incomplete
o	Row Amount Entry Field - Complete
	The amount of rows wanted by the user is input to be generated
	Limit the amount of additional columns to 16,384 -Incomplete
o	Functionality Buttons
	Generate data button
	Option Menus changed to buttons to access file types
	Generates amount of rows requested
	Generates an Excel file that is filled with the data needed by the user
	Additional field types button to add additional field type
	Delete Rows button to remove last field type
 Limit the amount of additional columns to 16,384
 
 Design
Functions used to display all of entry windows and option menus.
-	Entry menus are set in columns and rows with in the UI
-	Field names are not limited to type of character
-	Error Messages displayed when wrong inputs are set
-	Colors set, GUI centralized

Error Log
-	Scroll window is not usable with the current frame –unresolved
-	List exponentially grows. –Resolved
-	Window will not center. –resolved (Thank you Julius for the idea)
-	Button clicks from another window will not update in main menu. –unresolved
-	Additional fields won’t load into database. –unresolved


Version Control
 
Use Case 3 – Generate random Data for given data type cont.

- Customized columns 
-number based, alphanumeric length of field, kind of data they want.
- Convert into exe file so it no longer has to be run through python or cmd line.
Try to add multiple types in a window similar to mockaroo via buttons.
Features Use Case
•	User Friendly UI to provide inputs for random data generation
o	5 User input Data Fields
	Allows the user to name the columns for the generated data.
o	Row Amount Entry Field
	The amount of rows wanted by the user is input to be generated
o	Functionality Buttons
	Generate data button
	Option menu
	Generate new data type button
•	Used to add more rows of data to be entered for user
	Generates amount of rows requested
	Generates an Excel file that is filled with the data needed by the user


