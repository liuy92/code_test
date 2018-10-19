#-*-coding:utf-8-*-
import numpy as np

def DFS(target, graph, start):
    """
    target:目的地坐标 list
    graph:地图，list
    x,y：起点坐标，list
    """
    print np.array(graph), graph[target[0]][target[1]]
    direction = ((0,1),(0,-1),(1,0),(-1,0))
    label = 0
    x_n = len(graph)
    y_n = len(graph[0])
    used = np.array([[0]*y_n] * x_n)
    def dfs(x, y):
        if [x, y] == target:
            label = 1
            print '*' * 10, label
        for x_add, y_add in direction:
            print '====', (x, y), (x+x_add, y+y_add)#, '\n', np.array(used)
            if 0<=x+x_add<=x_n-1 and 0<=y+y_add<=y_n-1 \
                    and graph[x+x_add][y+y_add] == 1 \
                    and used[x+x_add][y+y_add] == 0\
                    and label == 0:
                print 'x = ', x+x_add, 'y = ', y+y_add
                used[x+x_add][y+y_add] = 1
                print np.array(used)
                dfs(x+x_add, y+y_add)
                print '#' * 20, label
                if label == 1:
                    return
                else:
                    used[x+x_add][y+y_add] = 0
    dfs(start[0], start[1])
    return used

if __name__ == '__main__':
    target = [0, 6]
    graph = [[1,1,1,0,0,1,1],[1,1,0,0,0,1,1],[1,1,1,1,1,1,0],[1,1,0,0,1,1,1],[1,1,1,1,1,1,1]]
    print '======\n', np.array(DFS([0,6], graph, [0,0]))