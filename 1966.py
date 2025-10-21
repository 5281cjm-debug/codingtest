import sys
input = sys.stdin.readline

class Queue():
    def __init__(self):
        self.queue = []
    
    def push(self,n):
        self.queue.append(n)
        return True
    
    def pop(self):
        if self.empty():
            return -1
        else:
            return self.queue.pop(0)

    def empty(self):
        if len(self.queue) == 0:
            return 1
        else:
            return 0
    
    def back(self):
        if self.empty():
            return -1
        else:
            return self.queue[-1]
    
    def front(self):
        if self.empty():
            return -1
        else:
            return self.queue[0].get_rank()
        
    def size(self):
        return len(self.queue)
    
    def do_sort(self):
        self.sort(self.queue)

    def getranks(self):
        ranklist = []
        for ele in self.queue:
            ranklist.append(ele.get_rank())
        return ranklist
    def getlen(self):
        return len(self.queue)
def sort(queue):
    if queue.getlen() == 1:
        return [queue.pop()]
    while max(queue.getranks()) != queue.front():
        queue.push(queue.pop())
    return [queue.pop()] + sort(queue)
    

class Document():
    num = 0
    def __init__(self,rank):
        self.num = Document.num
        Document.num += 1
        self.rank = rank
    def get_rank(self):
        return self.rank
    def get_num(self):
        return self.num
    def clear():
        Document.num = 0
def s2d(rank):
    doc = Document(int(rank))
    return doc
    
def main():
    T = int(input())
    for _ in range(T):
        queue = Queue()
        Document.clear()
        n,m = map(int,input().split())
        rank_docs = list(map(int,input().split()))
        for rank_doc in rank_docs:
            queue.push(s2d(rank_doc))
        sq = sort(queue)
        for idx,i in enumerate(sq):
            if m == i.get_num():
                print(idx+1)

        

        


if __name__ == "__main__":
    main()
