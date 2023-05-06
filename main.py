from questionary import prompt
import questionary
import login_system
import pprint

criminal_data = {}

class Main_Menu():
    def showMenu(self):
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
            self.adddata(criminal_data)
        if self.add_remove_choices_var["addremovechoices"] == 'Remove data from the database':
             pass
        if self.add_remove_choices_var["addremovechoices"] == 'Return to Main Menu':
             self.addremovereturntomenu()
    def adddata(self, criminal_data):
            while self.add_loop == True:
                self.addname = questionary.text("Name of the person you would like to add").ask()
                self.addage = questionary.text("Age of the person you would like to add").ask()
                self.addstatus = questionary.text("Punishment Status of the person you would like to add").ask()
                self.addoffense = questionary.text("Offense of the person you would like to add").ask()
                dictsys = dictionarysys(self.addname, self.addage, self.addstatus, self.addoffense)
                dictsys.createnewsets(criminal_data)
                self.ask_loop = questionary.confirm("Would you like to add more data?").ask()
                if self.ask_loop:
                    pass
                else:  
                    self.add_loop = False
                    self.addremovereturntomenu()

    def removedata(self):
            pass
    def addremovereturntomenu(self):
            self.ask_return_to_menu = questionary.confirm("Would you like to return to main menu?").ask()
            if self.ask_return_to_menu:
                go_to_main_menu = Main_Menu()
                go_to_main_menu.showMenu()
            else:       
                AddRemoveData()
class CheckData():
    def __init__(self):
            self.check_name = None
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
                 self.check_name = questionary.text("Enter the name of the person you would like to search up").ask()
                 self.checkdatabyname()
            if self.check_data_prompt["checkdata"] == "List all available data":
                 self.listalldata()
            if self.check_data_prompt["checkdata"] == "Return to Main Menu":
                 self.checkdatareturntomenu()
    def checkdatabyname(self):
            if self.check_name in criminal_data:
                pprint.pprint(criminal_data[self.check_name])
            else:
                print("Data not found for this person")
                check_loop_ask = questionary.confirm("Would you like to search more data?").ask()
                if check_loop_ask:
                     self.check_loop = True
                     pass
                else:
                     CheckData()
            while self.check_loop == True:
                 self.check_name = questionary.text("Enter the name of the person you would like to search up").ask()
                 self.checkdatabyname()
    def listalldata(self):
         pprint.pprint(criminal_data)
    def checkdatareturntomenu(self):
        self.ask_return_to_menu = questionary.confirm("Would you like to return to main menu?").ask()
        if self.ask_return_to_menu:
            go_to_main_menu = Main_Menu()
            go_to_main_menu.showMenu()
        else:       
            CheckData()

class ModifyData():
    pass
class dictionarysys():
    def __init__(self, add_name, add_age, add_status, add_offense):
        self.add_name = add_name
        self.add_age = add_age
        self.add_status = add_status
        self.add_offense = add_offense
    def createnewsets(self, criminal_data):
        criminal_data[self.add_name] = (self.add_name, self.add_age, self.add_status, self.add_offense)
        print(criminal_data)

login_system.loginsys()
if login_system.loggedin == True:
    go_to_main_menu = Main_Menu()
    go_to_main_menu.showMenu()

