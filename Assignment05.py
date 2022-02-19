# ------------------------------------------------------------------------ #
# Title: Assignment 05
# Description: Working with Dictionaries and Files
#              When the program starts, load each "row" of data
#              in "ToDoToDoList.txt" into a python Dictionary.
#              Add the each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# Brandon Lorge 2.11.2022-2.15.2022,Added code to complete assignment 5
# ------------------------------------------------------------------------ #

# -- Data -- #
# declare variables and constants
objFile = "ToDoList.txt"   # An object that represents a file
strData = ""  # A row of text data from the file
dicRow = {}    # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A list that acts as a 'table' of rows
strMenu = ""   # A menu of user options
strChoice = "" # A Capture the user option selection


# -- Processing -- #
# Step 1 - When the program starts, load the any data you have
# in a text file called ToDoList.txt into a python list of dictionaries rows (like Lab 5-2)
# Code to load the test file so that it is not empty at the start
objFile = open("ToDoList.txt", "w")
dicRow1 = {"Task":"Laundry", "Priority":"Medium"}
objFile.write(str(dicRow1['Task']) + ',' + str(dicRow1['Priority']) + '\n')
dicRow2 = {"Task":"Clean Car", "Priority":"Low"}
objFile.write(str(dicRow2['Task']) + ',' + str(dicRow2['Priority']) + '\n')
dicRow3 = {"Task":"Cook Dinner", "Priority":"High"}
objFile.write(str(dicRow3['Task']) + ',' + str(dicRow3['Priority']) + '\n')
objFile.close()
objFile = open("ToDoList.txt", "r")
# Loading file into memory in a table
for row in objFile:
    lstRow = row.split(",")
    dicRow = {"Task":lstRow[0],"Priority":lstRow[1].strip()}
    lstTable.append(dicRow)
objFile.close() #Closing File as processing starts, opening and closing later to save


# -- Input/Output -- #
# Step 2 - Display a menu of choices to the user
while (True):
    print("""
    Menu of Options
    1) Show current data
    2) Add a new item.
    3) Remove an existing item.
    4) Save Data to File
    5) Exit Program
    """)
    strChoice = str(input("Which option would you like to perform? [1 to 5] - "))
    print()  # adding a new line for looks

    # Step 3 - Show the current items in the table
    if (strChoice.strip() == '1'):
        for Row in lstTable:
            print(Row)
        continue

    # Step 4 - Add a new item to the list/Table
    elif (strChoice.strip() == '2'):
        strN1 = input("Enter a task ")      # Entered task handle is strN1
        strN2 = input("Enter a priority ")  # Entered priority is strN2
        dicRow = {"Task":strN1, "Priority":strN2}  # Adding the input to the dictionary
        lstTable.append(dicRow)
        continue

    # Step 5 - Remove a new item from the list/Table
    elif (strChoice.strip() == '3'):
        for row in lstTable:
            print(row)
        taskDelete = input("Please enter a task to delete ")
        for row in lstTable:
            if row["Task"].lower() == taskDelete.lower():
                lstTable.remove(Row)
        print("Please review the task list for your changes")
        for Row in lstTable:                    # Displays the list to the user
            print(Row)
        continue

    # Step 6 - Save tasks to the ToDoToDoList.txt file
    elif (strChoice.strip() == '4'):
        objFile = open("ToDoList.txt", "w")
        for lstRow in lstTable:
            objFile.write(str(lstRow) + '\n')
        print("Data was saved to file ")
        objFile.close()
        continue

    # Step 7 - Exit program
    elif (strChoice.strip() == '5'):
        print("Goodbye")
        break  # and Exit the program
