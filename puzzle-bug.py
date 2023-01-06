import sys

def getNodeNeigbour(data='',chain='', nbline = 0, init = False ) :
    resultat = ''
    x = 0
    end = len(line)
    print(f"getNodeNeigbour data = {data} chain = {chain}", file=sys.stderr, flush=True)
    while x < end :
        if data[0:2] == chain and init == True:
            resultat += f'{x} {nbline} '
            x += 1
            resultat += f'{x} {nbline}'
            x += 1
            return resultat
        elif data[0:2] == chain and init == False:
            resultat += f'{x} {nbline}'
            x += 1    
            return resultat        
        else :
            x += 2
            data = data[2:end]
        print(f"getNodeNeigbour END = {end} X = {x}", file=sys.stderr, flush=True)
    print(f"getNodeNeigbour Resultat : {resultat}", file=sys.stderr, flush=True)
    if len(resultat) == 0 :
        return False

# Don't let the machines win. You are humanity's last hope...

width = int(input())  # the number of cells on the X axis
height = int(input())  # the number of cells on the Y axis

lines = []
for i in range(height):
    line = input()  # width characters, each either 0 or .
    lines.append(line)

print(f"main {lines}", file=sys.stderr, flush=True)

firstFind = False
y = 0
for line in lines :
    print(f"main line  = '{line}'", file=sys.stderr, flush=True)
    first = getNodeNeigbour(data=line,chain='00',nbline=y,init=True)
    if first is not False :
        print(f"main First = '{first}' firstFind = {firstFind} ", file=sys.stderr, flush=True)
        if firstFind is False :
            firstFind = True
            nodeRigth = first
            print(f"main nodeRigth = '{nodeRigth}' firstFind = {firstFind} ", file=sys.stderr, flush=True)
    down = getNodeNeigbour(data=line,chain='0.',nbline=y)
    print(f"main down = '{down}'", file=sys.stderr, flush=True)
    if down is not False and firstFind is True :
        print(f"main 'break'", file=sys.stderr, flush=True)
        break
    y += 1


# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

# Three coordinates: a node, its right neighbor, its bottom neighbor
print(f'{nodeRigth} {down}')
