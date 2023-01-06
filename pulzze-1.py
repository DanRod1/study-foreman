import sys
from math import floor, ceil

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

# w: width of the building.
# h: height of the building.
global w,h,n,x,y,objectif
w, h = [int(i) for i in input().split()]
n = int(input())  # maximum number of turns before game over.
x, y = [int(i) for i in input().split()]
objectif = n
print(f"BOMBING params Init {w} {h} {n} {x} {y}", file=sys.stderr, flush=True)





def tower(order = '') :
    if order == 'U' :
        pas = [yy for yy in range(0,y,n)]
        resultat = pas[-2]
    elif order == 'D' :
        pas = [yy for yy in range(y,h,n)]
        resultat = y + pas[1]
    print(f"BOMBING ordre {order} pas {pas}", file=sys.stderr, flush=True)
    print(f'BOMBING resultat {resultat}',file=sys.stderr, flush=True)
    return resultat

def speed(order = '') :
    if y == 0 :
        fx = x + 1
        fy = x + 1
        q = ( fx // fy )
    else :
        q = ( x // y )

    if q < 1 and y == 0:
        pente = ( fy // fx )
    elif q < 1 and y != 0 :
        pente = ( y // x ) 
    elif q > 1 and ( y == 0 ):
        pente = ( fx // fy )
    else :
        pente = (x // y )

    if order == 'U' :
        pas = [yy for yy in range(0,y,pente)]
        resultat = pas[-1]
        couple = [x,resultat]
    if order == 'D' :
        pas = [yy for yy in range(y,h,pente)]
        resultat = pas[1]
        couple = [x,resultat]
    if order == 'L' :
        pas = [xx for xx in range(0,x,pente)]
        resultat = pas[-1]
        couple = [resultat,y]
    if order == 'R' :
        pas = [xx for xx in range(x,w,pente)]
        resultat = pas[1]
        couple = [resultat,y]
    if order == 'UR' :
        pas = [xx for xx in range(x,w,pente)]
        resultat = pas[-1]
        couple= [resultat]
        pas = [yy for yy in range(0,y,pente)]
        resultat = pas[-1]
        couple.append(resultat)
    if order == 'UL' :
        pas = [xx for xx in range(0,x,pente)]
        resultat = pas[-1]
        couple = [resultat]
        pas = [yy for yy in range(0,y,pente)]
        resultat = pas[-1]
        couple.append(resultat)
    if order == 'DR' :
        pas = [xx for xx in range(x,w,pente)]
        print(f"BOMBING Speed pas : {pas} pente : {pente}", file=sys.stderr, flush=True)
        resultat = pas[-1]
        print(f"BOMBING Speed position x : {resultat}", file=sys.stderr, flush=True)
        couple = [resultat]
        pas = [yy for yy in range(y,h,pente)]
        print(f"BOMBING Speed pas : {pas} pente : {pente}", file=sys.stderr, flush=True)
        resultat = pas[-1]
        print(f"BOMBING Speed position y : {resultat}", file=sys.stderr, flush=True)
        couple.append(resultat)     
    if order == 'DL' :
        pas = [xx for xx in range(0,x,pente)]
        resultat = pas[-1]
        couple = [resultat]
        pas = [yy for yy in range(y,h,pente)]
        resultat = pas[-1]
        couple.append(resultat)  
    return couple

def coupe(  order = '') :
    tours = [t for t in range((n * -1),0)]
    if tours[0] == ( n * -1 ) :
        posX = w / 2
        posY = h / 2
        couple = (posX,posY)
    else :
        couple = speed( order = order) 
    
    return couple


# game loop

while True:
    bomb_dir = input()  # the direction of the bombs from batman's current location (U, UR, R, DR, D, DL, L or UL)
    coast= {
        'AUTO': {
            'Speed' : {'xy' : speed},
            'Tower' : {'y' : tower },
            'Coupe' : {'xy' : coupe }
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
        y = coast['AUTO']['Tower']['y'](order = bomb_dir )
        x = 0
        print(f"Tower result {x} {y}", file=sys.stderr, flush=True)
    elif ( w / h * objectif ) < w and ( w / h * objectif ) < h :
        calculs = coast['AUTO']['Speed']['xy'](order = bomb_dir)
        x, y = [int(c) for c in calculs ]
        print(f"Speed result {x} {y}", file=sys.stderr, flush=True)
    elif ( w * h / objectif ) > w + h :
        calculs = coast['AUTO']['Coupe']['x'](order = bomb_dir)
        x, y = [int(c) for c in calculs ]
        print(f"Coupe result {x} {y}", file=sys.stderr, flush=True)
    else :
        x += coast[bomb_dir]['Building']['x']
        y += coast[bomb_dir]['Building']['y']
        print(f"Building result {x} {y}", file=sys.stderr, flush=True)
    n -= 1

    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)
    print(f"BOMBING a read dictionnary is always elegant {coast[bomb_dir]}", file=sys.stderr, flush=True)
    print(f"Apply New position : {x} {y}", file=sys.stderr, flush=True)


    # the location of the next window Batman should jump to.
    print(f'{x} {y}')
