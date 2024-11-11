from C06_Field import Field
from C02_Team import Team as T

class Formation:
    def __init__(self):
        self.positions = []
        self.locations = []

    def set_on_field(self, team):
    # resets on_field to False for all players on team
    # sets on_field to True for players in positions in self.positions
        pass

    def get_players_within_d_distance_of_location(self,d,location,team):
        # returns a list of players within d distance of location
        location = 73 # col 10, row 3
        ret = []
        # FUNCTION TO FIND DISTANCE
        for player in team.get_players_on_field():
            # get col,row per player
            # calculate distance
            # if distance < d
            # add to return
         pass     
            
    # note this is distance in terms of both rows and columns
    # if location was 71 then x,y = 8,3
        

def main_test_formation():
    print('main test formation:')
    # add any test code here