import sys
import math
input=sys.stdin.readline

a,b,v=map(int, input().split())

v=v-a
print(1+math.ceil(v/(a-b)))