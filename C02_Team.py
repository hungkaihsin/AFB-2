from Enums import E
from C01_Player import Player

class Team:
    # this is a skeleton class it will be added to later.
    
    def __init__(self,name = 'Default Team', players=[]):
        self.players = players
        self.name = name
    
    def get_players_at_position(self, position):
        # returns a list of players with whose position == position
        return [player for player in self.players if player.position == position]

    # you can add stuff here that makes your life easier. I have included some of the ones I used below.

    def get_players_on_field(self):
        # this is a helper function
        # returns a list of players where on_field == True
        return [player for player in self.players if player.on_field]
        
    def create_default_team(self):
        # this populates the team with players the number for each position is the third argument in E positions
        # E.QB[2] --> 2
        # E.RB[2] --> 3
        # reminder E.POSITIONS is a list of all positions
        # if self.get

        # Populates the team with players based on E.POSITIONS
        for pos_info in E.POSITIONS:
            if len(pos_info) < 3:
                print(f"Skipping position {pos_info[1]} as it lacks a count value.")
                continue

            position_id, position_name, count = pos_info
            for _ in range(count):
                # Create a Player object with the specified position
                player = Player(position=pos_info)
                self.players.append(player)
                
        

    def get_name_and_position_of_players_on_field(self):
        # this is used for testing purposes it is not directly necessary
        return [(player.name, player.position) for player in self.get_players_on_field()]


def main_test_team():
    print('main test team:')
    t = Team()
    # you should add code here to test functionality
    t.create_default_team()

    # Example of getting players on the field
    players_on_field = t.get_name_and_position_of_players_on_field()
    print("Players on field:", players_on_field)