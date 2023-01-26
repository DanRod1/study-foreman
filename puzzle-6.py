import sys
from math import ceil

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
def getDistanceWithBatard(x1=0,y1=0,x2=0,y2=0,ncx=0,ncy=0) :
    sens = 'S' if x1 < ncx and y1 < ncy else 'N'
    myboxes = (((x1-1)*16000+x1) + ((y1-1*9000)+y1))/100
    hisboxes = (((x2-1)*16000+x1) + ((y2-1*9000)+y1))/100
    delta = (myboxes - hisboxes)*-1 if sens == 'S' else hisboxes - myboxes
    return delta

def getDistanceWithCheckP(x1=0,y1=0,ncx=0,ncy=0) :
    myboxes = (((x1-1)*16000+x1) + ((y1-1*9000)+y1))/100
    checkboxes = (((ncx-1)*16000+x1) + ((ncy-1*9000)+y1))/100
    delta = myboxes - checkboxes
    return delta

def getCheckpoint(history={},cps=0) :
    print(f"Debug getCheckpoint history : {history} and cps {cps}", file=sys.stderr, flush=True)
    if list(history.keys()).count(next_checkpoint_x) <= 1 :
        history[next_checkpoint_x] = next_checkpoint_y
        cps = {next_checkpoint_x:next_checkpoint_y}
        print(f"Debug getCheckpoint case 1", file=sys.stderr, flush=True)
        return True,history,cps
    else :
        cps = {next_checkpoint_x:next_checkpoint_y}
        return False,history,cps


def virage(positif=False) :
    power = 100 - (100/380 * next_checkpoint_angle) if positif is True else 100 - (100/380 * -1 * next_checkpoint_angle)
    print(f"Debug virage angle posifif {positif} power {power}", file=sys.stderr, flush=True)
    return power
# game loop
laps = 0
nbCPs = 0
history= {}
actifCP = 0
while True:
    # next_checkpoint_x: x position of the next check point
    # next_checkpoint_y: y position of the next check point
    # next_checkpoint_dist: distance to the next checkpoint
    # next_checkpoint_angle: angle between your pod orientation and the direction of the next checkpoint
    x, y, next_checkpoint_x, next_checkpoint_y, next_checkpoint_dist, next_checkpoint_angle = [int(i) for i in input().split()]
    opponent_x, opponent_y = [int(i) for i in input().split()]
    history[next_checkpoint_x] = next_checkpoint_y

    ecart = getDistanceWithBatard(x1=x,y1=y,x2=opponent_x,y2=opponent_y,ncx=next_checkpoint_x,ncy=next_checkpoint_y)
    finish = getDistanceWithCheckP(x1=x,y1=y,ncx=next_checkpoint_x,ncy=next_checkpoint_y)
    stands = getCheckpoint(history=history,cps=nbCPs) 
    
    if stands[0] is True :
        nbCPs = len(list(stands[1].keys()))
        CPx = list(stands[1].keys())
        CPy = list(stands[1].values())
        finish = getDistanceWithCheckP(x1=x,y1=y,ncx=CPx[-1],ncy=CPy[-1])
        actifCP = CPx.index(next_checkpoint_x)
        print(f"Debug checkpoint find: '{nbCPs}' '{CPx[-1]}' '{CPy[-1]}' '{finish}' '{actifCP}'", file=sys.stderr, flush=True)   
        laps += 1 if actifCP > 0 else 0
        print(f"Debug laps '{laps}'", file=sys.stderr, flush=True)

    print(f"Debug distance data : '{ecart}' '{finish}' '{next_checkpoint_angle}'", file=sys.stderr, flush=True)
    if next_checkpoint_dist < 5000 :
        if next_checkpoint_angle <= 5 and next_checkpoint_angle >= -5 : 
            power = 100
            print(f"Debug angle positif power {power}", file=sys.stderr, flush=True)
        elif next_checkpoint_angle > 5 or next_checkpoint_angle < -5 :
            power = virage(positif=True) if next_checkpoint_angle > 5 else virage(positif=False)
            power = ceil(power)
        else :
            power = 95
    elif next_checkpoint_dist > 5000 and actifCP == 3:
        if next_checkpoint_angle <= 5 and next_checkpoint_angle >= -5 :
            power = 'BOOST'
            print(f"Debug boost trigged: {power}", file=sys.stderr, flush=True)
        else:
            power = 100
            print(f"Debug default full gas power {power}", file=sys.stderr, flush=True)
    else :
        power = 97
        print(f"Debug default full gas power {power}", file=sys.stderr, flush=True)
    # Write an action using print
    print(f"Debug {x} {y} {next_checkpoint_x} {next_checkpoint_y} {next_checkpoint_angle}", file=sys.stderr, flush=True)
    print(f"Debug {opponent_x} {opponent_y}", file=sys.stderr, flush=True)


    # You have to output the target position
    # followed by the power (0 <= thrust <= 100)
    # i.e.: "x y thrust"
    print(str(next_checkpoint_x) + " " + str(next_checkpoint_y) + " " + str(power))