from baseball_game_engine import make_quiz, check
from custom_error import InvalidCountError
answer = make_quiz()
# print(answer)
# 무한반복
count = 0


def save_history(player, count):
    with open('baseball_history.txt', 'a') as f:
        f.write(f'{player}\t{count}\n')

def load_history():
    count_list = []
    with open('baseball_history.txt', 'r') as f:
        while True:
            line = f.readline()
            if line == '' or not line:
                break
            # print(line.rstrip())
            line_data = line.split('\t')
            count_list.append(line_data[1])
        # 중복제거
        count_list = set(count_list)
        count_list = list(count_list)
        count_list.sort()
        return count_list[:3]

print(answer)
while True:
    # 숫자 3자리 중복없이 묻자
    player = input("숫자 세자리는?(t: top3)")  # player: "123" "fun"
    if player == 't':
        history = load_history()
        print(history)
        continue
    try:    # 숫자가 아닐 시 에러 처리
        player_int = int(player)        # ValueError
    except ValueError:
        continue
    # 길이가 3이 아닐 떄 에러 처리
    if len(player) != len(answer):
        # raise InvalidCountError("3자리가 아닙니다.")       # raise 는 발생시키다
        print(f'입력한 숫자의 개수가 정답과 다릅니다.정답: {len(answer)} 글자')
        continue

#  strike, ball 확인하자
    count += 1
    strike, ball = check(answer, player)
# 출력하자
    print(f'{player}\tstrick: {strike}\tball: {ball}\t{count}try')
# strike 가 3일 때, 나가자
    if strike == 3:
        # 저장하자
        save_history(player, count)
        break

# 축하해주자
print('축하합니다. 짝짝짝🎉🎉🎉')