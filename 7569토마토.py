m, n, h = map(int, input().split())

# 3차원 리스트 생성 (h층 x n세로 x m가로)
graph = []

for _ in range(h):
    layer = []
    for _ in range(n):
        # 한 줄(가로)의 정보를 리스트로 받아 층(layer)에 추가
        layer.append(list(map(int, input().split())))
    # 완성된 한 층을 전체 그래프에 추가
    graph.append(layer)

print(graph)