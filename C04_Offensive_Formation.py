from Enums import E, RequirementNotMet
# these are necessary for testing but not for implementation
from C02_Team import Team as T
from C03_Formation import Formation 
from C06_Field import Field

class OffensiveFormation(Formation):
    def __init__(self, name, tes=[], wrs=[], fbs=[], rbs=[], shotgun = False):
        super().__init__()
        
        # arguments are lists of locations
        # e.g. tes = [80,806] --> line up 2 tight ends at location 0 and 86
        #   translates to location information 80 and 806
        
        self.name = name
        self.tes = tes
        self.wrs = wrs
        self.fbs = fbs
        self.rbs = rbs
        self.shotgun = shotgun
        
        self.set_positions()
        
    def set_positions(self):
        # fill self.positions with those positions in this formation
        pass
    
    def lineup(self, team):
        # refer to Enums for location diagram
        # use instructions such as self.wrs to set player locations
        #   e.g. if self.wrs = [803,805] then set 1 player with position E.WR to location 803 and the other to 805
        # linemen [E.LT, E.LG, E.CC, E.RG, E.RT] are always in the same spot
        # E.QB is either behind center location (13) or if in shotgun back one row (location 23)
        pass
    
    def get_eligible_receivers():
        # returns a list of eligible receivers in this formation
        # eligible positions are WR, TE, RB, FB
        pass


def test_formation(f,t):
    f.set_on_field(t)
    t.get_name_and_position_of_players_on_field()
    f.lineup(t)
    field = Field()
    valid = field.update_grid(t,None)
    if valid:
        field.display_grid()

def main_test_offensive_formation():
    print("main test offensive formation:")
    t = T()
    t.create_default_team()
    f1 = OffensiveFormation('Single Back',tes = [80], fbs = [], rbs = [23], wrs = [801,803,806])
    f2 = OffensiveFormation('I-Back', tes = [86], fbs=[33],rbs=[23],wrs=[801,806])
    f3 = OffensiveFormation('Trips Right', tes=[80],wrs=[805,806,807], rbs = [23], shotgun=True)
    # A trips single back formation has a tightend on the left, no fullbacks, a running back behind the qb and three wrs to the right
    test_formation(f1,t)
    test_formation(f2,t)
    test_formation(f3,t)
