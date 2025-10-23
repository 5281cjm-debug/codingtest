import sys
def input():
    readin = sys.stdin.readline()
    return readin.rstrip()
def get_count_of_edges(node):
    node_nums = [node.get_num()]
    edges = node.get_edges()
    for edge in edges:
        node_nums.append(edge.get_num())
        node_nums = dfs2(edge,node_nums)
    return len(set(node_nums))-1

def dfs2(node,node_nums):
    edges = node.get_edges()
    for edge in edges:
        if edge.get_num() in node_nums:
            continue
        node_nums.append(edge.get_num())
        node_nums = dfs2(edge,node_nums)
    return node_nums

class Node():
    def __init__(self,num):
        self.num = num
        self.edges = []
    def set_edge(self,edge):
        self.edges.append(edge)
    def get_edges(self):
        return self.edges
    def get_num(self):
        return self.num

count_of_computer = int(input())
count_of_edge = int(input())
computers = [Node(i+1) for i in range(count_of_computer)]
for _ in range(count_of_edge):
    edge1,edge2 = map(int,input().rstrip().split())
    computers[edge1-1].set_edge(computers[edge2-1])
    computers[edge2-1].set_edge(computers[edge1-1])


print(get_count_of_edges(computers[0]))