n,m=map(int,input().split())
guide={}
for i in range(n):
    guide[i+1]=input()

for i in range(m):
    question=input()
    if question.isalpha():
        print(guide.key(question))
    else:
        print(guide[int(question)])