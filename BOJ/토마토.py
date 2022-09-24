# https://www.acmicpc.net/problem/7576

from collections import deque

m, n = map(int, input().split())
data = []
q = deque([])

for i in range(n) :
    data.append(list(map(int, input().split())))
    for j in range(m) :
        if data[i][j] == 1 : # 익은 토마토라면
            q.append([i, j])

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
result = 0

def bfs() :
    while q :
        x, y = q.popleft()
        for d in range(4) :
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < n and 0 <= ny < m and data[nx][ny] == 0 :
                q.append([nx, ny])
                data[nx][ny] = data[x][y] + 1

bfs()
flag = 0
for i in data :
    for j in i :
        if j == 0 :
            print(-1)
            exit(0)

    result = max(result, max(i))

print(result - 1)


'''
1. n줄의 창고 상태를 한 줄씩 입력받아 data 리스트에 추가하고, 해당 줄의 m개의 토마토 중 익은 토마토의 좌표를 q에 추가한다.

2. (상, 하, 좌, 우) 방향을 담은 dx, dy 리스트를 정의하고 bfs() 함수를 호출하여 수행한다. bfs() 함수의 작업은 아래와 같다.
  - q가 빌 때까지 좌표를 하나씩 꺼내(x, y) 네 가지 방향에 대한 각 다음 좌표를 확인한다.
  - 다음 좌표가 창고 범위 내에 존재하고 해당 좌표에 있는 토마토가 안익었다면 해당 좌표(nx, ny)를 q에 추가하고 원래의 좌표에 존재하는 data 값에 1을 더한 값을 data[nx][ny]에 할당한다.
 
3. bfs() 함수의 작업이 끝나면 창고 상태를 한 줄씩 확인하고, 안익은 토마토가 있다면 -1을 출력한 후 시스템을 종료한다.
 
4. 한 줄을 확인했을 때 안익은 토마토가 없다면 result값과 현재 줄에 존재하는 최댓값을 비교하여 더 큰 값을 result에 할당한다.
 
5. 반복 작업이 끝나면 최종적으로 result에 1을 뺀 값을 출력한다. (가장 처음 0이 아닌 1부터 시작하였으므로)

'''
