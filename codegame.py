import sys
import re
from math import ceil, pow, sqrt
import time


# debug formatage

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

#fonction perso
def chooseInNearList(choices = {}, robot = {}, herbes = [], used=[] ):
        possibleChoice = sorted(choices, key=choices.get('distance'))
        print(f'chooseInNearList :les choix le plus proches {possibleChoice} pour robot {robot}',file = sys.stderr, flush = True )
        print(f'chooseInNearList :les filtres used {used} et les herbes {herbes}',file = sys.stderr, flush = True )
        for i in possibleChoice:
            position = choices[i]['position']
            if position not in herbes and position not in used :
                robot['choose'] = i 
                robot['distance'] = choices[i]['distance']
                #print(f'chooseInNearList : Position { position } find for robot {robot}',file=sys.stderr,end="\n\n",flush=True)
                return position

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

def processRobots(config = {} ) :
    print(f'processRobots : DEBUT with config : {config}',file=sys.stderr,end="\n\n",flush=True)
    robots = config['robots']
    activeRobots = config['activeRobots']
    cibles = config['cibles']
    enemiesList = config['enemies']  
    used = []
    
    for index, key in enumerate(robots) :
        figthers = 0
        if tour == 0 :
            robots[key]['choose'] = 'wait'
        else :
            #print(f'processRobots Create figthers : {figthers}', file = sys.stderr, flush=True)
            tmp = [k for k,v in robots.items() if v['choose'] == 'figthers' ]
            figthers = len(tmp)
        posfrom = robots[key]['from']
        fabs, ford = [int(i) for i in posfrom.split()]        
        #print(f'processRobots Status Robots : {robots}', file = sys.stderr, flush=True)
        locateEnenmiesNear = getBox(zone = enemiesList,position = robots[key]['from'],filter = robots[key]['region'])
        trous = getBox(zone=tohell,statistics=True,position = robots[key]['from'],filter = robots[key]['region'])
        possible = dict((k,v) for k, v in cibles.items() if v['region'] == robots[key]['region'] )
        #print(f'processRobots : Case herbe à eviter par Region : {trous}', file = sys.stderr, flush=True)
        A = ['C','D']
        B = ['D','A']
        C = ['A','E']
        D = ['B','F']
        E = ['C','G','H']
        F = ['D','H']
        G = ['E','H']
        H = ['F','E']

        region = robots[key]['region']
        for nextregion in eval(region) :
            tmp = getBox(zone=tohell,position = robots[key]['from'],filter = nextregion, statistics = True) 
            newregion = { nextregion : len(tmp) }

        nextregion = sorted(newregion.items(), key=lambda x:x[0], reverse=True)
        print(f'processRobots :set de NextRegion si besoin : {nextregion[0][0]}',file = sys.stderr, flush = True )  
        print(f'processRobots : Cases Cibles disponibles  : {cibles}', file = sys.stderr, flush=True)
        action = f"MOVE 1"
        if len(trous) * ( 10 / 3 ) > len(possible)  :     
            near = getNearTarget( x = fabs, y = ford, target = cibles, region = nextregion[0][0],used = used ) 
            print(f'processRobots : Determination des Case NEAR {near}',file = sys.stderr, flush = True )
            destination = chooseInNearList(choices = near, robot = robots[key], herbes = trous, used = used )
            used.append(destination)
            robots[key]['region'] = nextregion[0][0]
            print(f'processRobots : Action change Regions for the robots {robots[key]}', file = sys.stderr, flush=True)
        elif index == len(robots) -1 :
            near = getNearTarget( x = fabs, y = ford, target = cibles,used = used )
            destination = chooseInNearList(choices = near, robot = robots[key], herbes = trous, used = used )
            used.append(destination)
            print(f'processRobots : Determination des Case NEAR {near}',file = sys.stderr, flush = True )  
            #print(f'Action if robots is the last for the Regions: {robots[key]}', file = sys.stderr, flush=True)     
        elif 0 >= (figthers * 100 / activeRobots ) < 10  or (figthers * 100 / activeRobots ) > 85 and  locateEnenmiesNear is not False :       
            robots[key]['choose'] = 'figthers'
            near = getNearTarget( x = fabs, y = ford, target = todestroy, used = used)
            print(f'processRobots : Determination des Case NEAR {near}',file = sys.stderr, flush = True )
            destination = chooseInNearList(choices = near, robot = robots[key], herbes = trous, used = used )
            used.append(destination)
            #print(f'processRobots : Action create Figther for  {robots[key]}',file = sys.stderr, flush = True )
        elif index > len(robots) - facteurBlitz :
            near = getNearTarget( x = fabs, y = ford, target = blitz, used = used )
            print(f'processRobots : Determination des Case NEAR {near}',file = sys.stderr, flush = True )
            destination = chooseInNearList(choices = near, robot = robots[key], herbes = trous, used = used )
            used.append(destination)
            #print(f'Action change for blitz War for robot: {robots[key]}', file = sys.stderr, flush=True)
        else:
            near = getNearTarget( x = fabs, y = ford, target = cibles, used = used )
            print(f'processRobots : Determination des Case NEAR  {near}',file = sys.stderr, flush = True )
            destination = chooseInNearList(choices = near, robot = robots[key], herbes = trous, used = used )
            used.append(destination)
            #print(f'processRobots : Action by default pour robot {robots[key]}', file = sys.stderr, flush=True)
        action += f' {robots[key]["from"]}'     
        if destination :
            action += f" {destination}"      

        print(f'processRobots : Action enregistré{ action } pour Robot {robots[key]}',file=sys.stderr,end="\n\n",flush=True)
        robots[key]['action'] = action
    print(f'processRobots : Fin with robots : {robots}',file=sys.stderr,end="\n\n",flush=True)        
    return robots

