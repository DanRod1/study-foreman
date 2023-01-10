import sys

def getNodes(chain='',start=0, y=0 ) :
    result = ''
    end = len(chain)
    print(f"getNodeNeigbour chain = {chain} start = {start}", file=sys.stderr, flush=True)
    if chain[start:start+1] == '0' :
        result += f'{start} {y}'
        print(f"getNodeNeigbour find result = {result}", file=sys.stderr, flush=True)
        return result
    elif start+1 > end :
        result += '-1 -1'
        return result
    else:
        result += '-1 -1'
        return result

def main():
    result = {}
    idNode = 1
    bottom = len(world.keys())
    print(f"main Begin world of {bottom} lines", file=sys.stderr, flush=True)
    for y,data in world.items() :
        count=0
        end = len(data)
        print(f"main Begin on line '{y}'", file=sys.stderr, flush=True)
        print(f"main Begin on postion {count} with data = {data}", file=sys.stderr, flush=True)
        node = []
        while count <= end :
            print(f"main processing data on position {count} of set {data} end = {end}", file=sys.stderr, flush=True)
            done = 0
            if data[count:count+1] == '0' :
                init = f'{count} {y}'
                print(f"main find Init Node in {count} line = {y} ", file=sys.stderr, flush=True)
                node.append(init)
                print(f"main Node in {node}", file=sys.stderr, flush=True)
                right = getNodes(chain=data[count:len(data)],start=count+1)
                print(f"main Add rigth neigbour in {node}", file=sys.stderr, flush=True)
                node.append(right)
                print(f"main setting Node at right store on {node}", file=sys.stderr, flush=True)
                if y+1 < bottom :
                    down = getNodes(chain=world[y+1],start=count,y=y+1)
                    print(f"main setting Node {down} for downstare find in {world[y+1]} at position {count} ", file=sys.stderr, flush=True)
                    node.append(down)
                    print(f"main setting Node at right store on {node}", file=sys.stderr, flush=True)
                elif y+1 == bottom :
                    down = '-1 -1'
                    print(f"main undeWorld is hell setting '-1 -1' on {node}", file=sys.stderr, flush=True)
                    node.append(down)
                    print(f"main undeWorld store'-1 -1' on {node}", file=sys.stderr, flush=True)
                done += 1
                print(f"main great only {done} node done", file=sys.stderr, flush=True)
            elif data[count:count+1] == '.' :
                print(f"main find '{data[count]}' on position {count} of data {data} next processing data are {data[count+1:end]}", file=sys.stderr, flush=True)
                count += 1
            if len(node) == 3 and done == 1 :
                tmp={f'{idNode}': list(node) }
                result.update(tmp)
                print(f"main one Node process at position {count} of data = {data} setting {tmp} to result", file=sys.stderr, flush=True)
                print(f"main save node in result = {result}", file=sys.stderr, flush=True) 
                idNode += 1
                node = []
            count += 1
    print(f"main End with result = {result}", file=sys.stderr, flush=True)
    return result

# Don't let the machines win. You are humanity's last hope...
global width,heigth,world
width = int(input())  # the number of cells on the X axis
height = int(input())  # the number of cells on the Y axis
world = {}

for i in range(height):
    line = input()  # width characters, each either 0 or .
    world[i] = line
    
print(f"main Begin world = {world}", file=sys.stderr, flush=True)

# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)
result = main()
print(f"Runlevel result = {result}", file=sys.stderr, flush=True)
for nodeNumber, nodeData in result.items():
    print(f"Finaly Node {nodeNumber}", file=sys.stderr, flush=True)
    print(f"Neighbours {nodeData}", file=sys.stderr, flush=True)
    print(f"position {nodeData[0]} {nodeData[1]} {nodeData[2]}", file=sys.stderr, flush=True)
    print(f"{nodeData[0]} {nodeData[1]} {nodeData[2]}")
    # Three coordinates: a node, its right neighbor, its bottom neighbor

