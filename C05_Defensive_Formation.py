from Enums import E, RequirementNotMet
from C02_Team import Team as T
from C03_Formation import Formation
from C06_Field import Field

class DefensiveFormation(Formation):
    def __init__(self, name, dl, lbs, cbs, sfs):
        super().__init__()
        self.name = name
        self.dl = dl      # List of DL locations
        self.lbs = lbs    # List of LB locations
        self.cbs = cbs    # Number of CBs to place
        self.sfs = sfs    # Number of Safeties to place

    def set_on_field(self, team):
        for player in team.players:
            player.on_field = False

    def lineup(self, team: T):
        print(f"\nSetting up {self.name} defensive lineup...")
        self.set_on_field(team)  # Reset the field for all players

        # DL Positions
        dl_players = team.get_players_at_position(E.DL[1])  # Get all players with DL position
        print("\nAssigning DL positions...")
        for i, location in enumerate(self.dl):
            if i < len(dl_players):
                dl_players[i].location = location
                dl_players[i].on_field = True
                print(f"Assigned {dl_players[i].name} - Position: {dl_players[i].position} - Location set to {dl_players[i].location}")
            else:
                print("Insufficient DL players available.")

        # LB Positions
        lb_players = team.get_players_at_position(E.LB[1])
        print("\nAssigning LB positions...")
        for i, location in enumerate(self.lbs):
            if i < len(lb_players):
                lb_players[i].location = location
                lb_players[i].on_field = True
                print(f"Assigned {lb_players[i].name} - Position: {lb_players[i].position} - Location set to {lb_players[i].location}")
            else:
                print("Insufficient LB players available.")

        # CB Positions
        cb_players = team.get_players_at_position(E.CB[1])
        print("\nAssigning CB positions...")
        cb_locations = [22, 23]  # Pre-defined locations for CBs
        for i, location in enumerate(cb_locations):
            if i < len(cb_players):
                cb_players[i].location = location
                cb_players[i].on_field = True
                print(f"Assigned {cb_players[i].name} - Position: {cb_players[i].position} - Location set to {cb_players[i].location}")
            else:
                print("Insufficient CB players available.")

        # S Positions
        s_players = team.get_players_at_position(E.S[1])
        print("\nAssigning S positions...")
        s_locations = [25, 26]  # Pre-defined locations for Safeties
        for i, location in enumerate(s_locations):
            if i < len(s_players):
                s_players[i].location = location
                s_players[i].on_field = True
                print(f"Assigned {s_players[i].name} - Position: {s_players[i].position} - Location set to {s_players[i].location}")
            else:
                print("Insufficient S players available.")

def test_formation(f, t):
    f.lineup(t)
    print("\nVerification: Players with on_field set to True and their locations:")
    for player in t.get_players_on_field():
        print(f"{player.name} - Position: {player.position} - Location: {player.location}")

    field = Field()
    valid = field.update_grid(None, t)
    if valid:
        field.display_grid()
    else:
        print("Field update failed, check player locations.")

def main_test_defensive_formation():
    print("main test defensive formation")
    t = T()
    t.create_default_team()
    f1 = DefensiveFormation('4-4', dl=[90, 92, 94, 96], lbs=[50, 52, 54, 57], cbs=2, sfs=1)
    f2 = DefensiveFormation('6-2', dl=[90, 91, 92, 94, 95, 96], lbs=[52, 54], cbs=2, sfs=1)
    f3 = DefensiveFormation('3-4', dl=[90, 93, 96], lbs=[50, 52, 54, 57], cbs=2, sfs=2)
    test_formation(f1, t)
    test_formation(f2, t)
    test_formation(f3, t)