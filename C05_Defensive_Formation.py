from Enums import E
from C02_Team import Team as T
from C03_Formation import Formation
from C06_Field import Field

class DefensiveFormation(Formation):
    def __init__(self, name, dl=[], lbs=[], cbs=[], safeties=[]):
        super().__init__()
        self.name = name
        self.dl = dl
        self.lbs = lbs
        self.cbs = cbs
        self.safeties = safeties
        self.set_positions()

    def set_positions(self):
        self.positions = []
        self.positions.extend([E.DL] * len(self.dl))
        self.positions.extend([E.LB] * len(self.lbs))
        self.positions.extend([E.CB] * len(self.cbs))
        self.positions.extend([E.S] * len(self.safeties))

    def set_on_field(self, team):
        for player in team.players:
            player.on_field = False

    def lineup(self, team):
        self.set_on_field(team)

        # Assign Defensive Linemen

        dl_positions = [90, 91, 92, 93, 94, 95]
        dls = team.get_players_at_position(E.DL)
        for i, position in enumerate(dl_positions):
            if i < len(dls):
                dls[i].location = position
                dls[i].on_field = True

        # Assign Linebackers
        lb_positions = [50, 52, 54]
        lbs = team.get_players_at_position(E.LB)
        for i, position in enumerate(lb_positions):
            if i < len(lbs):
                lbs[i].location = position
                lbs[i].on_field = True

        
        # Assign Cornerbacks
        cb_positions = [22, 25, 26, 27]
        cbs = team.get_players_at_position(E.CB)
        for i, position in enumerate(cb_positions):
            if i < len(cbs):
                cbs[i].location = position
                cbs[i].on_field = True

        # Assign Safeties
        safety_positions = [21, 44]
        safeties = team.get_players_at_position(E.S)
        for i, position in enumerate(safety_positions):
            if i < len(safeties):
                safeties[i].location = position
                safeties[i].on_field = True
def test_formation(f, t):
    f.lineup(t)
    
    field = Field()
    valid = field.update_grid(t, None)
    if valid:
        field.display_grid()
    else:
        print("Field update failed, check player locations.")
    print("\n" + "-" * 50 + "\n") # for divide groups

def main_test_defensive_formation():
    print("main test defensive formation:")
    t = T()
    t.create_default_team()
    f1 = DefensiveFormation('4-4', dl=[90, 92, 94, 96], lbs=[50, 52, 54, 57], cbs=[22, 23], safeties=[25, 26])
    f2 = DefensiveFormation('6-2', dl=[90, 91, 92, 94, 95, 96], lbs=[52, 54], cbs=[22, 23], safeties=[25, 26])
    f3 = DefensiveFormation('3-4', dl=[90, 93, 96], lbs=[50, 52, 54, 57], cbs=[22, 23], safeties=[25, 26])
    test_formation(f1, t)
    test_formation(f2, t)
    test_formation(f3, t)