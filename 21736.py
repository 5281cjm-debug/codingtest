
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

print(dfs1(inode))


# n,m = map(int,input().split())
# school = []
# for _ in range(n):
#     line = []
#     for state in list(input()):
#         line.append(state)
#     school.append(line)

# innodes = []
# for h in range(n):
#     for w in range(m):
#         if h*m+w in 