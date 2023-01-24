import sys
import re

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

s = 'Hello world'

change_count = 4
print(f"Debug {change_count}", file=sys.stderr, flush=True)
tmp=list(s)

with open('raw.txt', 'r') as f:
    for line in f.readlines(): 
        raw_change = line
        deb,fin,car = raw_change.split('|')
        if int(fin) <= len(s)-1 :
            before = s[int(deb):int(fin)]
            change = s[int(fin)]+car
            after = s[int(fin)+1:len(s)]
            s = before + car + after
        else :
            new = s[int(deb):int(fin)]+car
            s = new
res= ''.join(tmp)
print(f"Debug {res} {tmp}", file=sys.stderr, flush=True)
# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

print(res)
