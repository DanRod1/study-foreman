import sys
import re
from math import ceil
import time


# debug formatage

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

#fonction perso
def getDistBet2Pts(a='',b='') :
    xa, ya = a.split()
    xb, yb = b.split()
    if (int(xa) - int(xb)) >= 0 :
        fX = 1
    else:
        fX = -1
    if (int(ya) - int(yb)) >= 0 :
        fY = 1
    else:
        fY = -1
    
    dXY = (int(xa) - int(xb) * fX ) + ( int(ya) - int(yb) * fY)
    return int(dXY)

def processRobots(config = {}, moves = [] ) :
    robots = config['robots']
    activeRobots = config['activeRobots']
    stats = config['stats']
    cibles = config['cibles']
    enemiesList = config['enemies']  
    hauteur = config['hauteur']
    largeur = config['largeur']
    
    #unUsedRegion = next(iter(dict(sorted(boxByRegion.items(), key=lambda item: item[1]))))
    for key in robots :
        if tour == 0 :
            robots[key]['choose'] = 'wait'
            robots[key]['tour'] =  0 
        posfrom = robots[key]['from']
        fabs, ford = [int(i) for i in posfrom.split()]        
        max = ((largeur / hauteur) * 5 )
        figthers = (stats['figthers'] * 100 / activeRobots )
        locateEnenmiesNear = getBox(zone = enemiesList,position = robots[key]['from'],filter = robots[key]['region'])
        
        if 0 >= figthers < 10  and  locateEnenmiesNear is not False :
            action = f"MOVE 1"
            robots[key]['choose'] = 'figthers'
            near = getNearTarget( x = fabs, y = ford, cibles = todestroy, filter = robots[key]['region'], max = ceil(max))
            #print(f'Figther create {robots[key]}',file = sys.stderr, flush = True )
        elif figthers > 85 and locateEnenmiesNear is not False:
            action = f"MOVE 1"
            robots[key]['choose'] = 'figthers'    
            near = getNearTarget( x = fabs, y = ford, cibles = cibles, filter = robots[key]['region'], max = ceil(max) )
        else:
            action = f"MOVE 1"
            near = getNearTarget( x = fabs, y = ford, cibles = cibles, max = ceil(max))    

        action += f' {posfrom}'
        
        before = len(action)       
        #statsNoFight = dict(filter(lambda elem: elem[0] != 'figthers', stats.items()))

        possibleChoice = sorted(near, key=near.get('distance'))
        #print(f'choix le plus proche par distance {possibleChoice}',file = sys.stderr, flush = True )
        #print(f'Stats des deplacement de robots {stats}',file = sys.stderr, flush = True )
        for i in possibleChoice:
            position = near[i]['position']
            if position not in moves :
                robots[key]['choose'] = i 
                distance = near[i]['distance']
                robots[key]['tour'] = tour + distance
                break
        
        #print(f'POSITION == { position }',file=sys.stderr, flush=True)
        #print(f'CHOICE == { possibleChoice }',file=sys.stderr, flush=True)
        
        if 'position'  in locals():
            action += f" {position}"      
        after = len(action)
        
        if after - before > 0 :
            robots[key]['action'] = action
        else :
            robots[key]['action'] = ''
            robots[key]['tour'] = tour + 1
            
    return robots


def getBoxByRegion(cibles={}) :
    regions = sorted(set([v['region'] for k,v in cibles.items() if 'region' in v.keys() ]))
    taux = {}
    for i in regions :
        count = int(len([k for k,v in cibles.items() if v['region'] == i]))   
        region = i
        taux.update({ region : count })
    return taux

