def new_dict(varname):
    globals()[varname] = {}

def mainmenu():
    pass

class CriminalTemplate:
    
    def __init_(self, name, age, offense, sentences, status):
        self.name = name
        self.age = age
        self.offense = offense
        self.sentences = sentences
        self.status = status
    def addingdict(self):
        new_dict()
        