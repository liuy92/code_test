#-*-coding:utf-8-*-
import sys
import collections
reload(sys)
sys.setdefaultencoding('utf8')

"""https://www.nowcoder.com/questionTerminal/d64d259ee34141378b62e1ea4be74030
input:
4 4
....
..*@
....
.X..
6 6
...#..
......
#*##..
..##.#
..X...
.@#...
output:3, 11
其中 . 表示空地、X表示玩家、*表示箱子、#表示障碍、@表示目的地。
"""

def moveBox(bMap, N, M):
    dic = ((1,0),(-1,0),(0,1),(0,-1))
    #记录箱子和人的初始位置
    for i in range(N):
        for j in range(M):
            if bMap[i][j] == '*':    #该位置为箱子
                box = [i, j]
            if bMap[i][j] == 'X':    #该位置为人
                people = [i, j]
    dp = [[[[False for _ in range(M)] for _ in range(N)] for _ in range(M)] for _ in range(N)]
    dp[box[0]][box[1]][people[0]][people[1]] = True
    stack = collections.deque([[box[0], box[1], people[0], people[1]]])
    step = 0
    """因为箱子的位置是随人的位置发生变化的，所以在这里只考虑人走的位置是否会发生障碍
    而
    """
    while stack:
        step += 1
        n = len(stack)
        for _ in range(n):
            bx, by, px, py = stack.popleft() #箱子和人所在的位置
            for dx, dy in dic:
                nx, ny = px + dx, py + dy    #人可移动的位置
                if -1 < nx < N and -1 < ny < M and bMap[nx][ny] != '#':  #人可移动的位置不为障碍的话
                    if nx == bx and ny == by:     #人可以动的位置在箱子的位置的话
                        nbx, nby = bx+dx, by+dy   #判断箱子的位置
                        if -1 < nbx < N and -1 < nby < M:    #箱子的位置为目的地
                            if bMap[nbx][nby] == '@':
                                return step   #返回步数
                            else:
                                if not dp[nbx][nby][nx][ny]:   #如果人和箱子的位置没走过的话
                                    dp[bx+dx][by+dy][nx][ny] = True
                                    stack.append([bx+dx, by+dy, nx, ny])
                    else:
                        if not dp[bx][by][nx][ny]:   #如果人和箱子的位置没走过的话
                            dp[bx][by][nx][ny] = True
                            stack.append([bx,by,nx,ny])
    return -1

def result(bMap, N, M):
    bmap = []
    for i in range(N):
        bmap.append([ch for ch in bMap[i]])