# modules I used:
#   import random as r
#   import pandas as pd

from Enums import E, RequirementNotMet

class Player():
    def __init__(self, name = None, position = None) -> None:
        # Position must be set to a value that is in Enums.E.POSITIONS if not raise exception RequirementNotMet
        self.position = position
        
        self.attribute1 = E.MIN + 3 # These should be changed to be random and reflect the range from min to max in some way
        self.attribute2 = E.MAX
        self.attribute3 = 42


        #   if 2000 names are generated none should match exactly. 
        self.first_name = 'Adam'    # have a method of changing this
        self.last_name = 'Godson'   # have a method of changing this
        self.name = self.first_name + ' ' + self.last_name
        self.number = None          # this will be a reflection of position eventually and unique on a team for now it is simply initialized (0-99)
        
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

        return None # modify this return
    
    def get_col_row_from_location(self):
        # TODO: this is new !!!!!
        #3 OFFENSE   801   802   803  804      80 71 72 73 74 75 86         806      807      808      809
        #4:        811   812   813  814               13                  816      817      818      819 
        #5:                                        42 43 44
        #6:                                     21 22 23 24 25
        
        
        # these locations are ported to a columns and rows
        # where 73 is col 10, row 3
        # there is a space of 3 between 804 and 80 and 86 and 806
        # crib sheet:
            # 801 1 3
            # 802 2 3
            # 803 3 3
            # 804 4 3
            # 80 7 3
            # 71 8 3
            # 72 9 3
            # 73 10 3
            # 74 11 3
            # 75 12 3
            # 86 13 3
            # 806 16 3
            # 807 17 3
            # 808 18 3
        col = None
        row = None
        return col, row
    def compete(self, enumed_attribute):
        # returns an integer which is a reflection of the players performance with this attribute
        return r.randint(1,6)   # this is bad code as it doesn't consider the enumed attribute

def main_test_player():
    print('main test player:')
    p = Player(position = E.FB)    
    p.location = 43
    c,row = p.get_col_row_from_location()
    print("COL ROW",c,row)
    print(p.name)