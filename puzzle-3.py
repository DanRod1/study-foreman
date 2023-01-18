import sys
import re
from math import ceil
import numpy as np

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

def getNodeExemple(world={} ) :
    result = {}
    idNode = 1
    bottom = len(world.keys())
    print(f"getNodeExemple world of {bottom} lines", file=sys.stderr, flush=True)
    for y,data in world.items() :
        count = 0
        print(f"getNodeExemple processing line {y} and columns of {len(data)}", file=sys.stderr, flush=True)
        while count < len(data) :
            print(f"getNodeExemple processing column {count} of data '{data}'", file=sys.stderr, flush=True)
            if data[count] == '0' :
                print(f"getNodeExemple processing column {count} with '{data[count]}'", file=sys.stderr, flush=True)
                first = f'{count} {y}'
                rigth = f'{count+1} {y}' if data[count+1:count+2] == '0' else '-1 -1'
                if y+1 < bottom :
                    down = f'{count} {y+1}' if world[y+1][count] == '0' else '-1 -1'
                else: 
                    down = '-1 -1'
                result[idNode] = [first,rigth,down]
                del first
                del rigth
                del down
                idNode += 1
            count += 1
            print(f"getNodeExemple world set with {result}", file=sys.stderr, flush=True)
    return result

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

def getNodeCarre(world={} ) :
    idNode = 1
    absent = '-1 -1'
    sheet = {}
    lines = 0
    for key,data in world.items() :
        datas=list(data)
        if '0' in datas : lines += 1 
        print(f"getNodeCarre  processing {data} => {datas}", file=sys.stderr, flush=True)
        nodeX = 0
        while  datas :
            cordonates = []
            if '0' in datas and datas.index('0') == 0 :
                cordonates.append(f'{nodeX} {key}')
                sheet[idNode] = cordonates
                print(f"getNodeCarre create cordonate {cordonates} in sheet", file=sys.stderr, flush=True)
                idNode += 1
            nodeX += 1
            datas.pop(0)
    print(f"getNodeCarre sheet is {sheet}", file=sys.stderr, flush=True)
    step = len(sheet.keys()) // lines
    for key,data in sheet.items() :
        if key < step :
            data.append(sheet[key+1][0]) 
        else :
            data.append(absent)
            step *= 2
        print(f"getNodeCarre update with right cordonate in {sheet} {len(sheet.keys())} // {lines}", file=sys.stderr, flush=True)
    
    step = len(sheet.keys()) // lines
    for key,data in sheet.items() :
        if key <= step :
            data.append(sheet[key+step][0]) 
        else :
            data.append(absent)
            if lines < step : step *= 2 
        print(f"getNodeCarre update with down cordonate in {sheet} {len(sheet.keys())} // {lines}", file=sys.stderr, flush=True)
    print(f"getNodeCarre End with {sheet}", file=sys.stderr, flush=True)
    return sheet

def getNodeT(world={} ) :
    tmp = {k:v for k,v in world.items() if k == 0}
    line = getNodeHorizontal(world=tmp)
    down = ceil(len(line.keys())/2)
    print(f"getNodeT call with getNodeHorizontal with world {tmp} line {line} with intersection on {down}", file=sys.stderr, flush=True)
    tmp = {k:v for k,v in world.items() if k > 0}
    T = tmp[1].index('0')
    column = getNodeVertical(world=tmp, T=T)
    print(f"getNodeT call with getNodeVertical with world {tmp} and column {column} and T {T}", file=sys.stderr, flush=True)

    idNode = 1
    result = {}
    print(f"getNodeT merging line {line} and column {column}", file=sys.stderr, flush=True)
    for key,data in line.items() :
        print(f"getNodeT should replace at line id {down} value {column[1][0]}", file=sys.stderr, flush=True)
        if key == down :
            print(f"getNodeT replace done ", file=sys.stderr, flush=True)
            replace = column[1][0]
            data[-1] = replace
            result[idNode] = data
        else :
            print(f"getNodeT add {data} to {result} done ", file=sys.stderr, flush=True)
            result[idNode] = data
        idNode += 1
    for key,data in column.items() :
        print(f"getNodeT add {data} to {result} done ", file=sys.stderr, flush=True)
        result[idNode] = data
        idNode += 1

    return result       

def getNodeDiag(world={} ) :
    idNode = 1
    result = {}
    nbNodes = [ k for k,v in world.items() if v.count('0') >= 1 ]
    print(f"getNodeDiag with number Node {len(nbNodes)}", file=sys.stderr, flush=True)
    for key in world.keys():
        coordonates = []
        index = nbNodes.pop(0)
        coordonates.append(f'{index} {key}')
        coordonates.append(f'-1 -1')
        coordonates.append(f'-1 -1')
        result[idNode] = coordonates
        idNode += 1
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
        for x in range(0,len((list(world.keys())))) :
            line.append((x,y)) if world[y][x] == '0' else line.append((-1,-1))
        bible[y] = line 
        #print(f'getNodeComplex publishing line {y} of dict {bible}', file=sys.stderr, flush=True)
    print(f"getNodeComplex bible writted : {bible}", file=sys.stderr, flush=True)
    for line, coordonate in bible.items() :
        dcount = 0
        #print(f"getNodeComplex decalage de {dcount}", file=sys.stderr, flush=True)
        column = [ v[0] for k,v in bible.items() if k > line ]
        lineY = [ coordonate[line] for line in range(0,len(list(bible.keys()))) ] 
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
    if len(list(np.unique([v for k,v in world.items() if v.count('0') > 0 ]))) == 1:
        carre = True
    else:
        carre = False
    nbNodes = 0
    for x in [v.count('0') for k,v in world.items() if v.count('0') > 0 ]:
        nbNodes += x

    print(f"main Begin with world {world}", file=sys.stderr, flush=True)
    if width == 2 :
        print(f"main case for simple world of width {width}", file=sys.stderr, flush=True)
        result = getNodeExemple(world=world)      
        return result
    elif heigth == 1 :
        print(f"main case for simple world of heigth {heigth}", file=sys.stderr, flush=True)
        result = getNodeHorizontal(world=world)    
        return result       
    elif width == 1 :
        print(f"main case for simple world of heigth {heigth}", file=sys.stderr, flush=True)
        result = getNodeVertical(world=world)    
        return result   
    elif carre is True :
        print(f"main case for simple world carre", file=sys.stderr, flush=True)
        result = getNodeCarre(world=world)    
        return result 
    elif [re.findall(r'[0?]',v) for k,v in world.items() if '0' in list(v) ][0].count('0') > 1 and [re.findall(r'[0?]',v) for k,v in world.items() if '0' in list(v) ][1].count('0') == 1 :
        print(f"main case for simple T world", file=sys.stderr, flush=True)
        result = getNodeT(world=world)
        return result
    elif [ k for k,v in world.items() if v.count('0') == 1 ] == list(world.keys()) :
        print(f"main case for simple Diag world", file=sys.stderr, flush=True)
        result = getNodeDiag(world=world)
        return result
    else :
        print(f"main case for complex world {world} {nbNodes}", file=sys.stderr, flush=True)
        result = getNodeComplex(world=world)    
        return result 
# Don't let the machines win. You are humanity's last hope...
global width,heigth,world
width = int(input())  # the number of cells on the X axis
heigth = int(input())  # the number of cells on the Y axis
world = {}

for i in range(heigth):
    line = input()  # width characters, each either 0 or .
    world[i] = line

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

