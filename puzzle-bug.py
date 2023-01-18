import sys

class isdefine :
  """What the fuck with prelouze Boa """
  def __init__(self,variable):
    if len(variable) == 0 : return None
  def get(variable) :
    if len(variable) == 0 :
        return False
    else :
        return variable
  def convInDictArrTuple(bible={}):
    oldTestament = {}
    for key,array in bible.items():
        elements = []
        while array:
            x = array.pop(0)
            elements.append(f'{x[0]} {x[1]}')
        oldTestament[key] = elements
    return oldTestament

def getNodeHorizontal(world={}, T=0 ) :
    result = {}
    idNode = 1
    nbNodes = world[0].count('0')
    end = len(world[0])
    absent = '-1 -1'
    print(f"getNodeHorizontal world of 1 lines of {end} box with {nbNodes} nodes", file=sys.stderr, flush=True)
    count = 0
    coordonate = []
    while count < end :
        print(f"getNodeHorizontal {world[0][count]} {count}", file=sys.stderr, flush=True)
        if world[0][count] == '0' :
            coordonate.append(f'{count} {T}')
            print(f"getNodeHorizontal add {count} {T} in {coordonate} ", file=sys.stderr, flush=True)
        count += 1
    count = 0
    while coordonate :
        result[idNode] = [coordonate[count],coordonate[count+1],absent] if len(coordonate) > 1 else [coordonate[count],absent,absent]
        print(f"getNodeHorizontal coordonate {coordonate} and index {count} > {len(coordonate)} : {result}", file=sys.stderr, flush=True)
        coordonate.pop(0)
        idNode += 1       
    return result

def getNodeVertical(world={}, T=0 ) :
    result = {}
    idNode = 1
    absent = '-1 -1'
    coordonate = []
    print(f"getNodeVertical processing {world}", file=sys.stderr, flush=True)
    for key,data in world.items() :
        if data[data.index('0')] == '0' :
            coordonate.append(f'{T} {key}')
            print(f"getNodeVertical add {T} {key} to {coordonate}", file=sys.stderr, flush=True)
    count = 0
    while coordonate :
        print(f"getNodeVertical {coordonate} {count}", file=sys.stderr, flush=True)
        result[idNode] = [coordonate[count],absent,coordonate[count+1]] if len(coordonate) > 1 else [coordonate[count],absent,absent]
        coordonate.pop(0)
        idNode += 1
      
    print(f"getNodeVertical End with {result}", file=sys.stderr, flush=True)
    return result

def getNodeComplex(world={} ) :
    idNode = 1
    result = {}
    #print(f"getNodeComplex with world Node {world}", file=sys.stderr, flush=True)
    bible = {}
    newTestament = {}
    #print(f'getNodeComplex {world} for writting bible dict setting', file=sys.stderr, flush=True)
    for y in range(0,len((list(world.keys())))) :
        line = []
        #print(f'getNodeComplex writting line {y} of dict {bible}', file=sys.stderr, flush=True)
        for x in range(0,len(world[y])) :
            line.append((x,y)) if world[y][x] == '0' else line.append((-1,-1))
        bible[y] = line 
        #print(f'getNodeComplex publishing line {y} of dict {bible}', file=sys.stderr, flush=True)
    print(f"getNodeComplex bible writted : {bible}", file=sys.stderr, flush=True)
    for line, coordonate in bible.items() :
        dcount = 0
        #print(f"getNodeComplex decalage de {dcount}", file=sys.stderr, flush=True)
        column = [ v[0] for k,v in bible.items() if k > line ]
        lineY = [ line for line in coordonate ] 
        filter = set([(-1,-1)])
        filterLlines = [a for a in lineY if a not in filter]
        #print(f"getNodeComplex column {column}", file=sys.stderr, flush=True)
        #print(f"getNodeComplex filterLlines {filterLlines}", file=sys.stderr, flush=True)
        while filterLlines : 
            node = filterLlines.pop(0) 
            decalage = node[0]
            column = [ v[decalage] for k,v in bible.items() if k > line ]
            #print(f"getNodeComplex decalage de {dcount}", file=sys.stderr, flush=True)  
            #print(f"getNodeComplex column {column}", file=sys.stderr, flush=True)
            #print(f"getNodeComplex node {node}", file=sys.stderr, flush=True)
            neighbour = filterLlines[0] if len(filterLlines) > 0 else (-1,-1)
            #print(f"getNodeComplex neighbour {neighbour}", file=sys.stderr, flush=True)
            filterColumns = [a for a in column if a not in filter]
            #print(f"getNodeComplex filterColumns {filterColumns}", file=sys.stderr, flush=True)
            down = filterColumns.pop(0) if len(filterColumns) > 0 else (-1,-1)
            #print(f"getNodeComplex down {down}", file=sys.stderr, flush=True)
            if isdefine(node) is not None and isdefine(neighbour) is not None and isdefine(down) is not None :
                result[idNode] = [node,neighbour,down]
                print(f"getNodeComplex resultat {[node,neighbour,down]}", file=sys.stderr, flush=True)
                idNode += 1    
    newTestament = isdefine.convInDictArrTuple(bible=result)
    print(f"getNodeComplex result {result}", file=sys.stderr, flush=True)
    print(f"getNodeComplex newTestament {newTestament}", file=sys.stderr, flush=True)
    return newTestament

def main():
    print(f"main Begin with world {world}", file=sys.stderr, flush=True)
    if width == 1 :
        print(f"main case for simple world of width {width}", file=sys.stderr, flush=True)
        result = getNodeVertical(world=world)      
        return result
    elif heigth == 1 :
        print(f"main case for simple world of heigth {heigth}", file=sys.stderr, flush=True)
        result = getNodeHorizontal(world=world)    
        return result       
    else :
        print(f"main case for complex world {world}", file=sys.stderr, flush=True)
        result = getNodeComplex(world=world)    
        return result 
# Don't let the machines win. You are humanity's last hope...
global width,heigth,world
world = {}
width = 6
heigth = 6
data = ['0.0..', '0.000', '0....', '0....', '0.000','0.0..']

for y in range(0,heigth):
    for x in data :
        world[y] = x

# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)
result = main()
print(f"Init result = {result}", file=sys.stderr, flush=True)
for nodeNumber, nodeData in result.items():
    print(f"Finaly Node {nodeNumber}", file=sys.stderr, flush=True)
    print(f"Neighbours {nodeData}", file=sys.stderr, flush=True)
    print(f"position {nodeData[0]} {nodeData[1]} {nodeData[2]}", file=sys.stderr, flush=True)
    print(f"{nodeData[0]} {nodeData[1]} {nodeData[2]}")
    # Three coordinates: a node, its right neighbor, its bottom neighbor
