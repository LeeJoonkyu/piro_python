# intro - > 반복문
# 가위바위보 메소드 - > if 조건문
# 승,무,패 저장 - > dict
# print input

import random

def gamestart(): #클래스 생성
    while True:
        print_intro()
        user = get_user_input()
        com = random.randint(1,3)
        result = calc_result(user,com)
        print_result(result)

def print_intro(): #이걸 짜는 이유는 유지보수. 전체에서 다 통용될수있는 거니까.
    intro_str = """가위바위보 게임!!!
    반가워요~~~
    """
    print(intro_str)

def get_user_input():
    input_msg = '1.가위, 2. 바위, 3. 보, {종료 : Q,q}' #123 말고 진짜 가위바위보로 바꾸고싶다면 필요한 커맨드.
    while True:
        input_str = input(input_msg)
        if input_str in ['1','2','3','q','Q']:
            if input_str in ['q','Q']:
                print("안녕히가세요~")
                exit()
                #break 해버리면 바깥으로 바깥while문만 끝나지.
            else:
                user = int(input_str)
                break #return user로 가기 위해서 break 함수 처리 하기 전과 다른점!
        else:
            print("잘못골랐습니다 다시 입력해주세요")
    return user

def calc_result(user,com):
    if user == com:
        result= "draw"
    elif user % 3 + 1 == com:
        result = "lose"
    elif com % 3 + 1 == user:
        result = "win"
    return result

def print_result(result):
    if result =="win":
        print("이겼습니다")
    elif result=="lose":
        print("졌습니다")
    else:
        print("비겼습니다")

#gamestart()->실행시
#get_user_input()->실행시 return input str
#calc_result->실행시 return key->value(win,lose,draw)
#print_result()->실행 시 print


'''intro_str = """가위 바위 보 게임!!!
반가워요~~
"""
input_msg = '1. 가위, 2. 바위, 3. 보, {종료 : Q,q}'
score_msg = "승 : {win}, 패 : {lose}, 비김 : {draw}"

score = {'win' : 0, 'draw' : 0, 'lose' : 0}
rsp_set = {'가위','바위','보'}

while True :
    print(intro_str)
'''

gamestart()
