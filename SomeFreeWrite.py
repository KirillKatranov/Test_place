class Ship():
    """
    Ship model, for testing
    """
    def __init__(self, model, team):
        self.model = model
        self.team = team

class Team():
    def __init__(self, list_team):
        self.list_team = list_team


class Participants():
    def __init__(self, name:str, work:str):
        self.name = name
        self.work = work

    def add_to_team(self, cls:Team):
       crew = Team(self.name) 
        

#Не установлен смысл наследования