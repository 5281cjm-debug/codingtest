# n,k = map(int,input('').split())
# n_list = list(range(1,n))
# yosepus = []

# start_n = 0
# while len(n_list) != 0:
#     for n_idx in range(start_n,len(n_list),k):
#         yosepus.append(n_list.pop(n_idx))
#     start_n = len(yosepus) - n_idx

# print('<{}>'.format(yosepus))

"""class Yosepus():
    def __init__(self,n,k):
        self.n = n
        self.k = k
        self.yosepus = []
        self.n_list = list(range(1,n+1))
        self.going = self.k - 1

    def go_k(self):
        len_n_list = len(self.n_list)
        poplist = []
        if self.going == 0:
            self.going = self.k - 1
        while self.check_is_k_bigger_n():
            self.going -= len_n_list
        
        for n_idx in range(self.going,len_n_list,self.k):
            self.yosepus.append(self.n_list[n_idx])
            poplist.append(n_idx)
        
        popoff = 0
        for popidx in poplist:
            self.n_list.pop(popidx - popoff)
            popoff += 1

        self.going = len_n_list - 1 - n_idx

    def check_is_k_bigger_n(self):
        if len(self.n_list) <= self.going:
            return True
        else:
            return False
        
    def make_yosepus(self):
        while len(self.n_list) != 0:
            self.go_k()

    def print_yos(self):
        print('<',end='')
        for i in self.yosepus[:-1]:
            print(i,end=', ')
        print('{}>'.format(self.yosepus[-1]),end='')
    
def main():
    n,k = map(int,input('').split())
    yosepus = Yosepus(n,k)
    yosepus.make_yosepus()
    yosepus.print_yos()

if __name__ == "__main__":
    main()
"""
# class Yosepus():
#     def __init__(self,n,k):
#         self.n = n
#         self.k = k
#         self.yosepus = []
#         self.n_list = list(range(1,n+1))
#         self.going = self.k - 1

#     def go_k(self):
#         len_n_list = len(self.n_list)

#         while self.check_is_k_bigger_n():
#             self.going -= len_n_list
        

#         self.yosepus.append(self.n_list.pop(self.going))
        
#     def making_going(self):
#         self.going += self.k

#     def check_is_k_bigger_n(self):
#         if len(self.n_list) <= self.going:
#             return True
#         else:
#             return False
        
#     def make_yosepus(self):
#         while len(self.n_list) != 0:
#             self.go_k()
#             self.making_going()

#     def print_yos(self):
#         print('<',end='')
#         for i in self.yosepus:
#             print(i,end=' ')
#         print('>',end='')
    

# def main():
#     n,k = map(int,input('').split())
#     yosepus = Yosepus(n,k)
#     yosepus.make_yosepus()
#     yosepus.print_yos()

# if __name__ == "__main__":
#     main()

class Linked_list():
    def __init__(self,num,next=None):
        self.next = next
        self.num = num
    def get_num(self):
        return self.num
    def set_next(self,next):
        self.next = next
    def get_next(self):
        return self.next
    def get_last(self):
        node = self
        while node.get_next() is not None and node.get_next() != self:
            node = node.get_next()
        return node
        
def list2circle_linked_list(int_list):
    start_circle_linked_list = Linked_list(1)
            
    for int_list_idx in range(2, len(int_list)+1):
        next_circle_linked_list = Linked_list(int_list_idx)
        start_circle_linked_list.get_last().set_next(next_circle_linked_list)
    
    start_circle_linked_list.get_last().set_next(start_circle_linked_list)
    return start_circle_linked_list


def yosepus(circle_linked_list, n, k):
    # 처음 제거될 노드의 이전 노드를 찾아 초기화
    if k == 1:
        return list(range(1,n+1))
    now_add = circle_linked_list
    for _ in range(k - 2):  # k번째 이전 노드로 이동
        now_add = now_add.get_next()

    sorted_list = []
    while len(sorted_list) < n:
        if now_add.get_next() == now_add:
            sorted_list.append(now_add.get_num())
            break
        sorted_list.append(now_add.get_next().get_num())
        now_add.set_next(now_add.get_next().get_next())
        now_add = now_add.get_next()
        for _ in range(k-2):
            now_add = now_add.get_next()

        

    return sorted_list
def main():
    n,k = map(int,input('').split())
    range_n_list = list(range(1,n+1))
    circle_linked_list = list2circle_linked_list(range_n_list)
    yosepused_list = yosepus(circle_linked_list,n, k)
    print('<',end='')
    for i in yosepused_list[:-1]:
        print(i,end=', ')
    print(yosepused_list[-1],end='')
    print('>')

if __name__ == "__main__":
    main()
