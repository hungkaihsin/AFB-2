import random as r
import pandas as pd
from Enums import E, RequirementNotMet

class Player:
    nameset = set()
    def __init__(self, name=None, position=None):
        # Ensure the position is set to a value that exists in E.POSITIONS
        if position is None:
            position = E.POSITIONS[0][1]  # Default to the name of the first position in E.POSITIONS
        elif position not in [pos[1] for pos in E.POSITIONS]:
            raise RequirementNotMet("Position not recognized.")
        
        self.position = position

        self.attribute1 = r.randint(E.MIN, E.MAX)
        self.attribute2 = r.randint(E.MIN, E.MAX)
        self.attribute3 = r.randint(E.MIN, E.MAX)
        
        df = pd.read_csv('data/Names.csv')
        while True:
            self.first_name = df['first_name'].sample().values[0]
            self.last_name = df['last_name'].sample().values[0]
            self.name = f"{self.first_name} {self.last_name}"
            if self.name not in Player.nameset:
                Player.nameset.add(self.name)
                break

        self.number = r.randint(0, 99)
        self.location = (0, 0)
        self.on_field = False
        self.is_blitzing = False
        self.scheme_mod = False
        self.man_coverage = 0
        self.zone_coverage = 0

    def get_attribute(self, enumed_attribute):
        if enumed_attribute == E.ATR1:
            return self.attribute1
        elif enumed_attribute == E.ATR2:
            return self.attribute2
        elif enumed_attribute == E.ATR3:
            return self.attribute3
        else:
            raise RequirementNotMet

    def get_col_row_from_location(self):
        location_map = {
            801: (1, 3), 802: (2, 3), 803: (3, 3), 804: (4, 3),
            80: (7, 3), 71: (8, 3), 72: (9, 3), 73: (10, 3),
            74: (11, 3), 75: (12, 3), 86: (13, 3), 806: (16, 3),
            807: (17, 3), 808: (18, 3), 809: (19, 3),
            941: (2, 2), 942: (7, 2), 943: (13, 2), 944: (19, 2),
            931: (1, 2), 932: (8, 2), 933: (19, 2),
            531: (5, 1), 532: (13, 1),
            201: (1, 1), 202: (2, 1), 203: (3, 1), 204: (4, 1),
            50: (7, 1), 51: (8, 1), 52: (9, 1), 53: (10, 1),
            54: (11, 1), 55: (12, 1), 56: (13, 1), 206: (16, 1),
            207: (17, 1), 208: (18, 1), 209: (19, 1),
            811: (1, 0), 812: (2, 0), 3: (5, 0),
            42: (11, -1), 43: (12, -1), 44: (13, -1),
            21: (8, -2), 22: (9, -2), 23: (10, -2),
            24: (11, -2), 25: (12, -2),
            41: (2, -1), 31: (5, -1), 32: (8, -1), 33: (13, -1)
        }
        
        return location_map.get(self.location, (None, None))

    def compete(self, enumed_attribute):
        return self.get_attribute(enumed_attribute) + r.randint(1, 6)

def main_test_player():
    print('main test player:')
    p = Player(position='FB')  # Use the position name 'FB'
    p.location = 43
    col, row = p.get_col_row_from_location()
    print("COL ROW:", col, row)
    print(p.name)