def getBox(zone=[], position = '', filter=None, recycling = False ) :
    x , y = [ int(i) for i in position.split()]
    if filter is not None :
        region = filter
    else:
        region = getPositionRegion(hauteur,largeur,x,y)

    #pprint(f'sizeMap == {sizeMap} recycling == {recycling} ',file=sys.stderr, flush=True)
    for i in zone :
        if recycling is True :
            regionE = next(iter(i.keys()))
            posE = i[regionE]
            if region == regionE :
                xE , yE = [ int(i) for i in posE.split()]
                if ( yE - 1 == x ) or ( yE + 1 == x ) :
                    return f'{x} {y}'
        else:
            regionE = next(iter(i.keys()))
            #pprint(f'REGION == {next(iter(i.keys()))}',file=sys.stderr, flush=True)
            posE = i[regionE]
            #pprint(f'POSITION == {i[regionE]}',file=sys.stderr, flush=True)
            if region == regionE :
                xE , yE = [ int(j) for j in posE.split()]
                if xE - 1 == x and yE - 1 == y :
                    return f'{xE} {yE}'
                if xE == x and yE -1 == y :
                    return f'{xE} {yE}'
                if xE + 1 == x and yE -1 == y :
                    return f'{xE} {yE}'
                if xE -1 == x and yE == y :
                    return f'{xE} {yE}'
                if xE + 1 == x and yE == y:
                    return f'{xE} {yE}'
                if xE - 1 == x and yE + 1 == y :
                    return f'{xE} {yE}'
                if xE == x and yE + 1 == y :
                    return f'{xE} {yE}'
                if xE + 1 == x and yE + 1 == y:
                    return f'{xE} {yE}'
                else :
                    continue
    return False


def getPositionRegion(hauteur=0,largeur=0, x=0, y=0 ) :
    geoloc = ''
    if ( y == 0 and x == 0 ) or ( y == 0 and (x / 2 < largeur / 2 ) ):
        return 'A'
    elif y == 0 and ( x / 2 >= largeur / 2 ) :
        return 'D'
    if x <= ( 0.5 * largeur) and y <= ( 0.5 * hauteur ) and ( x / y ) >= ( hauteur / largeur ):
        return 'A'
    if x <= ( 0.5 * largeur) and y <= ( 0.5 * hauteur ) and ( x / y ) < ( hauteur / largeur ) :
        return 'C'
    if x >= ( 0.5 * largeur) and y <= ( 0.5 * hauteur ) and ( x / y ) >= ( hauteur / largeur ) :
        geoloc = 'D'
    if x >= ( 0.5 * largeur ) and y <= ( 0.5 * hauteur ) and ( x / y ) < ( hauteur / largeur ) :
        geoloc = 'E'
    if x <= ( 0.5 * largeur) and y >= ( 0.5 * hauteur ) and ( x / y ) >= ( hauteur / largeur ) :
        geoloc = 'B'
    if x <= ( 0.5 * largeur) and y >= ( 0.5 * hauteur ) and ( x / y ) < ( hauteur / largeur ) : 
        geoloc = 'H'
    if x >= ( 0.5 * largeur) and y >= ( 0.5 * hauteur ) and ( x / y ) >= ( hauteur / largeur ) :
        geoloc = 'F'
    if x >= ( 0.5 * largeur) and y >= ( 0.5 * hauteur ) and ( x / y ) >= ( hauteur / largeur ) :
        geoloc = 'G'
    
    return geoloc

def getStatByRobots(robots = {} ) :
    tmp = [k for k,v in robots.items() if v['choose'] == 'rigth' ]
    robotsOnRigth = len(tmp)
    tmp = [k for k,v in robots.items() if v['choose'] == 'left' ]
    robotsOnLeft = len(tmp)
    tmp = [k for k,v in robots.items() if v['choose'] == 'up' ]
    robotsOnUp = len(tmp)
    tmp = [k for k,v in robots.items() if v['choose'] == 'down' ]
    robotsOnDown = len(tmp)
    tmp = [k for k,v in robots.items() if v['choose'] == 'wait' ]
    robotsOnWait = len(tmp)
    tmp = [k for k,v in robots.items() if v['choose'] == 'figthers' ]
    robotsOnFight = len(tmp)

    stats = {   'rigth' : int(robotsOnRigth) , 
                'left' : int(robotsOnLeft) , 
                'up' : int(robotsOnUp) , 
                'down' : int(robotsOnDown), 
                'wait' : int(robotsOnWait),
                'figthers' : int(robotsOnFight)
            }
    print(f'STATS ROBOTS == { stats }',file=sys.stderr, flush=True)
    return stats 

