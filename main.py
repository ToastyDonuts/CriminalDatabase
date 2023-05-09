from questionary import prompt
import questionary
import login_system
from prettytable import PrettyTable
import sqlite3

criminal_data = {}

class MainMenu():
    def show_menu(self):
        mainmenustuff = [
            {
                'type': 'select',
                'message': "Welcome to Super's Simple Criminal Database 1.0",
                'name': 'mainmenuchoice',
                "choices": ["Add or Remove Criminal Data", "Check Criminals Data", "Modify Exisiting Criminal Data", "Exit the database"]
            }
        ]
        main_menu_choices = prompt(mainmenustuff)
        if main_menu_choices["mainmenuchoice"] == 'Add or Remove Criminal Data':
            add_remove_data = AddRemoveData()
            add_remove_data.add_remove_choices_var
        elif main_menu_choices["mainmenuchoice"] == 'Check Criminals Data':
            check_criminal_data = CheckData()
            check_criminal_data.check_data_prompt
        elif main_menu_choices["mainmenuchoice"] == 'Modify Existing Criminal Data':
            pass
        elif main_menu_choices["mainmenuchoice"] == 'Exit the database':
            exit()
        else:
            print("Invalid choice")
 
class AddRemoveData():
    def __init__(self):
        self.add_name = None
        self.add_age = None
        self.add_status = None
        self.add_offense = None
        self.add_loop = False
        add_remove_choices = [   
            {
                'type': 'select',
                'message': "Please select your operations",
                'name': 'addremovechoices',
                "choices": ["Add data to the database", "Remove data from the database", "Return to Main Menu"]
            }
        ]
        self.add_remove_choices_var = prompt(add_remove_choices)
        if self.add_remove_choices_var["addremovechoices"] == 'Add data to the database':
            self.add_loop = True
            self.add_data()
        if self.add_remove_choices_var["addremovechoices"] == 'Remove data from the database':
            name_to_delete = questionary.text("Name of the person you would like to delete").ask()
            remove_data_init_db = Database()
            remove_data_init_func = remove_data_init_db.delete_specific_data_from_db
            remove_data_init_func(name_to_delete)
        if self.add_remove_choices_var["addremovechoices"] == 'Return to Main Menu':
                MainMenu().show_menu()
    def add_data(self):
            while self.add_loop == True:
                self.add_name = questionary.text("Name of the person you would like to add").ask()
                self.add_age = questionary.text("Age of the person you would like to add").ask()
                self.add_status = questionary.text("Punishment Status of the person you would like to add").ask()
                self.add_offense = questionary.text("Offense of the person you would like to add").ask()
                criminal_data[self.add_name] = (self.add_name, self.add_age, self.add_status, self.add_offense)
                database_class = Database()
                database_create = database_class.db_create_data
                database_create()
                self.ask_loop = questionary.confirm("Would you like to add more data?").ask()
                if self.ask_loop:
                    self.add_loop = True
                    pass
                else:  
                    self.add_loop = False
                    AddRemoveData()


    def removedata(self):
            pass
class CheckData():
    def __init__(self):
        check_data_question = [
             {
                'type': 'select',
                'message': "Please select your operations",
                'name': 'checkdata',
                "choices": ["Check specific person's data", "List all available data", "Return to Main Menu"]
             }
        ]
        self.check_data_prompt = prompt(check_data_question)
        self.check_loop = False
        if self.check_data_prompt["checkdata"] == "Check specific person's data":
            self.check_data_by_name() # Call the checkdatabyname function
            self.check_loop = True
        if self.check_data_prompt["checkdata"] == "List all available data":
            self.list_all_data()
        if self.check_data_prompt["checkdata"] == "Return to Main Menu":
            MainMenu().show_menu() # Call the showMenu function of the MainMenu class

    def check_data_by_name(self):
        check_by_name_init_db = Database()
        check_by_name_init_func = check_by_name_init_db.list_specific_data
        specific_ask_name_loop = False
        while specific_ask_name_loop == False:
            ask_name = questionary.text("Enter the name of the person you like to search up").ask()
            check_by_name_init_func(ask_name)
            specific_ask_name_loop_ask = questionary.confirm("Would you like to search for more data").ask()
            if specific_ask_name_loop_ask:
                pass
            else:
                CheckData() # Create a new instance of the CheckData class when the user is done searching
    def list_all_data(self):      
            db = Database()
            db.list_all_data()
    
