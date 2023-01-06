import sys
from math import floor, ceil

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

# w: width of the building.
# h: height of the building.
global w,h,n,x,y,objectif,position
w, h = [int(i) for i in input().split()]
n = int(input())  # maximum number of turns before game over.
x, y = [int(i) for i in input().split()]
objectif = n
position = []
print(f"BOMBING params Init {w} {h} {n} {x} {y}", file=sys.stderr, flush=True)

def tower(order = '', X= 0, Y=0) :
    resultat = []
    if order == 'U' :
        pas = [yy for yy in range(0,Y,n)]
        resultat = pas[-2]
        print(f"BOMBING ordre {order} pas {pas}", file=sys.stderr, flush=True)
        print(f'BOMBING resultat {resultat}',file=sys.stderr, flush=True)
    elif order == 'D' :
        pas = [yy for yy in range(Y,h,n)]
        resultat = y + pas[1]
        print(f"BOMBING ordre {order} pas {pas}", file=sys.stderr, flush=True)
        print(f'BOMBING resultat {resultat}',file=sys.stderr, flush=True)
    position = [X,resultat]
    return position

def speed(order = '', X = 0, Y = 0) :
    if Y == 0 :
        Y += 1
        X += 1
    if X == 0 :
        X += 1
        Y += 1
    q = ( X // Y )

    if q < 1 :
        pente = ( X // Y )
    else :
        pente = ( Y // X )
    
    if pente == 0 :
        pente = 1
    resultat = []
    if ( pente == 1 ) :
        y = tower(order=order, X=X, Y=Y)
        position = [X,Y]
        return position
    if order == 'U' :
        pas = [yy for yy in range(0,Y,pente)]
        resultat = pas[-1]
        position = [x,resultat]
    if order == 'D' :
        pas = [yy for yy in range(Y,h,pente)]
        resultat = pas[1]
        position = [x,resultat]
    if order == 'L' :
        pas = [xx for xx in range(0,X,pente)]
        resultat = pas[-1]
        position = [resultat,y]
    if order == 'R' :
        pas = [xx for xx in range(X,w,pente)]
        resultat = pas[1]
        position = [resultat,Y]
    if order == 'UR' :
        pas = [xx for xx in range(X,w,pente)]
        print(f"BOMBING Speed pas : {pas} pente : {pente}", file=sys.stderr, flush=True)
        resultat = pas[-1]
        print(f"BOMBING Speed position x : {resultat}", file=sys.stderr, flush=True)
        couple= [resultat]
        pas = [yy for yy in range(0,Y,pente)]
        print(f"BOMBING Speed pas : {pas} pente : {pente}", file=sys.stderr, flush=True)
        resultat = pas[-1]
        print(f"BOMBING Speed position y : {resultat}", file=sys.stderr, flush=True)
        position.append(resultat)
    if order == 'UL' :
        pas = [xx for xx in range(0,X,pente)]
        resultat = pas[-1]
        couple = [resultat]
        pas = [yy for yy in range(0,Y,pente)]
        resultat = pas[-1]
        couple.append(resultat)
    if order == 'DR' :
        pas = [xx for xx in range(X,w,pente)]
        print(f"BOMBING Speed pas : {pas} pente : {pente}", file=sys.stderr, flush=True)
        resultat = pas[-1]
        print(f"BOMBING Speed position x : {resultat}", file=sys.stderr, flush=True)
        position = [resultat]
        pas = [yy for yy in range(Y,h,pente)]
        print(f"BOMBING Speed pas : {pas} pente : {pente}", file=sys.stderr, flush=True)
        resultat = pas[-1]
        print(f"BOMBING Speed position y : {resultat}", file=sys.stderr, flush=True)
        position.append(resultat)     
    if order == 'DL' :
        pas = [xx for xx in range(0,X,pente)]
        resultat = pas[-1]
        position = [resultat]
        pas = [yy for yy in range(Y,h,pente)]
        resultat = pas[-1]
        position.append(resultat)  
    return position

def coupe(  order = '', X= 0, Y=0) :
    tours = [t for t in range((n * -1),0)]
    if tours[0] == ( n * -1 ) :
        posX = w / 2
        posY = h / 2
        couple = (posX,posY)
    else :
        couple = speed( order = order, X=X, Y=Y) 
    
    return couple

# game loop

while True:
    bomb_dir = input()  # the direction of the bombs from batman's current location (U, UR, R, DR, D, DL, L or UL)
    coast= {
        'AUTO': {
            'Speed' : {'xy' : speed},
            'Coupe' : {'xy' : coupe},
            'Tower' : {'y' : tower }
        },
        'U' : {
            'Building' : {'x' : 0, 'y' : -1}
        },
        'D' : {
            'Building' :{'x' : 0, 'y' : 1 }
        },
        'L' : {
            'Building' : {'x' : -1, 'y': 0 }
        },
        'R' : {
            'Building' : {'x' : 1, 'y' : 0}
        },
        'UR' : {
            'Building' : {'x' : 1  , 'y' : -1 }
        },
        'UL' :{
            'Building' : {'x' : -1 , 'y' : -1 }
        },
        'DR' : {
            'Building' : {'x' : 1, 'y' : 1}
        },
        'DL' : {
            'Building' : {'x' : 1, 'y' : -1 }
        }
    }

    if w == 1 :
        calculs = coast['AUTO']['Tower']['y'](order = bomb_dir, X=x, Y=y )
        x, y = [int(c) for c in calculs ]
        print(f"Tower result {x} {y} {bomb_dir}", file=sys.stderr, flush=True)
    elif w != h and (w * h) > objectif :
        calculs = coast['AUTO']['Speed']['xy'](order = bomb_dir, X=x, Y=y)
        x, y = [int(c) for c in calculs ]
        print(f"Speed result {x} {y} {bomb_dir}", file=sys.stderr, flush=True)
    elif w == h:
        calculs = coast['AUTO']['Coupe']['xy'](order = bomb_dir, X=x, Y=y)
        x, y = [int(c) for c in calculs ]
        print(f"Coupe result {x} {y} {bomb_dir}", file=sys.stderr, flush=True)
    else :
        x += coast[bomb_dir]['Building']['x']
        y += coast[bomb_dir]['Building']['y']
        print(f"Building result {x} {y} {bomb_dir}", file=sys.stderr, flush=True)
    n -= 1

    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)
    #print(f"BOMBING a read dictionnary is always elegant {coast[bomb_dir]}", file=sys.stderr, flush=True)
    print(f"Apply New position : {x} {y}", file=sys.stderr, flush=True)


    # the location of the next window Batman should jump to.
    print(f'{x} {y}')