def getBox(zone=[], position = '', filter=None, recycling = False, statistics = False ) :
    x , y = [ int(i) for i in position.split()]
    if filter is not None :
        region = filter
    else:
        region = getPositionRegion(hauteur,largeur,x,y)
    
    historique = []

    #print(f'getBox : sizeMap à {sizeMap} avec recycling à {recycling} ',file=sys.stderr,end="\n\n",flush=True)
    for k,v in zone.items() :
        regionE = v['region']
        #print(f'getBox : avec un filtre sur REGION {regionE}',file=sys.stderr,end="\n\n",flush=True)
        posE = v['action']
        #print(f'getBox : POSITION recupérée {posE}',file=sys.stderr,end="\n\n",flush=True)
        if recycling is True :
            if region == regionE :
                xE , yE = [ int(i) for i in posE.split()]
                if ( yE - 1 == x ) or ( yE + 1 == x ) :
                    if statistics is True :
                        historique.append(f'{x} {y}')
                    else :
                        return f'{x} {y}'
        else:
            if region == regionE :
                xE , yE = [ int(j) for j in posE.split()]
                if xE - 1 == x and yE - 1 == y :
                    if statistics is True :
                        historique.append(f'{xE} {yE}')
                    else:
                        return f'{xE} {yE}'
                if xE == x and yE -1 == y :
                    if statistics is True :
                        historique.append(f'{xE} {yE}')
                    else:
                        return f'{xE} {yE}'
                if xE + 1 == x and yE -1 == y :
                    if statistics is True :
                        historique.append(f'{xE} {yE}')
                    else:
                        return f'{xE} {yE}'
                if xE -1 == x and yE == y :
                    if statistics is True :
                        historique.append(f'{xE} {yE}')
                    else:
                        return f'{xE} {yE}'
                if xE + 1 == x and yE == y:
                    if statistics is True :
                        historique.append(f'{xE} {yE}')
                    else:
                        return f'{xE} {yE}'
                if xE - 1 == x and yE + 1 == y :
                    if statistics is True :
                        historique.append(f'{xE} {yE}')
                    else:
                        return f'{xE} {yE}'
                if xE == x and yE + 1 == y :
                    if statistics is True :
                        historique.append(f'{xE} {yE}')
                    else:
                        return f'{xE} {yE}'
                if xE + 1 == x and yE + 1 == y:
                    if statistics is True :
                        historique.append(f'{xE} {yE}')
                    else:
                        return f'{xE} {yE}'
                else :
                    continue

    if statistics is True :
        return historique
    else:
        return False


