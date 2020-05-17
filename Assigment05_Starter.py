# ------------------------------------------------------------------------ #
# Title: Assignment 05
# Description: Working with Dictionaries and Files
#              When the program starts, load each "row" of data
#              in "ToDoToDoList.txt" into a python Dictionary.
#              Add the each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# Kate Golenkova,05/17/2020,Added code to complete assignment 5
# ------------------------------------------------------------------------ #

# -- Data -- #
# declare variables and constants
objFile = "ToDoList.txt"   # An object that represents a file
strData = ""  # A row of text data from the file
dicRow = {}    # A row of data separated into elements of a dictionary {Fruit, Letters}
lstTable = []  # A list that acts as a 'table' of rows
strMenu = ""   # A menu of user options
strChoice = "" # A Capture the user option selection

# -- Processing -- #
# Step 1 - When the program starts, load the any data you have
# in a text file called ToDoList.txt into a python list of dictionaries rows (like Lab 5-2)
# TODO: Add Code Here
print("\nIn the file ToDoList.txt you have next information: \n")
# Open file and read each row into list
objFile = open("C:\_PythonClass\Assignment05\ToDoList.txt", "r")
for row in objFile:
    strData = row.split(",") # Returns a list!
    dicRow = {"Fruit": strData[0], "Letters": strData[1].strip()}
    lstTable.append(dicRow)
objFile.close()
print(lstTable)

# -- Input/Output -- #
# Step 2 - Display a menu of choices to the user
print("\nPlease choose the option from the Menu what to do next.")
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
        # TODO: Add Code Here
        print("You choose option 1, your current data in ToDoList.txt file is: \n")
        print(lstTable)

    # Step 4 - Add a new item to the list/Table
    elif (strChoice.strip() == '2'):
        # TODO: Add Code Here
        # while loop to get user input and print new data
        while True:
            item = input("You choose option 2, please type your favorite fruit: ")
            len_item = int(len(item))
            item = item.capitalize()
            print("Yor favorite fruit is " + item + " and this word contains  " + str(len_item) + " letters!\n")
            dicRow = {"Fruit": item, "Letters": len_item}
            lstTable.append(dicRow)
            print("Here is your new data: \n")
            print(dicRow)
            break

    # Step 5 - Remove a new item from the list/Table
    elif (strChoice.strip() == '3'):
        # TODO: Add Code Here
        # while loop to get user input to delete row with exact fruit
        while True:
            strData = input("You choose option 3, please type the fruit you want to delete: \n")
            for row in lstTable:
                if row["Fruit"].lower() == strData.lower():
                    lstTable.remove(row)
                    print("The row has been deleted.")
                    break
                else:
                    print("This fruit not found.")
            #input("Press Enter to exit option 3: \n")
            break

    # Step 6 - Save tasks to the ToDoToDoList.txt file
    elif (strChoice.strip() == '4'):
        # TODO: Add Code Here
        # Open file and save each row of new data to it
        print("You choose option 4, lets save your data into ToDoList.txt file!\n")
        objFile = open("C:\_PythonClass\Assignment05\ToDoList.txt", "w")
        for row in lstTable:
            objFile.write("{0},{1}\n".format(row["Fruit"], row["Letters"]))
        objFile.close()
        print(lstTable)
        print("\nYour data has been saved!\n")
        input("Press Enter key to exit option 4: \n")

    # Step 7 - Exit program
    elif (strChoice.strip() == '5'):
        # TODO: Add Code Here
        input("Press ENTER key to exit the program: ")
        break  # and Exit the program


