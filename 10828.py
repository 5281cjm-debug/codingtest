import sys
input = sys.stdin.readline

n = int(input())

class Stack():
    def __init__(self):
        self.stack = []
    
    def push(self,n):
        self.stack.append(n)
        return True
    
    def pop(self):
        if self.empty():
            return -1
        else:
            return self.stack.pop()

    def empty(self):
        if len(self.stack) == 0:
            return 1
        else:
            return 0
    
    def top(self):
        if self.empty():
            return -1
        else:
            return self.stack[-1]
        
    def size(self):
        return len(self.stack)

def main():
    stack = Stack()
    for _ in range(n):
        program = input().split()
        if program[0] == 'push':
            stack.push(program[1])
        elif program[0] == 'top':
            print(stack.top())
        elif program[0] == 'size':
            print(stack.size())
        elif program[0] == 'empty':
            print(stack.empty())
        elif program[0] == 'pop':
            print(stack.pop())


if __name__ == "__main__":
    main()
