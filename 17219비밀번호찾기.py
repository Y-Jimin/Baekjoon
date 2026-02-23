n,m = map(int,input().split())
password = {}

for i in range(n):
    comp, pw = input().split()
    password[comp] = pw

for j in range(m):
    print(password[input()])