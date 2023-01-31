import sys
from math import ceil,atan2,hypot,pi,floor
class vector:
    def __new__(cls, my=(),history={}):
        print("1. Create a new instance of Vector.",file=sys.stderr, flush=True)
        return super().__new__(cls)
    def __init__(self) :
        self.activeCP = -1
        self.fireCP = -2
        self.history = {}
        print("1. Init a new instance of Vector.",file=sys.stderr, flush=True)
    def setup(self,my=(),cp=()):
        self.x = my[0]
        self.y = my[1]
        self.angle = atan2(self.y, self.x)
        self.abs = hypot(self.x, self.y)
        self.discover = True
        self.activeCP=cp
        self.history[(0,0)] = 0
        self.turn = 1

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
    def cps(self,cp=()) :
        keys = list(self.history.keys())
        self.changeCP = False if keys[-1] == cp else True
        if self.turn == 2: self.turn += 1 
        print(f"Debug cps : {self.changeCP}", file=sys.stderr, flush=True)
  
    def getCheckpoint(self,cp=(0,0)) :
        values = []
        self.get_distanceCP(cp)
        keys = list(self.history.keys())
        print(f"Debug getCheckpoint choice : {self.changeCP} activeCP : {self.activeCP} keys : {keys}, cp : {cp}", file=sys.stderr, flush=True)
        if cp in keys and self.changeCP is True :
            self.discover = False
            print(f"Debug getCheckpoint end of discover : {self.discover}", file=sys.stderr, flush=True)   
        else:
            self.history[cp] = self.distanceCP
        print(f"Debug getCheckpoint choice : {self.discover}", file=sys.stderr, flush=True)   
        keys = list(self.history.keys())
        i = keys.index(cp)
        self.passCP = keys[i-1] if i > 0 else keys[-1]
        self.get_distanceCP(self.passCP)
        self.history[self.passCP] = self.distanceCP
        self.values = sorted(self.history.values())
        print(f"Debug getCheckpoint values : {values}", file=sys.stderr, flush=True)   
        if self.discover is False:
            largest = self.values[-1]
            self.fireCP = [ k for k,v in self.history.items() if v == largest ][0]
            self.turn = 2
        print(f"Debug getCheckpoint activeCP : {self.activeCP} and fireCP {self.fireCP}", file=sys.stderr, flush=True)

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
strategy = vector()
bastard = vector()
while True:
    # next_checkpoint_x: x position of the next check point
    # next_checkpoint_y: y position of the next check point
    # next_checkpoint_dist: distance to the next checkpoint
    # next_checkpoint_angle: angle between your pod orientation and the direction of the next checkpoint
    x, y, next_checkpoint_x, next_checkpoint_y, next_checkpoint_dist, next_checkpoint_angle = [int(i) for i in input().split()]
    opponent_x, opponent_y = [int(i) for i in input().split()]
    
    #init startegy
    strategy.setup(my=(x,y),cp=(next_checkpoint_x,next_checkpoint_y))
    strategy.get_quadrant()
    # base strategy is to fluck bastard at last time
    mypod = strategy.get_distance((opponent_x,opponent_y))
    # get the CP status turn by turn
    strategy.cps((next_checkpoint_x,next_checkpoint_y))
    strategy.getCheckpoint((next_checkpoint_x,next_checkpoint_y))
    bastard.setup((opponent_x, opponent_y))
    bastard.get_quadrant()
    mybastardpod = bastard.get_distance((next_checkpoint_x,next_checkpoint_y))

    # be sur flucking bastard is possible avoid case it is a rabbit chinese year sign
    ecart = ceil(mypod - mybastardpod)

    #determine my orientation between CP ( no sexe subject keep cool please )
    strategy.getQuadrantCP((next_checkpoint_x,next_checkpoint_y))
    
    #Time to mesure power beetwen orientation of the Navi points ( special advise to Cameron Methodologie ) 
    print(f"Debug ecart is :'{ecart}' '{strategy.activeCP} : {strategy.fireCP}' {next_checkpoint_angle}", file=sys.stderr, flush=True)

    if strategy.activeCP == strategy.fireCP and next_checkpoint_angle >= -1 and next_checkpoint_angle <= 1 and strategy.turn == 3:
        power = 'BOOST'
        print(f"Debug case BOOST : {power}", file=sys.stderr, flush=True)
    elif next_checkpoint_dist < 500 or strategy.history[strategy.passCP] < 500:
        strategy.get_quadrant()
        strategy.virage()
        power = floor(strategy.puissance)
        print(f"Debug case °CP {strategy.angleCP} virage : {power}", file=sys.stderr, flush=True)
    else :
        if ecart > 50 or ecart < 0 :
            power = 100
            print(f"Debug case default Full Gas power {power}", file=sys.stderr, flush=True)
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
    