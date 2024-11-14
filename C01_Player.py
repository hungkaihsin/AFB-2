# modules I used:
import random as r
import pandas as pd

from Enums import E, RequirementNotMet


class Player():
    nameset = set()
    def __init__(self, name = None, position = None) -> None:
        # Position must be set to a value that is in Enums.E.POSITIONS if not raise exception RequirementNotMet
        if position is None:
            position = E.POSITIONS[0]  # Assuming E.POSITIONS[0] is a valid default
        elif position not in [pos[1] for pos in E.POSITIONS]:
            raise RequirementNotMet("Position not recognized.")
        
        
        self.position = position


        
        self.attribute1 = r.randint(E.MIN, E.MAX) # These should be changed to be random and reflect the range from min to max in some way
        self.attribute2 = r.randint(E.MIN, E.MAX) 
        self.attribute3 = r.randint(E.MIN, E.MAX) 
        df = pd.read_csv('data/Names.csv')

        #   if 2000 names are generated none should match exactly. 

        while True:
            self.first_name = df['first_name'].sample().values[0]
            self.last_name = df['last_name'].sample().values[0]
            self.name = f"{self.first_name} {self.last_name}"
            if self.name not in Player.nameset:
                Player.nameset.add(self.name)
                break


        # self.first_name = 'Adam'    # have a method of changing this
        # self.last_name = 'Godson'   # have a method of changing this
        # self.name = self.first_name + ' ' + self.last_name
        self.number = 15          # this will be a reflection of position eventually and unique on a team for now it is simply initialized (0-99)
        
        #   game level variables these will change throughout the game
        self.location = 0,0         # this will change with time
        self.on_field = False       
        self.is_blitzing = False
        self.scheme_mod = False
        self.man_coverage = 0
        self.zone_coverage = 0

    def generate_random_name(self):
        # this is an optional function to generate a name so you don't clutter you initialize. 
        # you may make as many of these as you wish. Just know I will never call them directly.
        pass

    def get_attribute(self, enumed_attribute):
        # enumertions ATR1,ATR2,ATR3 exist in enums
        # based on the enumed attribute return the correct associated value
        # raise RequirementNotMet if the enumed_attribue is not ATR1 ATR2 or ATR3
        # for example if player.attribute1 = 100
        # then player.get_attribute_enumed_attribute(E.ATR1) should return 100
        if  enumed_attribute == E.ATR1:
            return self.attribute1
        elif  enumed_attribute == E.ATR2:
            return self.attribute2
        elif  enumed_attribute == E.ATR3:
            return self.attribute3
        else:
            raise RequirementNotMet  


        # return None # modify this return
    
    def get_col_row_from_location(self):

        # Expanded location map with new mappings from the provided diagram
        location_map = {
            801: (1, 3), 802: (2, 3), 803: (3, 3), 804: (4, 3),
            80: (7, 3), 71: (8, 3), 72: (9, 3), 73: (10, 3),
            74: (11, 3), 75: (12, 3), 86: (13, 3), 806: (16, 3),
            807: (17, 3), 808: (18, 3), 809: (19, 3),
            
            # New locations based on the additional comments
            941: (2, 2), 942: (7, 2), 943: (13, 2), 944: (19, 2),
            931: (1, 2), 932: (8, 2), 933: (19, 2),
            531: (5, 1), 532: (13, 1),
            
            201: (1, 1), 202: (2, 1), 203: (3, 1), 204: (4, 1),
            50: (7, 1), 51: (8, 1), 52: (9, 1), 53: (10, 1),
            54: (11, 1), 55: (12, 1), 56: (13, 1), 206: (16, 1),
            207: (17, 1), 208: (18, 1), 209: (19, 1),
            
            # Defense positions (Backfield Eligible)
            811: (1, 0), 812: (2, 0), 3: (5, 0),
            42: (11, -1), 43: (12, -1), 44: (13, -1),
            21: (8, -2), 22: (9, -2), 23: (10, -2),
            24: (11, -2), 25: (12, -2),
            
            # Pass zones
            41: (2, -1), 31: (5, -1), 32: (8, -1), 33: (13, -1)
        }
        
        # Retrieve the column and row for the given location
        if self.location in location_map:
            col, row = location_map[self.location]
        else:
            col, row = None, None  # Handle cases where location is not mapped

        return col, row


    def compete(self, enumed_attribute):
        if self.get_attribute(enumed_attribute) == E.ATR1:
            return self.get_attribute(enumed_attribute) + r.randint(1, 6)
        elif self.get_attribute(enumed_attribute) == E.ATR2:
            return self.get_attribute(enumed_attribute) + r.randint(1, 6)
        elif self.get_attribute(enumed_attribute) == E.ATR3:
            return self.get_attribute(enumed_attribute) + r.randint(1, 6)
        else:
            raise RequirementNotMet


        # returns an integer which is a reflection of the players performance with this attribute
        return r.randint(1,6)   # this is bad code as it doesn't consider the enumed attribute

def main_test_player():
    print('main test player:')
    p = Player(position = E.FB)    
    p.location = 43
    c,row = p.get_col_row_from_location()
    print("COL ROW",c,row)
    print(p.name)