def getPositionRegion(hauteur=0,largeur=0, x=0, y=0 ) :
    geoloc = ''
    largeur += 1
    hauteur +=1
    if ( y == 0 and x == 0 ) or ( y == 0 and (x / 2 >= largeur / 2 ) ):
        return 'B'
    elif y == 0 and ( x / 2 < largeur / 2 ) :
        return 'A'
    elif y == 0 and ( x >= largeur /2  ) :
        return 'B'
    if x <= ( 0.5 * largeur) and y <= ( 0.5 * hauteur ) and ( x / y ) > ( largeur / hauteur ):
        return 'A'
    if x <= ( 0.5 * largeur) and y <= ( 0.5 * hauteur ) and ( x / y ) <= ( largeur / hauteur ) :
        return 'C'
    if x > ( 0.5 * largeur) and y <= ( 0.5 * hauteur ) and ( x / y ) > ( largeur / hauteur / 2 ) :
        geoloc = 'B'
    if x > ( 0.5 * largeur ) and y <= ( 0.5 * hauteur ) and ( x / y ) <= ( largeur / hauteur / 2 ) :
        geoloc = 'D'
    if x <= ( 0.5 * largeur) and y > ( 0.5 * hauteur ) and ( x / y ) > ( largeur / 2 / hauteur ) :
        geoloc = 'E'
    if x <= ( 0.5 * largeur) and y > ( 0.5 * hauteur ) and ( x / y ) <= ( largeur / 2 / hauteur ) : 
        geoloc = 'G'
    if x > ( 0.5 * largeur) and y > ( 0.5 * hauteur ) and ( x / y ) > ( largeur / hauteur ) :
        geoloc = 'F'
    if x > ( 0.5 * largeur) and y > ( 0.5 * hauteur ) and ( x / y ) <= ( largeur / hauteur ) :
        geoloc = 'H'
    
    return geoloc

def getNearTarget( x=int(0), y=int(0), target = {}, region = None, used = [] ):
    max = sqrt((pow(largeur,2) + pow(hauteur,2)))
    print(f'getNearTarget : DEBUT avec une amplitude  max de {max}',file=sys.stderr,end="\n\n",flush=True)
    location = {}
    dist = 1
    print(f'getNearTarget : CIBLE du pannel existant et disponible{target}',file=sys.stderr,end="\n\n",flush=True)
    if region is not None :
        filterTarget = {}
        for k,v in target.items() :
            if v['region'] == region :
                filterTarget[k] = v
        target = filterTarget

    start = x - 3
    stop = x + 3
    rx = list(range(start,stop))
    start = y - 3
    stop = y + 3
    ry = list(range(start,stop))
    resultat = list()
    for i in rx:
        for j in ry :
            if i > 0 and j > 0 :
                resultat.append(f'{i} {j}')

    print(f'getNearTarget : deteminetion du perimeètre du robot {resultat}',file=sys.stderr,end="\n\n",flush=True)
    for k,v in target.items() :
        print(f'getNearTarget : parse target comparait au perimetre ==> {k}',file=sys.stderr,end="\n\n",flush=True)
        if k in resultat :
            ecart = getDistBet2Pts(a=f'{x} {y}',b=f'{v["abs"]} {v["ord"]}') 
            location = {tour:{}}
            if x - v["abs"] > 0 and y == v["ord"] :
                tmp = {'rigth' : v }
                location[tour].update(tmp)
                location[tour]['rigth'].update({'distance':ecart})
            elif x - v["abs"] < 0 and y == v["ord"] :
                tmp = {'left' : v }
                location[tour].update(tmp)
                location[tour]['left'].update({'distance':ecart})
            elif v["abs"] == 0 and y - v["ord"] > 0 :
                tmp = {'down' : v }
                location[tour].update(tmp)
                location[tour]['down'].update({'distance':ecart})
            elif v["abs"] == 0 and y - v["ord"] < 0 :
                tmp = {'up' : v }
                location[tour].update(tmp)
                location[tour]['up'].update({'distance':ecart})
            print(f'getNearTarget : choix après comparaison ==> {v} with {location[tour]} ',file=sys.stderr,end="\n\n",flush=True)
 
        dist += 1
    print(f'getNearTarget : Fin avec LOCATION ==> {location}',file=sys.stderr,end="\n\n",flush=True)
    return location

#taille de la carte pour init du jeu
global hauteur
global Largeur
largeur, hauteur = [int(i) for i in input().split()]

# init vars 
global tour
tour = 0
global killit
killit = False
global cibles
cibles = {}


