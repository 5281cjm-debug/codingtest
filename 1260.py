import sys
def input():
    readin = sys.stdin.readline()
    return readin.rstrip()
def dfs(node):
    stack = []
    visited = []
    visited.append(node)
    for i in sorted(node.get_edge(),key=lambda x: -x.get_num()):
        stack.append(i)
    while len(stack) != 0:
        now_node = stack.pop()
        if now_node in visited:
            continue
        visited.append(now_node)
        for i in sorted(now_node.get_edge(),key=lambda x: -x.get_num()):
            stack.append(i)
    return visited

def bfs(node):
    queue = []
    visited = []
    visited.append(node)
    queue += sorted(node.get_edge(),key=lambda x:x.get_num())
    while len(queue) != 0:
        now_node = queue.pop(0)
        if now_node in visited:
            continue
        visited.append(now_node)
        queue += sorted(now_node.get_edge(),key=lambda x: x.get_num())
    return visited

def print_nodes(nodes):
    for i in nodes:
        print(i.get_num(),end=' ')

class Node():
    def __init__(self,num):
        self.num = num
        self.edge = []
    def set_edge(self,node):
        self.edge.append(node)
    def get_edge(self):
        return self.edge
    def get_num(self):
        return self.num

n,m,v = map(int,input().split())

nodes = [Node(i+1) for i in range(n)]
for _ in range(m):
    edge1,edge2 = map(int,input().split())
    nodes[edge1 -1].set_edge(nodes[edge2-1])
    nodes[edge2 -1].set_edge(nodes[edge1-1])
    
dfs_nodes = dfs(nodes[v-1])
bfs_nodes = bfs(nodes[v-1])

print_nodes(dfs_nodes)
print()
print_nodes(bfs_nodes)