from colorama import Fore
from questionary import prompt


def mainmenu():
    mainmenu = [

        {
            'type': 'select',
            'message': "Please Sign-In before accessing the database",
            'name': 'mainmenuchoice',
            "choices": ["Add or Remove Criminal Data", "Check Criminals Data", "Modify Exisiting Criminal Data", "Exit the database"]
        }
    ]

    mainmenuchoices = prompt(mainmenu)
    if mainmenuchoices["mainmenuchoice"] == 'Add or Remove Criminal Data':
        pass
    elif mainmenuchoices["mainmenuchoice"] == 'Check Criminals Data':
        pass
    elif mainmenuchoices["mainmenuchoice"] == 'Modify Existing Criminal Data':
        pass
    elif mainmenuchoices["mainmenuchoice"] == 'Exit the database':
        exit()
    else:
        print("Invalid choice")


def new_dict(varname):
    globals()[varname] = {}

class CriminalTemplate:
    
    def __init_(self, name, age, offense, sentences, status):
        self.name = name
        self.age = age
        self.offense = offense
        self.sentences = sentences
        self.status = status
    def addingdict(self):
        new_dict()
        
mainmenu()