t=int(input())

def vps(line):
    stack = []
    for i in line:
        if i == '(':
            stack.append(i)
        else:
            if stack == []:
                print("NO")
                return
            stack.pop(-1)
    if stack == []:
        print("YES")
    else:
        print("NO")

for i in range(t):
    line=list(input())
    vps(line)