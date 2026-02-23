import sys # 시간 초과 뜰 때, 이거 먼저 고려하기
input=sys.stdin.readline # 시간 초과 뜰 때, 이거 먼저 고려하기
def binarySearch(a_list, num):
    start=0
    finish=len(a_list)-1
    mid=(start+finish)//2
    while start<=finish:
        if a_list[mid]==num:
            return 1
        elif a_list[mid]<num:
            start=mid+1
            mid=(start+finish)//2
        else:
            finish=mid-1
            mid=(start+finish)//2
    return 0


n=int(input())
a_list=list(map(int,input().split()))
a_list.sort()
m=int(input())
b_list=list(map(int,input().split()))

for i in range(m):
    if binarySearch(a_list, b_list[i]):
        print(1)
    else:
        print(0)