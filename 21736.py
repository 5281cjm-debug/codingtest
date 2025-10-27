"""
import sys
def input():
    readin = sys.stdin.readline()
    return readin.rstrip()

def dfs1(inode):

    edges = dfs2(inode)
    ps = 0
    for edge in edges:
        if edge.get_state() == 'P':
            ps += 1
    if ps != 0:
        return ps
    else:
        return 'TT'

def bfs(node):
    queue = []
    visited = []
    visited.append(node)
    queue += node.get_edges()
    while len(queue) != 0:
        now_node = queue.pop(0)
        if now_node in visited:
            continue
        visited.append(now_node)
        queue += now_node.get_edges()
    return visited


# def dfs2(node,edges):
#     for edge in node.get_edges():
#         if edge in edges:
#             continue
#         edges.append(edge)
#         edges = dfs2(edge,edges)
#     return edges

def dfs2(inode):
    
    for edge in inode.get_edges():
        if edge in edges:
            continue
        edges.append(edge)
        edges = dfs2(edge,edges)
    return edges


class Node():
    num = 1
    def __init__(self,state):
        self.num = Node.num
        self.state = state
        self.edges = []
        Node.num += 1
    def add_edge(self,edge):
        self.edges.append(edge)
    def get_edges(self):
        return self.edges
    def get_num(self):
        return self.num
    def get_state(self):
        return self.state
n,m = map(int,input().split())
school = []
for _ in range(n):
    line = []
    for state in list(input()):
        line.append(Node(state))
    school.append(line)

inode = 0

for h in range(n):
    for w in range(m):
        now_node = school[h][w]
        if now_node.get_state() == 'I':
            inode = now_node
        try:
            if h-1 >= 0 and school[h-1][w].get_state() != 'X' and now_node.get_state() != 'X':
                school[h-1][w].add_edge(now_node)
                now_node.add_edge(school[h-1][w])
        except:
            pass
        try:
            if w-1 >= 0 and school[h][w-1].get_state() != 'X' and now_node.get_state() != 'X':
                school[h][w-1].add_edge(now_node)
                now_node.add_edge(school[h][w-1])
        except:
            pass
people = len([i for i in bfs(inode) if i.get_state() == 'P'])
if people == 0:
    people = 'TT'
print(people)
"""
from collections import deque
n,m = map(int,input().split())
school = []

ih = 0
iw = 0
for h in range(n):
    line = []
    for w,state in enumerate(list(input())):
        line.append(state)
        if state == 'I':
            ih = h
            iw = w  
    school.append(line)

queue = deque([])
now_node = (ih, iw, 'I')
queue.append(now_node)
visited = set()
while queue:
    now_node = queue.popleft()
    if now_node in visited:
        continue
    else:
        visited.add(now_node)

    h = now_node[0]
    w = now_node[1]
    if h-1 >= 0 and school[h-1][w] != 'X':
        queue.append((h-1, w,school[h-1][w]))
    if h+1 < n and school[h+1][w] != 'X':
        queue.append((h+1, w,school[h+1][w])) 
    if w-1 >= 0 and school[h][w-1] != 'X':
        queue.append((h, w-1,school[h][w-1]))
    if w+1 < m and school[h][w+1] != 'X':
        queue.append((h, w+1,school[h][w+1])) 
peoples = len([i for i in visited if i[2]=='P'])
print(peoples if peoples>0 else 'TT')