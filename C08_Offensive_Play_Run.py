from C07_Offensive_Play import Offensive_Play

class Offensive_Run_Play(Offensive_Play):
    def __init__(self, name, formation, ball_carrier, zone):
        super().__init__(self, name, formation)
        # ball_carrier is position
        # zone is a number reflecting location on field
        self.ball_carrier = ball_carrier
        self.zone = zone

    def stage1(self):
        # this should get the positions that will block at the point of attack
        pass

    def stage2(self):
        # this should get the positions that will block at the second level
        pass
