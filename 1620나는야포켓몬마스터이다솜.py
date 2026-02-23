#import sys
#input=sys.stdin.readline

n,m=map(int,input().split())
dogam = []
reverse_dogam = {}

for i in range(n):
    name=input()
    dogam.append(name)
    reverse_dogam[name]=i+1

for i in range(m):
    question=input()
    if question.isdigit():
        print(dogam[int(question)-1])
    else:
        print(reverse_dogam[question])