def getNearTarget( x=int(0), y=int(0), cibles = {}, max=5, filter = None ):
    location = {}
    dist = 1
    #pprint(f'DEBUT getNearTarget CIBLE',file=sys.stderr, flush=True)
    #pprint(f'CIBLE == {cibles}',file=sys.stderr, flush=True)
    if filter is not None :
        filterCibles = {}
        for k,v in cibles.items() :
            if v['region'] == filter :
                filterCibles[k] = v
        cible = filterCibles
    while max - dist > 0 :
        #pprint(f' From X == {x} Y == {y}',file=sys.stderr, flush=True)
        increaseRigth = dist
        increaseLeft = dist
        increaseUp = dist
        increaseDown = dist   
        for k,v in cibles.items() :
            ecart = getDistBet2Pts(a=f'{x} {y}',b=f'{v["abs"]} {v["ord"]}') 
            #pprint(f'Lookin for case {v} and ecart de {ecart} et max à {max}',file=sys.stderr, flush=True)
            if v['abs'] == ( x + increaseRigth ) and v['ord'] == y and location.get('rigth') is None and ecart <= max :
                location['rigth'] = { 'distance' : dist, 'position' : f'{x + increaseRigth} {y}', 'choose' : 'rigth', 'region' : v['region'] }
                #pprint(f'RIGTH cible == {v["action"]} x == {x} y == {y} location == {location["rigth"]}',file=sys.stderr, flush=True)
            if v['abs'] == ( x - increaseLeft ) and v['ord'] == y and location.get('left') is None and ecart <= max :
                location['left'] = { 'distance' : dist, 'position' : f'{x - increaseLeft} {y}', 'choose' : 'left', 'region' : v['region'] }
                #pprint(f'LEFT cible == {v["action"]} x == {x} y == {y} location == {location["left"]}',file=sys.stderr, flush=True)
            if v['abs'] == x and v['ord'] == ( y + increaseDown ) and location.get('down') is None and ecart <= max :
                location['down'] = { 'distance' : dist, 'position' : f'{x} {y +  increaseDown}', 'choose' : 'down', 'region' : v['region'] }
                #pprint(f'DOWN cible == {v["action"]} x == {x} y == {y} location == {location["down"]}',file=sys.stderr, flush=True)
            if v['abs'] == x and v['ord'] == ( y - increaseUp ) and location.get('up') is None and ecart <= max:
                location['up'] = { 'distance' : dist, 'position' : f'{x} {y - increaseUp}', 'choose' : 'up', 'region' : v['region'] }
                #pprint(f'UP cible == {v["action"]} x == {x} y == {y} location == {location["up"]}',file=sys.stderr, flush=True)
        dist += 1
    #pprint(f'FIN getNearTarget LOCATION == {location}',file=sys.stderr, flush=True)
    return location

#taille de la carte pour init du jeu
largeur, hauteur = [int(i) for i in input().split()]

# init vars 
id = 0
tour = 0
killit = False


