from Enums import E
from C02_Team import Team as T
from C03_Formation import Formation
from C06_Field import Field

class OffensiveFormation(Formation):
    def __init__(self, name, tes=[], wrs=[], fbs=[], rbs=[], shotgun=False):
        super().__init__()
        self.name = name
        self.tes = tes
        self.wrs = wrs
        self.fbs = fbs
        self.rbs = rbs
        self.shotgun = shotgun
        self.set_positions()

    def set_positions(self):
        self.positions = [E.QB]
        self.positions.extend([E.WR] * len(self.wrs))
        self.positions.extend([E.TE] * len(self.tes))
        self.positions.extend([E.FB] * len(self.fbs))
        self.positions.extend([E.RB] * len(self.rbs))
        self.positions.extend([E.LT, E.LG, E.C, E.RG, E.RT])

    def set_on_field(self, team):
        for player in team.players:
            player.on_field = False

    def lineup(self, team):
        self.set_on_field(team)
        # Linemen positions
        linemen_positions = [71, 72, 73, 74, 75]
        linemen_roles = [E.LT, E.LG, E.C, E.RG, E.RT]
        
        position_check_list = []

        for role, position in zip(linemen_roles, linemen_positions):
            
            linemen = team.get_players_at_position(role)
            # if len(position_check_list) != 0:
            #     break

            # if count != 0 :
            #     break

            if linemen not in position_check_list:
                count = 0
                for index in linemen:
                    if count > 0:
                        break
                    index.location = position
                    index.on_field = True
                    position_check_list.append(index)
                    count += 1



                

        # QB position
        QB_position = [13]
        QB_role = [E.QB]
        result_QB = []

        for role, position in zip(QB_role, QB_position):
            qbs = team.get_players_at_position(role)

            if qbs not in result_QB:
                count = 0
                for index in qbs:
                    if count > 0:
                        break

                    index.position = position
                    index.on_field = True
                    result_QB.append(index)
                    count += 1

        
    


        # WR, TE, RB, FB positions
        position_role = [E.WR, E.TE, E.RB, E.FB]
        WR_TE_RB_FB_position = [800, 80, 20, 40]

        WR_check_list = []



        for role, position in zip(position_role, WR_TE_RB_FB_position):
            player = team.get_players_at_position(role)

            if player not in WR_check_list:
                count = 0
                for index in player:
                    if count > 0:
                        break
                    index.location = position
                    index.on_field = True
                    WR_check_list.append(index)
                    count += 1






        # for position_list, players, position_name in zip(
        #     [self.wrs, self.tes, self.rbs, self.fbs],
        #     [team.get_players_at_position(E.WR[1]),
        #      team.get_players_at_position(E.TE[1]),
        #      team.get_players_at_position(E.RB[1]),
        #      team.get_players_at_position(E.FB[1])],
        #     ["WR", "TE", "RB", "FB"]):

        #     for i, location in enumerate(position_list):
        #         if i < len(players):
        #             players[i].location = location
        #             players[i].on_field = True

    def get_eligible_receivers(self):
        eligible_positions = [E.WR, E.TE, E.RB, E.FB]
        return [p for p in self.positions if p in eligible_positions]

def test_formation(f, t):
    f.lineup(t)
   
    field = Field()
    valid = field.update_grid(t, None)
    if valid:
        field.display_grid()

def main_test_offensive_formation():
    print("main test offensive formation:")
    t = T()
    t.create_default_team()
    f1 = OffensiveFormation('Single Back', tes=[80], fbs=[], rbs=[23], wrs=[801, 803, 806])
    f2 = OffensiveFormation('I-Back', tes=[86], fbs=[33], rbs=[23], wrs=[801, 806])
    f3 = OffensiveFormation('Trips Right', tes=[80], wrs=[805, 806, 807], rbs=[23], shotgun=True)
    test_formation(f1, t)
    test_formation(f2, t)
    test_formation(f3, t)