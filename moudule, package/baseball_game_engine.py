# 숫자 야구게임
# 퀴즈내자 숫자 3자리 중복없이
import random
def make_quiz():
    # 숫자 3자리 중복없이
    list_r = random.sample(range(1, 9 + 1), 3)
    string_number = "".join(map(str, list_r))

    return string_number

def check(answer, player):
    strike = 0
    ball = 0
    # 번호가 있고, 자리가 같으면 strick += 1
    for i, p in enumerate(player):
        for j, a in enumerate(answer):
            if p == a:
                if i == j:
                    strick += 1
                else:
                    ball += 1
    # 번호가 없고, 자리가 다르면 ball += 1
    return strike, ball

if __name__ == '__main__':
    answer = make_quiz()
    print(answer)
    strick, ball = check("238", "241")
    print(answer, ball)     # 1 0
    strick, ball = check("381", "182")
    print(strick, ball)     # 1 1
