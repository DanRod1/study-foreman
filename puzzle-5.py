import sys
import math
import re

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

message = input()
print(f"message is ... {message}", file=sys.stderr, flush=True)
# Write an answer using print
# To debug: 
binary = ''.join([format(ord(x),'b') for x in message])
print(f"binary is ... {binary}", file=sys.stderr, flush=True)
#encoded = ' '.join([ '0 0 ' if binary[x] == '1'  else '0' for x in range(0,len(binary)) ])

res = ' '.join(['0 '+'0'*x.count('1') if x.count('1')>=1 else '00 '+'0'*x.count('0') for x in re.findall("[1]+|[0]+", binary) ])
print(f"Debug ... {res}", file=sys.stderr, flush=True)

print(f"{res}")