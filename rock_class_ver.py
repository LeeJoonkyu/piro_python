# class name(인자):
#     property
#     def function(self,인자):
#         name.property
#         print()
# class userinterface() 정의

import random

class game():
    intro_msg = "가위 바위 보 게임 !! 안녕하세요"
    input_msg = "1.가위 2. 바위 3. 보 종료(q,Q)"
    choice_list = ('가위','바위','보')
    confirm_msg = "{user}를 내셨군요, 저는 {com}을 냈습니다."
    user = None
    com = None
    calc_result = None

    def start(self):
        while True:
            self.intro()
            self.user = self.get_user_input()
            self.com = random.randint(1,3)
            self.calc_result()
            self.print_confirm_msg()

        #게임의 흐름. 밑과 똑같지?

        # print_intro()
        # user = get_user_input()
        # com = random.randint(1, 3)
        # result = calc_result(user, com)
        # print_result(result)
    def intro(self):
        print(self.intro_msg)

    def get_user_input(self): #바로 밑에 라인 refactored.
        while True:
            input_str = input(self.input_msg)
            if input_str in ['1', '2', '3', 'q', 'Q']:
                if input_str in ['q', 'Q']:
                    print("안녕히가세요~")
                    exit()
                    # break 해버리면 바깥으로 바깥while문만 끝나지.
                else:
                    return int(input_str) #여기 refactored 체크
                    break  # return user로 가기 위해서 break 함수 처리 하기 전과 다른점!
            else:
                print("잘못골랐습니다 다시 입력해주세요")
        return user

    def calc_result(self):
        if self.user == self.com:
            self.result = "draw"
        elif self.user % 3 + 1 == self.com:
            self.result = "lose"
        elif self.com % 3 + 1 == self.user:
            self.result = "win"
        #return self.result
    def print_result(self):
        if self.result == "win":
            print("이겼습니다")
        elif self.result == "lose":
            print("졌습니다")
        else:
            print("비겼습니다")
    def print_confirm_msg(self):
        print(self.confirm_msg.format(user = self.user, com = self.com))


rock = game()
rock.start()
