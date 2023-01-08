import sys

def getNodes(chain='',start=0, y=0 ) :
    result = ''
    end = len(chain)
    print(f"getNodeNeigbour chain = {chain} start = {start}", file=sys.stderr, flush=True)
    if chain[start:start+1] == '0' and start <= end:
        result += f'{start} {y}'
        print(f"getNodeNeigbour find result = {result}", file=sys.stderr, flush=True)
        return result
    else:
        result += '-1 -1'

def main():
    result = {}
    bottom = len(world.keys())
    print(f"main Begin world of {bottom} lines", file=sys.stderr, flush=True)
    for y,data in world.items() :
        count=0
        node = []
        print(f"main Begin on line '{y}'", file=sys.stderr, flush=True)
        print(f"main Begin on postion {count} with data = {data}", file=sys.stderr, flush=True)
        if data[count:count+1] == '0' :
            init = f'{count} {y}'
            print(f"main find Init Node in {count} {y} ", file=sys.stderr, flush=True)
            node.append(init)
        if data[count+1:count+2] == '0' and 'init' in locals() :
            right = getNodes(chain=data,start=count+1)
            node.append(right)
            print(f"main find Right Node in {count+1} {y} ", file=sys.stderr, flush=True)
        if data[count:count+1] == '0' and 'init' in locals() and 'right' in locals():
            if y+1 < bottom :
                down = getNodes(chain=world[y+1],start=count,y=y+1)
                node.append(down)
                print(f"main find Down Node {down} in {world[y+1]} in start {count} ", file=sys.stderr, flush=True)
            else :
                node.append('-1 -1')
                print(f"main find Down Node {down} in {world[y]} in start {count} ", file=sys.stderr, flush=True)
        if len(node) == 3 and len(node) > 1:
            print(f"main End processing line {data} with result = {node}", file=sys.stderr, flush=True)
            result[count] = node
            print(f"main save node in result = {result}", file=sys.stderr, flush=True)   
            del init 
            del right
            del down
        elif len(node) >= 1 :
            for i in range(1,3) :
                node.append('-1 -1')
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

# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)
result = main()
for line,data in result.items():
    print(f"Finaly print Nodes Friends = {data}", file=sys.stderr, flush=True)
    print(f'{data[0]} {data[1]} {data[2]}')
    # Three coordinates: a node, its right neighbor, its bottom neighbor