class ModifyData():
    pass

class Database():
    def db_create_data(self):
        # connect to a database file
        conn = sqlite3.connect('criminal_data.db')
        # create a cursor
        c = conn.cursor()
        # create a table to store criminal data
        c.execute('''CREATE TABLE IF NOT EXISTS criminal_data
                    (name text, age integer, punishment text, offense text)''')
        # insert data into the table
        for name, data in criminal_data.items():
            c.execute("SELECT * FROM criminal_data WHERE name=?", (name,))
            row = c.fetchone()
            if row:
                print(f'Data for {name} already exists in the table.')
            else:
                c.execute("INSERT INTO criminal_data VALUES (?, ?, ?, ?)", data)
                print(f"Data for {name} added successfully.")
        # commit the changes and close the connection
        conn.commit()
        conn.close()
    def list_all_data(self):
        conn = sqlite3.connect('criminal_data.db')
        c = conn.cursor()
        # Execute a query to retrieve data from table
        c.execute('SELECT * FROM criminal_data')
        # Get column names and data rows
        rows = c.fetchall()
        # Create a pretty table and add columns
        list_all_table = PrettyTable()
        list_all_table.field_names = ["Name", "Age", "Punishment", "Offense"]
        # Add rows to table
        for row in rows:
            list_all_table.add_row(row)
        # Print the table
        print(list_all_table)
        AddRemoveData()
        # Close the database connection
        conn.close()
    def list_specific_data(self, name_to_search):
        # Connect to the database
        conn = sqlite3.connect('criminal_data.db')
        # Create a cursor object
        c = conn.cursor()
        # Execute a SELECT statement with a WHERE clause to search for a specific name
        print(f"Searching for data with name '{name_to_search}'...")
        c.execute("SELECT * FROM criminal_data WHERE name=?", (name_to_search,))
        list_search_table = PrettyTable()
        list_search_table.field_names = ["Name", "Age", "Punishment", "Offense"]
        # Fetch the results
        results = c.fetchall()
        print(f"Found {len(results)} matching rows")
        if results is not None:
            # Add the results to the table
            for row in results:
                list_search_table.add_row(row)
            # Print the table
            print(list_search_table)
        else:
            print("No data found for this person")
        # Close the cursor and the connection
        c.close()
        conn.close()
        
    def delete_specific_data_from_db(self, name_to_delete):
        # Connect to the database
        conn = sqlite3.connect('criminal_data.db')
        # Create a cursor object
        c = conn.cursor()
        # Execute a SELECT statement with a WHERE clause to search for a specific name
        print(f"Searching for data with name '{name_to_delete}'...")
        c.execute("SELECT * FROM criminal_data WHERE name=?", (name_to_delete,))
        list_search_table = PrettyTable()
        list_search_table.field_names = ["Name", "Age", "Punishment", "Offense"]
        # Fetch the results
        results = c.fetchall()
        print(f"Found {len(results)} matching rows") 
        if results is not None:
            # Add the results to the table
            for row in results:
                list_search_table.add_row(row)
            # Print the table
            print(list_search_table)
            delete_specific_data_confirmation = questionary.confirm(f"Are you sure you wanted to delete '{results}' from the database?").ask()
            if delete_specific_data_confirmation:
                c.execute("DELETE FROM criminal_data WHERE name=?", (name_to_delete,))
                print(f"'{name_to_delete}' has been successfully deleted")
                conn.commit()
                c.execute('VACUUM')
                conn.commit()
                AddRemoveData()
            else:
                print(f"Data deletion for '{name_to_delete}' has been cancelled")
                AddRemoveData()
        else:
            print("No data found for this person")
        # Close the cursor and the connection
        c.close()
        conn.close()

def return_to_main_menu():
        go_to_main_menu = MainMenu()
        go_to_main_menu.show_menu()

login_system.loginsys()
if login_system.loggedin == True:
    go_to_main_menu = MainMenu()
    go_to_main_menu.show_menu()

