from Enums import E, RequirementNotMet
from C02_Team import Team as T
from C03_Formation import Formation 
from C06_Field import Field

class DefensiveFormation(Formation):
    def __init__(self, name, dl, lbs, cbs, sfs):
        super().__init__()
        
        # dl, lbs arguments are lists of locations
        # e.g. dl = [90,92,94,96] --> line up 4 DL at locations 90, 92,94,96
        # cbs and sfs are just the number on the field as their location is dependent on the offensive formation
        # NOTE: sometimes a lb will change location if man coverage but that doesn't need to be covered here
        
        self.name = name
        self.dl = dl
        self.lbs = lbs
        self.cbs = cbs
        
        self.set_positions()
        
    def set_positions(self):
        # fill self.positions with those positions in this formation
        pass
    
    def lineup(self, team:T):
        # refer to Enums for location diagram
        # use instructions such as self.wrs to set player locations
        #   e.g. if self.wrs = [803,805] then set 1 player with position E.WR to location 803 and the other to 805
        # linemen [E.LT, E.LG, E.CC, E.RG, E.RT] are always in the same spot
        # E.QB is either behind center location (13) or if in shotgun back one row (location 23)
        pass

def test_formation(f,t):
    f.set_on_field(t)
    t.get_name_and_position_of_players_on_field()
    f.lineup(t)
    field = Field()
    valid = field.update_grid(None,t)
    if valid:
        field.display_grid()

def main_test_defensive_formation():    
    print('main test defensive formation')
    t = T()
    t.create_default_team()
    f1 = DefensiveFormation('4-4',dl = [90,92,94,96], lbs = [50,52,54,57],cbs = 2, sfs = 1)
    f2 = DefensiveFormation('6-2',dl = [90,91,92,94,95,96], lbs = [52,54],cbs = 2, sfs = 1)
    f3 = DefensiveFormation('3-4',dl = [90,93,96], lbs = [50,52,54,57],cbs = 2, sfs = 2)
    test_formation(f1,t)
    test_formation(f2,t)
    test_formation(f3,t)