# # 1. 핸드폰 요금이 62421원 나왔다. 100원 미만은 절사한다고 한다. 62400원 청구. 59827원일 경우, 실제 청구 금액은?
# import math
# bill = 59827
# print(bill//100*100)
# print(bill-bill%100)
# print(math.floor(bill/100)*100)
#
#
# # 2. 평가계획은 100점 만점에 10점 단위로 점수를 줄 수 있다. 채점한 결과 93점이 나왔다. 90점 부여. 56점은 몇 점 부여?
# score = 93
# score = 56
# print(round(score / 10) * 10)
# print(round(score, -1))
#
#
# # 3. 로또 복권 자동 생성기를 만든다면?
# # (로또복권: 1~45 사이의 번호 중 랜덤으로 6개 뽑기)
# import random
# print(random.sample(range(1, 46), 6))
#
#
# # 4. 1~9 숫자로 중복되지 않은 숫자 세자리를 뽑는 방법은?(185:O, 212:X)
# import random
# num = list(range(1, 10))  # num = [1,2,3,4,5,6,7,8,9]
# number = []
#
# for i in range(3):
#     number.append(num.pop(num.index(random.choice(num))))
# print(number)
#
# list_r = random.sample(range(1, 9 + 1), 3)
# print("".join(str(n)for n in list_r))       # "273"
# print("".join(map(str, list_r)))
#
# string = ''
# for n in list_r:
#     string += str(n)
# print(string)


# 5. 내가 태어난 날로부터 며칠이 지났는지?
# import datetime
# print('-'*20)
# now = datetime.datetime.now()
# print(now)
# birthday = datetime.datetime(2004, 10, 14)
# print(birthday)
# print(now - birthday)


# import datetime
# birthday = datetime.datetime(2004, 10, 14)
# now = datetime.datetime.now()
# birthday = datetime.datetime.now()
# print(now - birthday)


# 6. 올해 크리스마스까지 며칠이 남았는지?
# import datetime
# print('-'*20)
# def getDaysBefore(d="12-25"):
#     dList = d.split("-")
#     year = int(dList[0])
#     month = int(dList[1])
#     day = int(dList[2])
#     dday = datetime.datetime(year, month, day)
#     now = datetime.datetime.now()
#
#     return str(dday - now).split(",")[0]
#
# print(getDaysBefore("2021-12-25"))


# christmas = datetime.datetime(2021, 12, 25)
# print(christmas - now)


# 7. 내 생일이 며칠 남았는지?
# import datetime
# print('-'*20)
# def getDaysBefore(d="2004-10-14"):
#     dList = d.split("-")
#     year = int(dList[0])
#     month = int(dList[1])
#     day = int(dList[2])
#     dday = datetime.datetime(year, month, day)
#     now = datetime.datetime.now()
#
#     return str(dday - now).split(",")[0]
#
# print(getDaysBefore("2021-10-14"))


# import datetime
# print('-'*20)
# def getDaysBefore(d="2004-10-14"):
#     dList = d.split("-")
#     year = int(dList[0])
#     month = int(dList[1])
#     day = int(dList[2])
#     dday = datetime.datetime(year, month, day)
#     now = datetime.datetime.now()
#
#     return str(dday - now).split(",")[0]
#
# print(getDaysBefore("2021-10-14"))


# 8. 랜덤하게 번호로 자리를 배치하는 방법은?
# 제적(전출, 자퇴) 인원이 있다면?
# 마지막 번호를 묻자
last_number = input("마지막 번호는? ")
# 1 ~ 마지막 번호까지 리스트 만들자
list_class = list(range(1, int(last_number) + 1))
# 무한반복
while True:
# 나간 친구 번호 묻자
    exclude_number = input("뺄 번호는?(enter치면 끝내자) ")
# 그냥 enter 치면 반복 끝내자
    if exclude_number == '':
        break
# 리스트에서 빼자
    list_class.remove(int(exclude_number))
    print(list_class)
