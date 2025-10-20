import sys
input = sys.stdin.readline

n = int(input())

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
            return self.queue[0]
        
    def size(self):
        return len(self.queue)

def main():
    queue = Queue()
    for _ in range(n):
        program = input().split()
        if program[0] == 'push':
            queue.push(program[1])
        elif program[0] == 'back':
            print(queue.back())
        elif program[0] == 'front':
            print(queue.front())
        elif program[0] == 'size':
            print(queue.size())
        elif program[0] == 'empty':
            print(queue.empty())
        elif program[0] == 'pop':
            print(queue.pop())


if __name__ == "__main__":
    main()
