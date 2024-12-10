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
        print(f"Setting up {self.name} defensive lineup...")

        # Assign Defensive Linemen
        for i, location in enumerate(self.dl):
            dl_players = team.get_players_at_position(E.DL[1])
            if i < len(dl_players):
                dl_players[i].location = location
                dl_players[i].on_field = True
                print(f"Assigned {dl_players[i].name} - Position: DL - Location set to {dl_players[i].location}")

        # Assign Linebackers
        for i, location in enumerate(self.lbs):
            lb_players = team.get_players_at_position(E.LB[1])
            if i < len(lb_players):
                lb_players[i].location = location
                lb_players[i].on_field = True
                print(f"Assigned {lb_players[i].name} - Position: LB - Location set to {lb_players[i].location}")

        # Assign Cornerbacks
        for i, location in enumerate(self.cbs):
            cb_players = team.get_players_at_position(E.CB[1])
            if i < len(cb_players):
                cb_players[i].location = location
                cb_players[i].on_field = True
                print(f"Assigned {cb_players[i].name} - Position: CB - Location set to {cb_players[i].location}")

        # Assign Safeties
        for i, location in enumerate(self.safeties):
            s_players = team.get_players_at_position(E.S[1])
            if i < len(s_players):
                s_players[i].location = location
                s_players[i].on_field = True
                print(f"Assigned {s_players[i].name} - Position: S - Location set to {s_players[i].location}")

def test_formation(f, t):
    f.lineup(t)
    print("\nVerification: Players with on_field set to True and their locations:")
    for player in t.players:
        if player.on_field:
            print(f"{player.name} - Position: {player.position} - Location: {player.location}")

    print("\nPlayers and their assigned locations before grid update:")
    for player in t.players:
        if player.on_field:
            print(f"{player.name} - Position: {player.position} - Location: {player.location}")
    
    field = Field()
    valid = field.update_grid(t, None)
    if valid:
        field.display_grid()
    else:
        print("Field update failed, check player locations.")

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