# game loop
while True:
    start_time = time.time()
    monMatos, sonMatos = [int(i) for i in input().split()]
    myboxes = 0
    hisboxes = 0
    herbe = 0
    idbuild = 0
    tosuck = []
    activeRobots = 0
    badRobots = 0
    robots = {}
    robotid = 0
    targets = {}
    builds = {}
    spawns = {}
    nbrecycler = 0
    todestroy = {}
    attack=[]
    defense=[]
    sizeMap = hauteur * largeur
    for y in range(hauteur):
        for x in range(largeur):
            
            # scrap_amount: facteur de disponibilité de la cas
            # owner: 1 = me, 0 = foe, -1 = neutral attribut case
            # units: mon nombre d'untié sur cette case 
            # recycler: présence d'un recycler si oui à 1
            # 
            scrap_amount, owner, units, recycler, can_build, can_spawn, in_range_of_recycler = [int(k) for k in input().split()]
            if owner == 1 :
                myboxes += 1
            elif owner == 0 :
                hisboxes += 1
            elif scrap_amount == 0:
                herbe += 1
            if can_build == 1 and recycler == 0 and owner == 1:
                idbuild += recycler
                builds[idbuild] = { 'action' : f'BUILD {x} {y}' }   
                builds[idbuild]['position'] = f'{x} {y}'  
                builds[idbuild]['region'] = getPositionRegion(hauteur,largeur, x, y )
                builds[idbuild]['owner'] = owner
            if  owner == 0 and units > 0 :
                badRobots += units
                id = f'{x}{y}'
                region = getPositionRegion(hauteur,largeur, x, y )
                todestroy[id] = {'abs':int(x), 'ord': int(y), 'action' : f'{x} {y}', 'region' : region, 'owner' : owner }
                attack.append({region:f'{x} {y}'})
            if units >= 1 and owner == 1 and tour == 0 :
                activeRobots += units
                robotid += 1
                robots[robotid] = {'from' : f'{x} {y}' }
                robots[robotid]['abs'] = x
                robots[robotid]['ord'] = y
                robots[robotid]['numberUnits'] = units 
                robots[robotid]['region'] = getPositionRegion(hauteur,largeur, x, y )     
                robots[robotid]['action'] = f'move 1 {robots[robotid]["from"]} {x} {y}'
                #print(f'init robots : { robots }',file=sys.stderr, flush=True)
            if units >= 1 and owner == 1 and tour > 0 :
                activeRobots += units
                posXY =  [ processedRobots[k]['from'] for k in processedRobots.keys() ]
                robotid += 1
                if f'{x} {y}' not in posXY :
                    robots[robotid] = {'from' : f'{x} {y}' }
                    robots[robotid]['abs'] = x
                    robots[robotid]['ord'] = y
                    robots[robotid]['numberUnits'] = units 
                    robots[robotid]['region'] = getPositionRegion(hauteur,largeur, x, y )     
                    robots[robotid]['action'] = f'move 1 {robots[robotid]["from"]} {x} {y}'
                    robots[robotid]['tour'] = tour
                    robots[robotid]['choose'] = 'wait'
            if owner < 1 and scrap_amount > 0 and recycler == 0 :
                id = f'{x}{y}'
                region = getPositionRegion(hauteur,largeur, x, y )
                targets[id] = {'abs':int(x), 'ord': int(y), 'action' : f'{x} {y}', 'region' : region, 'owner' : owner }     
                #pprint(f'{id} : { targets[id]["action"] }',file=sys.stderr, flush=True)
            if can_spawn == 1 and recycler == 0 and units == 0 :
                id = f'{x}{y}'
                spawns[id] = { 'action' : f'SPAWN 1 {x} {y}' }
                #pprint(f'{ spawns[id]  }',file=sys.stderr, flush=True) 
            if owner == 0 and ( x != 0 or y != 0 )  :
                regionE = getPositionRegion(hauteur,largeur,x,y)
                tosuck.append({regionE : f'{x} {y}'})
            if recycler == 1 and owner == 1 :
                nbrecycler += 1
    
    print(f'Robots Dispo on tour {tour} : { robots }',file=sys.stderr, flush=True)
    
    
    #
    # initizialisation des données de départ
    #

    if killit is False or tour > 190:
        touse = dict((k,v) for k, v in targets.items() if v['owner'] == -1 )
    else:
        touse = todestroy
    his = dict((k,v) for k, v in targets.items() if v['owner'] == 0 )
    myoccupation = ( myboxes / len(targets) ) * 100
    hisoccupation = (  hisboxes / len(targets) ) * 100
    free = ( ( len(touse) ) / len(targets) * 100 )

    if myoccupation - hisoccupation > 10 :
        cibles = {**todestroy,**touse}
        killit = True
    elif myoccupation - hisoccupation > 10 and ( len(targets) / 200 ) / ( activeRobots ) > 15 :
        cibles = {**todestroy}
        killit = True
    elif free < 5 and myoccupation - hisoccupation < -5 or killit is True:
        cibles = {**his,**todestroy}
    elif free > 30 and ( myoccupation - hisoccupation < -15 ) :
        cibles = {**his,**touse,**todestroy}
        killit = False
    elif free > 50 and myoccupation - hisoccupation > -5 and myoccupation - hisoccupation < 5 :
        cibles = {**his,**touse}
        killit = False
    else:
        cibles = {**touse,**his }
        killit = False
    
    boxByRegion = getBoxByRegion(cibles = cibles)
    #print(f'Taux de case par Region : {boxByRegion}', file=sys.stderr, flush=True)

    if tour > 0 :
        stats = getStatByRobots(robots = processedRobots)
    else :
        stats = {   'rigth' : 0 , 
            'left' : 0 , 
            'up' : 0 , 
            'down' : 0, 
            'wait' : 4,
            'figthers' : 0
        }
    
    #print(f'monMatos : {monMatos} vs sonMatos : {sonMatos} ', file=sys.stderr, flush=True)

    #
    #traitement des créatiosnd'untiées
    #

    spawn = ''
    if (( monMatos > sonMatos ) and ( monMatos > 10 )) or ( killit is True and monMatos > sonMatos  ) :
        for key in spawns.keys() :
            spawn += f'{ spawns[key]["action"] };'
            monMatos -= 10
            #pprint(f'SPAWN ROBOT { spawns[key]["action"] }',file=sys.stderr, flush=True)
            action = re.search('SPAWN 1 (\d+) (\d+)$', spawns[key]["action"] )
            x = action.group(1)
            y = action.group(2)
            if monMatos < 10 :
                break 
    spawns = {}
    
    #
    #traitement des unitées présente
    #

    config = { 'robots' : robots,
                'activeRobots' : activeRobots,
                'stats' : stats,
                'cibles' : cibles,
                'enemies' : attack,
                'hauteur' : hauteur,
                'largeur' : largeur,
                'boxByRegion' : boxByRegion
     }
    if tour == 0 :
        processedRobots = processRobots(config = config)
    else :
        processedRobots = processRobots(config = config, moves = moveByRobots )

    print(f'Robots Survivant on tour {tour} : {processedRobots}',file=sys.stderr, flush=True)
    #print(f'Process Robots : {robots}',file=sys.stderr, flush=True)
    move = ''
    for key in processedRobots.keys() :
        if len(processedRobots[key]['action']) > 0 :
            move += f"{ processedRobots[key]['action'] };"   
    #print(f'Processed Move : {move}',file=sys.stderr, flush=True)
    tmp = move.split(';')
    tmp.pop()
    moveByRobots = []
    for i in tmp :
        posXY = re.search('MOVE (\d) (\d+) (\d+) (\d+) (\d+)$', i )     
        x = posXY.group(4)
        y = posXY.group(5)
        moveByRobots.append(f'{x} {y}')

    #print(f'Store Move : {moveByRobots}',file=sys.stderr, flush=True)

    #
    #traitement des recyclers
    #

    build = ''
    #pprint(f'builds : {builds}', file=sys.stderr, flush=True)
    if ( herbe / sizeMap ) > 0.05  or tour > 20 :   
        if ( monMatos > 10 ) or (  activeRobots <= badRobots ) or ( killit is True or tour > 80):
            #pprint(f'taux herbe par robot : {herbe} {sizeMap} {( sizeMap - herbe ) / 4 }', file=sys.stderr, flush=True)
            #pprint(f'taux occupation par robots : {myoccupation / floor(activeRobots) } {nbrecycler}', file=sys.stderr, flush=True)
            if ( myboxes / sizeMap * 100 )  > nbrecycler or killit is True :
                for key in builds.keys() :
                    position = getBox(zone = tosuck,position = builds[key]["position"], recycling = True ) 
                    if position is not False :
                        build += f'BUILD { position };'
                        monMatos -= 10
                        #pprint(f'MonMatos : {monMatos}', file=sys.stderr, flush=True)
                        if monMatos < 10 :
                            break 
                            
    if ( f'{build}{spawn}{move}' != '' ) :
        #pprint(f"len de {build}{spawn}{move} = {len('{build}{spawn}{move}')}",file=sys.stderr, flush=True)
        print(f'{build}{spawn}{move}')
        #pprint(f'Active Robots : {activeRobots} Bad Robots : {badRobots}',file=sys.stderr, flush=True)
        #pprint( f'myoccupation : {myoccupation} hisoccupation : {hisoccupation}', file=sys.stderr, flush=True)
    elif ( f'{build}{spawn}{move}' == 'WAIT' ) :
        print(f'MESSAGE What\'s the fluck with my code ^-^ ?!?!?')

    print( f'Exec Time {time.time() - start_time}' ,file=sys.stderr, flush=True)    
    tour += 1
        