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
        # Reset all players' on_field status
        self.set_on_field(team)

        # Assign Offensive Linemen (LT, LG, C, RG, RT)
        offensive_line_positions = [71, 72, 73, 74, 75]
        offensive_line_roles = [E.LT, E.LG, E.C, E.RG, E.RT]

        for role, position in zip(offensive_line_roles, offensive_line_positions):
            linemen = team.get_players_at_position(role)
            if linemen:
                linemen[0].location = position
                linemen[0].on_field = True

        # Assign Quarterback (QB)


        qb_positions = [42]  # Example QB positions
        qbs = team.get_players_at_position(E.QB)

        for position in qb_positions:
            if qbs:  # Ensure there are available QBs to assign
                qb = qbs[0]  # Get the first QB
                qb.location = position
                qb.on_field = True
                qbs.pop(0)  # Remove the assigned QB from the list



        # Assign Wide Receivers (WR)
        wr_positions_left = [801, 802, 803, 804]  # Left-side WR positions
        wr_positions_right = [806, 807, 808, 809]  # Right-side WR positions

        wrs = team.get_players_at_position(E.WR)
        num_left = len(wr_positions_left)
        num_right = len(wr_positions_right)

        # Assign left-side WRs
        for i, position in enumerate(self.wrs):
            if i < len(wrs):
                wrs[i].location = position
                wrs[i].on_field = True

        # # Assign right-side WRs
        # for i, position in enumerate(wr_positions_right):
        #     if i + num_left < len(wrs):  # Continue from the next WR
        #         wrs[i + num_left].location = position
        #         wrs[i + num_left].on_field = True





        # Assign Tight Ends (TE)
        te_positions = [803]  # Example TE position
        tes = team.get_players_at_position(E.TE)
        for i, position in enumerate(self.tes):
            if i < len(tes):
                tes[i].location = position
                tes[i].on_field = True

        # Assign Fullbacks (FB)
        fb_positions = [24]  # Example FB position
        fbs = team.get_players_at_position(E.FB)
        for i, position in enumerate(self.fbs):
            if i < len(fbs):
                fbs[i].location = position
                fbs[i].on_field = True

        # Assign Running Backs (RB)
        rb_positions = [25]  # Example RB position
        rbs = team.get_players_at_position(E.RB)
        for i, position in enumerate(self.rbs):
            if i < len(rbs):
                rbs[i].location = position
                rbs[i].on_field = True






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
    print("\n" + "-" * 50 + "\n") # for divide group


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