# n,k = map(int,input('').split())
# n_list = list(range(1,n))
# yosepus = []

# start_n = 0
# while len(n_list) != 0:
#     for n_idx in range(start_n,len(n_list),k):
#         yosepus.append(n_list.pop(n_idx))
#     start_n = len(yosepus) - n_idx

# print('<{}>'.format(yosepus))

class Yosepus():
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
