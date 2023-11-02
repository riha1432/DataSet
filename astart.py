import pandas as pd
import numpy as np
import time
import math

maze = ['maze11','maze21','maze31','maze41','maze51','maze61','maze71','maze81']
size = 11
maze_cnt = 30

class Node():
    def __init__(self, x, y, cost, end_x, end_y):
        self.x = x
        self.y = y
        self.cost = cost
        self.heuristic = self.heuristic_fun(x, y, end_x, end_y)

    def __lt__(self, other):
        return (self.cost + self.heuristic) < (other.cost + other.heuristic)
    
    def heuristic_fun(self ,x, y, ex, ey):
        return math.sqrt(pow(ex-x,2)+ pow(ey-y,2))

def Astart(maze_node):
    move = [[1,0], [0,1], [-1,0], [0,-1]]
    dq = []
    end_node_x = size -1
    end_node_y = size -2
    dq.append(Node(0, 1, 0, end_node_x, end_node_y))
    count = 1

    while dq:
        dq = sorted(dq)
        node = dq.pop(0)
        maze_node[node.y][node.x] = count
        count += 1

        if( node.x == end_node_x and node.y == end_node_y):
            break
        
        for i in move:
            if( ((node.x + i[0]) < 0 or (node.x + i[0]) >= size) or ((node.y + i[1]) < 0 or (node.y + i[1]) >= size) ):
                continue
            if( maze_node[node.y + i[1]][node.x + i[0]] >= 1):
                continue
            
            dq.append(Node(node.x + i[0], node.y + i[1], node.cost+1, end_node_x, end_node_y))

    # print(np.array(maze_node))
    return 0


maze_time_avr = []

for url in maze:
    url1 = '/home/tjqjaejr9741/MyGitHub/share/' + url + '.csv'
    f = pd.read_csv(url1)
    f = np.array(f)
    s_maze = 0
    sum_time = 0

    for i in range(maze_cnt):
        s_time = time.time()
        Astart(f[s_maze:(s_maze + size)].tolist())
        sum_time += (time.time() - s_time)
        s_maze += size

    maze_time_avr.append(sum_time/maze_cnt)
    size += 10


for i in range(len(maze_time_avr)):
    print('미로 '+ str(i+1) +'1 : ',end='')
    print(maze_time_avr[i])