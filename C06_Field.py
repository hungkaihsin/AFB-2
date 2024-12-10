from C02_Team import Team as T
from C01_Player import Player as P

class Field:
    COLS = 21
    ROWS = 7
    
    def __init__(self):
        # Initialize an empty grid with placeholders
        self.grid = [[" - " for _ in range(self.ROWS)] for _ in range(self.COLS)]
    
    def update_grid(self, offense:T, defense:T):
        valid = False
        
        # Debug output: offense players on field
        if offense is not None:
            players = offense.get_players_on_field()
            if players:
                print("Updating grid with offensive players:")
                valid = True
                for player in players:
                    player:P
                    try:
                        col, row = player.get_col_row_from_location()
                        if col is not None and row is not None:
                            # Place player's position symbol on the grid
                            self.grid[col][row] = ' ' + player.position[1]
                    except Exception as e:
                        print(f"Error placing {player.name} ({player.position}): {e}")
        
        # Debug output: defense players on field
        if defense is not None:
            players = defense.get_players_on_field()
            if players:
                print("Updating grid with defensive players:")
                valid = True
                for player in players:
                    player:P
                    try:
                        col, row = player.get_col_row_from_location()
                        if col is not None and row is not None:
                            # Place player's position symbol on the grid
                            self.grid[col][row] = ' ' + player.position[1]
                            print(f"Placed {player.name} ({player.position}) at ({col}, {row})")
                        else:
                            print(f"Warning: Invalid location for {player.name} ({player.position})")
                    except Exception as e:
                        print(f"Error placing {player.name} ({player.position}): {e}")
            else:
                print('Empty field: no defensive players or locations are not set.')
        
        if valid:
            return True
        else:
            print('No players detected on offense or defense')
            return False

    def display_grid(self):
        print("\nField Display:")
        for rw in range(self.ROWS):
            row = ""
            for c in range(self.COLS):
                row += self.grid[c][rw]
            print(row)