# game loop
while True:
    start_time = time.time()
    monMatos, sonMatos = [int(i) for i in input().split()]
    myboxes = 0
    hisboxes = 0
    herbe = 0
    idbuild = 0
    tosuck = {}
    activeRobots = 0
    badRobots = 0
    robots = {}
    robotid = 0
    targets = {}
    builds = {}
    spawns = {}
    nbrecycler = 0
    todestroy = {}
    blitz = {}
    tohell = {}
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
                region = getPositionRegion(hauteur,largeur, x, y )
                myDomain = {f'{x} {y}' : region }
            elif owner == 0 :
                hisboxes += 1
            elif scrap_amount == 0:
                region = getPositionRegion(hauteur,largeur, x, y )
                data = {f'{x} {y}' : {'abs':int(x), 'ord': int(y), 'action' : f'{x} {y}', 'region' : region, 'owner' : owner }}
                tohell.update(data)
                #print(f'Init : Case herbe dans la map referencent les ennemis : {tohell}', file=sys.stderr, flush=True)              
            if can_build == 1 and recycler == 0 and owner == 1:
                idbuild = tour
                builds[idbuild] = { 'action' : f'BUILD {x} {y}' }   
                builds[idbuild]['position'] = f'{x} {y}'  
                builds[idbuild]['region'] = getPositionRegion(hauteur,largeur, x, y )
                builds[idbuild]['owner'] = owner
            if  owner == 0 and units > 0 and tour == 0 :
                data = { f'{x}{y}' : {'abs':int(x), 'ord': int(y), 'action' : f'{x} {y}', 'region' : region, 'owner' : owner } }
                blitz.update(data)
            if  owner == 0 and units > 0 and tour > 0 :
                badRobots += units
                data = { f'{x}{y}' : {'abs':int(x), 'ord': int(y), 'action' : f'{x} {y}', 'region' : region, 'owner' : owner } }
                region = getPositionRegion(hauteur,largeur, x, y )
                todestroy.update(data)
            if units >= 1 and owner == 1 and tour == 0 :
                activeRobots += units
                robotid += 1
                robots[robotid] = {'from' : f'{x} {y}' }
                robots[robotid]['abs'] = x
                robots[robotid]['ord'] = y
                robots[robotid]['numberUnits'] = units 
                robots[robotid]['region'] = getPositionRegion(hauteur,largeur, x, y )     
                robots[robotid]['action'] = f'move 1 {robots[robotid]["from"]} {x} {y}'
                #print(f'Init : recuperation des robots dispo : { robots }',file=sys.stderr,end="\n\n",flush=True)
            if units >= 1 and owner == 1 and tour > 0 :
                activeRobots += units
                posXY =  [ processedRobots[k]['from'] for k in processedRobots.keys() ]
                if f'{x} {y}' not in posXY :
                    robotid += 1
                    robots[robotid] = {'from' : f'{x} {y}' }
                    robots[robotid]['abs'] = x
                    robots[robotid]['ord'] = y
                    robots[robotid]['numberUnits'] = 1 
                    robots[robotid]['region'] = getPositionRegion(hauteur,largeur, x, y )     
                    robots[robotid]['action'] = f'move 1 {robots[robotid]["from"]} {x} {y}'
                    robots[robotid]['choose'] = 'wait'
            if 0 < owner or owner > 0  and scrap_amount > 0 and recycler == 0 :
                region = getPositionRegion(hauteur,largeur, x, y )
                data = { f'{x} {y}' : {'abs':int(x), 'ord': int(y), 'action' : f'{x} {y}', 'region' : region, 'owner' : owner }} 
                targets.update(data) 
                #print(f'Init : recuperation de pannel de cases : { data }',file=sys.stderr,end="\n\n",flush=True)
            if can_spawn == 1 and recycler == 0 and units == 0 :
                coordonnees = f'{x}{y}'
                spawns[coordonnees] = { 'action' : f'SPAWN 1 {x} {y}' }
                #print(f'Init : recuperation des case usine { coordonnees  }',file=sys.stderr,end="\n\n",flush=True) 
            if owner == 0 and ( x != 0 or y != 0 )  :
                region = getPositionRegion(hauteur,largeur,x,y)
                data = { f'{x} {y}' : {'abs':int(x), 'ord': int(y), 'action' : f'{x} {y}', 'region' : region, 'owner' : owner }}
                tosuck.update(tosuck)
                #print(f'Init : recuperation des case à spolier { coordonnees  }',file=sys.stderr,end="\n\n",flush=True)
            if recycler == 1 and owner == 1 :
                nbrecycler += 1
    
    print(f' Init : Robots En debut de tour {tour} : { robots }',file=sys.stderr,end="\n\n",flush=True)
    #
    #traitement des unitées présente
    #

    config = { 'robots' : robots,
                'activeRobots' : activeRobots,
                'cibles' : cibles,
                'enemies' : todestroy
     }
    
    processedRobots = processRobots(config = config)

    for k in processedRobots.keys() :
        print(f'main : Processed Robot on tour {tour} : {processedRobots[k]}',file=sys.stderr,end="\n\n",flush=True)

    
    #
    # initizialisation des données de départ
    #

    if killit is False or tour > 190:
        touse = dict((k,v) for k, v in targets.items() if 0 < v['owner'] > 0 )
    else:
        touse = todestroy
    his = dict((k,v) for k, v in targets.items() if v['owner'] == 0 )
    myoccupation = ( myboxes / len(targets) ) * 100
    hisoccupation = (  hisboxes / len(targets) ) * 100
    free = ( ( len(touse) ) / len(targets) * 100 )
    facteurBlitz = ceil(activeRobots * 0.3)

    if myoccupation - hisoccupation > 30 :
        cibles = {**todestroy,**touse}
        killit = True
    elif  activeRobots - badRobots > 5 and killit is True:
        cibles = {**todestroy}
        killit = True
    elif free < 5 or killit is True:
        cibles = {**his,**todestroy}
    elif free > 30 :
        cibles = {**his }
        killit = False
    elif 5 < myoccupation - hisoccupation > -5 and myoccupation - hisoccupation < 5 :
        cibles = {**his,**touse}
        killit = False
    else:
        cibles = {**touse }
        killit = False

    #
    #traitement des créatiosnd'untiées
    #

    spawn = ''
    if (( monMatos > sonMatos ) or ( monMatos > 10 )) or ( killit is True and monMatos > sonMatos  ) :
        for key in spawns.keys() :
            spawn += f'{ spawns[key]["action"] };'
            monMatos -= 10
            #print(f'main : Process des SPAWN ROBOT { spawns[key]["action"] }',file=sys.stderr,end="\n\n",flush=True)
            action = re.search('SPAWN 1 (\d+) (\d+)$', spawns[key]["action"] )
            x = action.group(1)
            y = action.group(2)
            if monMatos < 10 :
                break 
    spawns = {}
    

    move = ''
    for key in processedRobots.keys() :
        if len(processedRobots[key]['action']) > 0 :
            move += f"{ processedRobots[key]['action'] };"   
    print(f'main : Processed Move : {move}',file=sys.stderr,end="\n\n",flush=True)
    
    #
    #traitement des recyclers 
    #

    build = ''
    #print(f' main : Process des builds : {builds}', file=sys.stderr, flush=True)  
    if ( monMatos > 10 ) or (  activeRobots <= badRobots ) or ( killit is True or tour > 80):
        #print(f'main : taux herbe par robot : {herbe} {sizeMap} {( sizeMap - herbe ) / 4 }', file=sys.stderr, flush=True)
        #print(f'main : taux occupation par robots : {myoccupation / floor(activeRobots) } {nbrecycler}', file=sys.stderr, flush=True)
        if ( myboxes / sizeMap * 100 )  > nbrecycler or killit is True :
            for key in builds.keys() :
                position = getBox(zone = tosuck,position = builds[key]["position"], recycling = True ) 
                if position is not False :
                    build += f'BUILD { position };'
                    monMatos -= 10
                    #print(f'main : MonMatos : {monMatos}', file=sys.stderr, flush=True)
                    if monMatos < 10 :
                        break 
                            
    if ( f'{build}{spawn}{move}' != '' ) :
        #print(f"main : application des ordres : {build}{spawn}{move} = {len('{build}{spawn}{move}')}",file=sys.stderr,end="\n\n",flush=True)
        print(f'{build}{spawn}{move}')
    elif ( f'{build}{spawn}{move}' == 'WAIT' ) :
        print(f'MESSAGE What\'s the fluck with my code ^-^ ?!?!?')
    else:
         print(f'WAIT')

    print( f'Conclusion : temps Exec Time {time.time() - start_time}' ,file=sys.stderr,end="\n\n",flush=True)    
    tour += 1
        