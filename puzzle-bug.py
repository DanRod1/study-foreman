import sys
from math import ceil,atan2,hypot,pi,floor
class vector:
    def __init__(self, my):
        self.x = my[0]
        self.y = my[1]
        self.angle = atan2(self.y, self.x)
        self.abs = hypot(self.x, self.y)
        self.history = {}

    def get_quadrant(self):
        """Get the quadrant a vector is facing."""
        if self.x > 0 and self.y > 0:
            self.quadrant = 1
        elif self.x < 0 and self.y > 0:
            self.quadrant = 2
        elif self.x < 0 and self.y < 0:
            self.quadrant = 3
        elif self.x > 0 and self.y < 0:
            self.quadrant = 4
    
    def getQuadrantCP(self,cp):
        """Get the quadrant a vector is facing."""
        self.angleCP = atan2(cp[1], cp[0])
    
    def get_distance(self, bastard):
        """ Get distance between two points """
        xp = bastard[0] - self.x
        yp = bastard[1] - self.y
        self.distance = hypot(xp, yp)
        return self.distance
    
    def get_distanceCP(self, cp):
        """ Get distance between two cp """
        xp = cp[0] - self.x
        yp = cp[1] - self.y
        self.distanceCP = hypot(xp, yp)
    
    def virage(self) :
        if self.quadrant == 1 :
            self.puissance = ( 100 * pi/4 )
            print(f"Debug virage case {self.quadrant} power {self.puissance}", file=sys.stderr, flush=True)
        elif self.quadrant == 2 :
            self.puissance = ( 100 - (90 * pi/4) )
            print(f"Debug virage case {self.quadrant} power {self.puissance}", file=sys.stderr, flush=True)
        elif self.quadrant == 3:
            self.puissance = 100 - ( 90 * 3 * pi / 4 )
            print(f"Debug virage case {self.quadrant} power {self.puissance}", file=sys.stderr, flush=True)
        elif self.quadrant == 4:
            self.puissance = ( 100 * 3 * pi / 4 )
            print(f"Debug virage case {self.quadrant} power {self.puissance}", file=sys.stderr, flush=True) 
    
    def cps(self,actifCP) :
        self.actifCP = actifCP
        self.oldCP = actifCP - 1 if actifCP >= 0 else 0
        self.newCP = actifCP + 1 if self.oldCP + 1 - actifCP == 0 else self.oldCP + 1
    
    def getCheckpoint(self,cp=(0,0)) :
        keys = list(self.history.keys())
        values = []
        discover = True
        print(f"Debug getCheckpoint history : {self.history} and cp {cp} keys {keys}", file=sys.stderr, flush=True)
        if cp not in keys :
            self.get_distanceCP(cp)
            self.history[cp] = self.distanceCP
            discover = True
            self.activeCP = -1
            self.fireCP = -2
        else :
            self.activeCP = keys.index(cp)
            values = sorted(list(self.history.values()))
            discover = False     
        if discover is False:
            self.fireCP = keys.index(values[-1])
        print(f"Debug getCheckpoint history : {self.activeCP} and cps {self.fireCP}", file=sys.stderr, flush=True)

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

while True:
    # next_checkpoint_x: x position of the next check point
    # next_checkpoint_y: y position of the next check point
    # next_checkpoint_dist: distance to the next checkpoint
    # next_checkpoint_angle: angle between your pod orientation and the direction of the next checkpoint
    x, y, next_checkpoint_x, next_checkpoint_y, next_checkpoint_dist, next_checkpoint_angle = [int(i) for i in input().split()]
    opponent_x, opponent_y = [int(i) for i in input().split()]
    strategy = vector((x,y))
    strategy.get_quadrant()
    mypod = strategy.get_distance((opponent_x,opponent_y))
    strategy.getCheckpoint((next_checkpoint_x,next_checkpoint_y))
    print(f"Debug history is :'{strategy.history}'", file=sys.stderr, flush=True)

    bastard= vector((opponent_x, opponent_y))
    bastard.get_quadrant()
    mybastardpod = bastard.get_distance((next_checkpoint_x,next_checkpoint_y))

    ecart = ceil(mypod - mybastardpod)
    #print(f"Debug mypods : {dir(strategy)}", file=sys.stderr, flush=True)
    #print(f"Debugbastard : {dir(bastard)} ", file=sys.stderr, flush=True)
    print(f"Debug ecart is :'{ecart}'", file=sys.stderr, flush=True)


    strategy.getQuadrantCP((next_checkpoint_x,next_checkpoint_y))
    viragedb = False if strategy.angleCP > -5 and strategy.angleCP < 5 else True

    if strategy.activeCP == strategy.fireCP:
        power = 'BOOST'
    elif next_checkpoint_dist < 500 and viragedb == True:
        strategy.get_quadrant()
        strategy.virage()
        power = floor(strategy.puissance)
        print(f"Debug case °CP {strategy.angleCP} virage {viragedb} : {power}", file=sys.stderr, flush=True)
    else :
        viragedb = False
        if ecart > 50 or ecart < 0 :
            power = 100
        else:
            power = 100 - floor(ecart/10)
            print(f"Debug case default Follow Bastard power {power}", file=sys.stderr, flush=True)
    # Write an action using print
    print(f"Debug Proude Knight {x} {y}", file=sys.stderr, flush=True)
    print(f"Debug Bastard {opponent_x} {opponent_y}", file=sys.stderr, flush=True)
    print(f"Debug Finsih Data {next_checkpoint_x} {next_checkpoint_y} {next_checkpoint_dist} {next_checkpoint_angle}", file=sys.stderr, flush=True) 
    


    # You have to output the target position
    # followed by the power (0 <= thrust <= 100)
    # i.e.: "x y thrust"
    print(str(next_checkpoint_x ) + " " + str(ceil(next_checkpoint_y)) + " " + str(power))