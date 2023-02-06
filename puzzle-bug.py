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
        self.turn = 1
        self.consentant = 0
        self.velocity = 0
        self.wavepoint = 0
        print("1. Init a new instance of Vector.",file=sys.stderr, flush=True)   
    def setup(self,my=(),cp=()):
        self.x = my[0]
        self.y = my[1]
        self.angle = atan2(self.y, self.x)
        self.abs = hypot(self.x, self.y)
        self.discover = True
        self.activeCP=cp
    def colissionAlert(self) :
        max = hypot(16000,9000)
        self.alert = ( self.distance/max ) * 100 
    def get_quadrant(self):
        """Get the quadrant a vector is facing."""
        self.quadrant = atan2(self.y , self.x)  
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
        if self.quadrant >= 0 and self.quadrant < 1.57 :
            self.puissance = ( 100 * pi/4 )
            print(f"Debug virage case {self.quadrant} power {self.puissance}", file=sys.stderr, flush=True)
        elif self.quadrant >= 1.57 and self.quadrant < 3.14 :
            self.puissance = ( 100 - (90 * pi/4) )
            print(f"Debug virage case {self.quadrant} power {self.puissance}", file=sys.stderr, flush=True)
        elif self.quadrant >= 3.14 and self.quadrant < 4.71 :
            self.puissance = 100 - ( 90 * 3 * pi / 4 )
            print(f"Debug virage case {self.quadrant} power {self.puissance}", file=sys.stderr, flush=True)
        elif self.quadrant >= 4.71 and self.quadrant <= 6.28:
            self.puissance = ( 100 * 3 * pi / 4 )
            print(f"Debug virage case {self.quadrant} power {self.puissance}", file=sys.stderr, flush=True) 
    def cps(self,cp=()) :
        keys = list(self.history.keys())
        self.changeCP = False 
        if len(keys) >= 2 :
            last = keys.pop(len(keys)-2)
            print(f"Debug cps : {self.wavepoint} last : {last}", file=sys.stderr, flush=True) 
            if last != cp : 
                self.changeCP = True
                print(f"Debug cps wavepoint : {self.wavepoint} cp : {cp}", file=sys.stderr, flush=True) 
                if self.fireCP == cp :
                    self.consentant = self.wavepoint
                    print(f"Debug cps wavepoint : {self.wavepoint} cp : {cp} consentant : {self.consentant}", file=sys.stderr, flush=True)
        
        print(f"Debug cps : {self.changeCP}", file=sys.stderr, flush=True)

  
    def envoiPurée(self, next_checkpoint_angle ):
        self.get_distanceCP(self.activeCP)
        aligned = True if next_checkpoint_angle >= -3 and next_checkpoint_angle <= 3 and self.distanceCP > 500 else False
        if self.turn == 2 and self.consentant > 0 and self.fireCP == self.activeCP and aligned == True :
            return True
        else:
            return False

    def getCheckpoint(self,cp=(0,0)) :
        self.get_distanceCP(cp)
        keys = list(self.history.keys())
        self.wavepoint = len(keys)
        #print(f"Debug getCheckpoint distanceCP : {self.distanceCP}", file=sys.stderr, flush=True) 
        t0 =  self.distanceCP
        print(f"Debug getCheckpoint keys : {keys}, cp : {cp}", file=sys.stderr, flush=True)
        self.history[cp] = {'distance': self.distanceCP, 'wavepoint' : self.wavepoint }    
        #print(f"Debug getCheckpoint choice : {self.discover}", file=sys.stderr, flush=True)   
        keys = list(self.history.keys())
        i = keys.index(cp)
        self.passCP = keys[i-1] if i > 0 else keys[-1]
        self.get_distanceCP(self.passCP)
        t1 =  self.distanceCP
        #print(f"Debug getCheckpoint passCP : {self.passCP}", file=sys.stderr, flush=True)   
        self.history[self.passCP] = {'distance': self.distanceCP, 'wavepoint' : self.wavepoint }    
        #print(f"Debug getCheckpoint values : {self.values}", file=sys.stderr, flush=True)   
        if self.discover is False:
            largest = self.values[-1]
            self.fireCP = [ k for k,v in self.history.items() if v == largest ][0]
            #print(f"Debug getCheckpoint largest {largest} : {self.fireCP}", file=sys.stderr, flush=True)  
        if keys.index(self.passCP) == 3 and type(self.fireCP) is tuple : self.turn = 2 
        self.looping = True if t0 == t1 else False 
        print(f"Debug getCheckpoint history : {self.history}", file=sys.stderr, flush=True)   
        #print(f"Debug getCheckpoint activeCP : {self.activeCP} and fireCP {self.fireCP}", file=sys.stderr, flush=True)

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
    # base strategy is to fluck bastard at last time or defonce it option
    cp = (next_checkpoint_x,next_checkpoint_y)
    strategy.setup(my=(x,y),cp=cp)
    strategy.get_quadrant()
    ecart = ceil(strategy.get_distance((opponent_x,opponent_y)))
    
    # get the CP status turn by turn
    strategy.getCheckpoint((next_checkpoint_x,next_checkpoint_y))
    strategy.cps((next_checkpoint_x,next_checkpoint_y))
    
    # be sur flucking bastard is possible, avoid case it is a rabbit chinese year sign
    #bastard.setup((opponent_x, opponent_y))
    #bastard.cps((next_checkpoint_x,next_checkpoint_y))
    #bastard.getCheckpoint((next_checkpoint_x,next_checkpoint_y))
    #bastard.get_quadrant()
    #mybastardpod = bastard.get_distance((next_checkpoint_x,next_checkpoint_y)) 
 

    #New parameter to manage
    strategy.colissionAlert()

    #determine my orientation between CP ( no sexe subject keep cool please )
    strategy.getQuadrantCP((next_checkpoint_x,next_checkpoint_y))
    
    #Time to mesure power beetwen orientation of the Navi points ( special advise to Cameron Methodologie ) 
    print(f"Debug ecart before choice strategy is :'{ecart}'", file=sys.stderr, flush=True)
    if strategy.envoiPurée(next_checkpoint_angle) :
        power = 'BOOST'
        print(f"Debug case BOOST : {power}", file=sys.stderr, flush=True)
    elif next_checkpoint_dist < 3000 or strategy.history[strategy.passCP]['distance'] < 100 :
        strategy.get_quadrant()
        strategy.virage()
        power = floor(strategy.puissance)
        print(f"Debug ecart is :'{ecart}' quadrant '{strategy.quadrant} and {strategy.angleCP}", file=sys.stderr, flush=True)
    elif ecart > 100 :
        cp = (opponent_x,opponent_y)
        power = 100
        print(f"Debug ecart focus on Bastard :'{ecart}' power '{power}", file=sys.stderr, flush=True)
    elif ecart <= -100 :
        cp = (next_checkpoint_x,next_checkpoint_y)
        power = 100
        print(f"Debug ecart focus on CP :'{ecart}' power '{power}", file=sys.stderr, flush=True)
    else :
            power = 100 if strategy.looping is False else ceil(100 - ( ceil(strategy.alert) / 100 )-1)
            print(f"Debug case default Follow Bastard power {power}", file=sys.stderr, flush=True)
    # Write an action using print
    print(f"Debug Proude Knight {x} {y}", file=sys.stderr, flush=True)
    print(f"Debug Bastard {opponent_x} {opponent_y}", file=sys.stderr, flush=True)
    print(f"Debug Finsih Data {next_checkpoint_x} {next_checkpoint_y} {next_checkpoint_dist} {next_checkpoint_angle}", file=sys.stderr, flush=True) 
    


    # You have to output the target position
    # followed by the power (0 <= thrust <= 100)
    # i.e.: "x y thrust"
    print(str(next_checkpoint_x ) + " " + str(ceil(next_checkpoint_y)) + " " + str(power))
    