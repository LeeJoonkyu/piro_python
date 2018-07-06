from random import randint
class Groupper(object):
    def __init__(self, names):
        self.names = names
        self.dict = {}
    def random_group(self, group_count):
        for k in range(1,group_count+1):
            self.dict.setdefault(k)
            self.dict[k] =[]
        for k in range(1, group_count+1): #1~4 까지
            for x in range(len(self.names)-1): #1,12 까지 k가 오고
                pid = randint(0, len(self.names)-1) #pid 받아오기 #0, 13-1 randint 0
                if len(self.dict[k]) >= 3: #len이 0 부터 시작하니까 0일때 추가 1일때추가 2일때 추가 3일때 break니까...
                    #
                    break
                else :
                    self.dict[k].append(self.names.pop(pid))  #key가 5를 입력해서 오류인것. 이걸 고쳐봐
        k = randint(1,4)
        self.dict[k].append(self.names[0])

    def print_group(self):
        print(self.dict)
