import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())  # the number of temperatures to analyse
data = {}
data['positif'] = []
data['negatif'] = []
data['null'] = []
isnegatif = False
ispositif = False
isnull = False
isboth = False
for i in input().split():
    # t: a temperature expressed as an integer ranging from -273 to 5526
    t = int(i)
    if t >= 0 :
        data['positif'].append(t)
    elif t <= 0:
        data['negatif'].append(t)

# Write an answer using print

tmp = [ x for x in sorted(data['negatif'],reverse=True) ]
data['negatif'] = tmp
if len(data['negatif']) > 0 : isnegatif = True
tmp = [ x for x in sorted(data['positif'])]
data['positif'] = tmp
if len(data['positif']) > 0 : ispositif = True
tmp = [ x for x in sorted(data['null'])]
if isnegatif is True and ispositif is True :
    plus = len([ x for x in range(0,data['positif'][0]) ])
    moins = len([ x for x in range(data['negatif'][0],0) ])
    print(f" plus {plus} moins {moins} ", file=sys.stderr, flush=True)
    isBoth = True
print(f"data {data} isnegatif {isnegatif} ispositif {ispositif}", file=sys.stderr, flush=True)

if isboth is True :
    resultat = data['positif'][0] if plus < moins else data['negatif'][0]
    print(f"result du to isboth {plus} and {moins}", file=sys.stderr, flush=True)
elif isnegatif is True and ispositif is False :
    resultat = data['negatif'][0] 
    print(f"I am negatif { data['negatif'][0] } ", file=sys.stderr, flush=True)
elif ispositif is True and isnegatif is True:
    resultat = data['positif'][0] 
    print(f"I am ispositif { data['positif'][0] } ", file=sys.stderr, flush=True)
else :
    resultat = 0

print(f"{resultat}")
