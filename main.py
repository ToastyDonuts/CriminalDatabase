from colorama import Fore
from questionary import prompt
import questionary
import login_system

criminaldata = {}

class mainmenu():
    def mainmenu(self):
        mainmenustuff = [
            {
                'type': 'select',
                'message': "Welcome to Super's Simple Criminal Database 1.0",
                'name': 'mainmenuchoice',
                "choices": ["Add or Remove Criminal Data", "Check Criminals Data", "Modify Exisiting Criminal Data", "Exit the database"]
            },
            {
                'type': 'select',
                'message': "Please select your operations",
                'name': '1choices',
                "choices": ["Add data to the database", "Remove data from the database", "Return to Main Menu"]
            }
        ]

        mainmenuchoices = prompt(mainmenustuff)
        if mainmenuchoices["mainmenuchoice"] == 'Add or Remove Criminal Data':
            if mainmenuchoices["1choices"] == 'Add data to the database':
                self.addname = questionary.text("Name of the person you would like to add").ask()
                self.addingdict()
            elif mainmenuchoices["1choices"] == 'Remove data from the database':
                pass
            elif mainmenuchoices["1choices"] == 'Return to Main Menu':
                mainmenu()
        elif mainmenuchoices["mainmenuchoice"] == 'Check Criminals Data':
            pass
        elif mainmenuchoices["mainmenuchoice"] == 'Modify Existing Criminal Data':
            pass
        elif mainmenuchoices["mainmenuchoice"] == 'Exit the database':
            exit()
        else:
            print("Invalid choice")
    
    
    def addingdict(self):
        globals()[self.addname] = {}
        globals()[self.addname]["Name"] = str(self.addname)
        print(globals()[self.addname])


login_system.loginsys()

def logincheck():
    if login_system.loggedin == True:
        initmainmenu = mainmenu()
        initmainmenu.mainmenu()

logincheck()
