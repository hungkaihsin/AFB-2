class Team:
    # this is a skeleton class it will be added to later.
    
    def __init__(self,name = 'Default Team', players=[]):
        self.players = players
        self.name = name
    
    def get_players_at_position(self, position):
        ret = []
        # returns a list of players with whose position == position
        return ret

    # you can add stuff here that makes your life easier. I have included some of the ones I used below.

    def get_players_on_field(self):
        # this is a helper function
        # returns a list of players where on_field == True
        pass
        
    def create_default_team(self):
        # this populates the team with players the number for each position is the third argument in E positions
        # E.QB[2] --> 2
        # E.RB[2] --> 3
        # reminder E.POSITIONS is a list of all positions
        pass

    def get_name_and_position_of_players_on_field(self):
        # this is used for testing purposes it is not directly necessary
        pass

def main_test_team():
    print('main test team:')
    t = Team()
    # you should add code here to test functionality
