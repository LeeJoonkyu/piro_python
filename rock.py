# intro - > 반복문
# 가위바위보 메소드 - > if 조건문
# 승,무,패 저장 - > dict
# print input

import random

intro_str = """가위 바위 보 게임!!!
반가워요~~
"""
input_msg = '1. 가위, 2. 바위, 3. 보, {종료 : Q,q}'
score_msg = "승 : {win}, 패 : {lose}, 비김 : {draw}"

score = {'win' : 0, 'draw' : 0, 'lose' : 0}
rsp_set = {'가위','바위','보'}

while True :
    print(intro_str)
    while True:
        input_str = input(input_msg)
        if input_str in ['1','2','3','q','Q']:
            if input_str in['q','Q']:
                print("안녕히가세요~")
                exit()
                #break 해버리면 바깥으로 바깥while문만 끝나지.
            else:
                user = int(input_str)
                com = random.randint(1, 3)

                if user == com:
                    print("비겼습니다")
                    score['draw'] +=1
                elif user % 3 + 1 == com:
                    print("졌습니다")
                    score['lose']+=1
                elif com % 3 + 1 == user:
                    print("이겼습니다")
                    score['win']+=1
                print(score_msg.format(
                    win=score['win'],
                    lose = score['lose'],
                    draw=score['draw']
                ))

        else:
            print("잘못골랐습니다 다시 입력해주세요")




#input_str == "q, Q" -> 게임을 종료
'''com_str = random.randint(1,3)
가위 = 1
바위 = 2
보 = 3
#user_str == com_str -> 비김 : score[draw] +=1
가위 < 바위 가위+1 == 바위
바위 < 보 바위+1 == 보
보 < 가위 보+1 4 %3 == 가위 ==1
'''
