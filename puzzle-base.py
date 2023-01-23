import sys
import math


l = int(input())
h = int(input())
t = input()
for i in range(h):
    # create input()
    row = input()
    t = t.upper()
    outp = ""
    for subt in t:
        i = 0
        while i < l:
            ordn = ord(subt)
            if ordn > 91 or ordn < 65: ordn = 91
            n = (ordn-65)*l
            
            outp += row[n+i]
            i += 1
# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)
    print(outp)