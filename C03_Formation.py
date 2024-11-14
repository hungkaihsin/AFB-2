from C06_Field import Field
from C02_Team import Team as T
from math import sqrt


class Formation:
    def __init__(self, positions=None, locations=None):
        self.positions = positions if positions is not None else []
        self.locations = locations if locations is not None else []

    def set_on_field(self, team):
    # resets on_field to False for all players on team
    # sets on_field to True for players in positions in self.positions
        for player in team.players:
            player.on_field = False

        for player in team.players:
            if player.position in self.positions:
                player.on_field = True


    def get_players_within_d_distance_of_location(self,d,location,team):
        # returns a list of players within d distance of location
        # location = 73 # col 10, row 3
        # e.g., location = (10, 3) for position 73       
        col, row = location   
        ret = []
        # FUNCTION TO FIND DISTANCE


        for player in team.get_players_on_field():
            # get col,row per player
            # calculate distance
            # if distance < d
            # add to return
            player_col, player_row = player.get_col_row_from_location()


            if player_col is not None and player_row is not None:
                distance = sqrt((col - player_col) ** 2 + (row - player_row) ** 2)
                if distance <= d:
                    ret.append(player)
        
        return ret

            
    # note this is distance in terms of both rows and columns
    # if location was 71 then x,y = 8,3
        

def main_test_formation():
    print('main test formation:')
    # add any test code here
    formation = Formation(positions=['QB', 'WR', 'RB', 'TE', 'DL', 'S'])  # Example positions

    # Create a team and set players on field
    team = T(name="Test Team")
    team.create_default_team()

    # Set players in the formation on the field
    formation.set_on_field(team)

    # Test players on the field (this should show only those in specified positions)
    players_on_field = team.get_players_on_field()
    for player in players_on_field:
        print(f"{player.name} - Position: {player.position} - On Field: {player.on_field}")

    # Example location to find nearby players (e.g., center of the field at (10, 3))
    location = (10, 3)
    d = 5  # Define distance
    nearby_players = formation.get_players_within_d_distance_of_location(d, location, team)
    print(f"Players within {d} units of location {location}:")
    for player in nearby_players:
        print(f"{player.name} - Position: {player.position}")