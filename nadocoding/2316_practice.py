# # 숫자 자료형
# print(5)
# print(-10)
# print(3.14)
# print(1000)
# print(5+3)
# print(2*8)
# print(3*(3+1))
#
# # 문자 자료형
# print('풍선')
# print("나비")
# print("ㅋㅋㅋㅋㅋㅋㅋㅋㅋ")
# print("ㅋ"*9)
#
# # boolean 자료형
# # 참 / 거짓
# print(5 > 10)
# print(5 < 10)
# print(True)
# print(False)
# print(not True)
# print(not False)
# print(not (5 > 10))
#
# # 변수
# # 애완동물을 소개해 주세요~
# animal = "강아지"
# name = "연탄이"
# age = 4
# hobby = "산책"
# is_adult = age >= 3
#
# ''' 주석은 이렇게 작은 따옴표 3개 혹은 #
# 길게 하고 싶을 땐 주석처리 할 부분들을 잡고 Ctrl + / '''
#
# print("우리집 " + animal + "의 이름은 " + name + "예요")
# hobby = "간식"
# # print(name + "는 " + str(age) + "살이며, " + hobby + "을 아주 좋아해요")
# print(name, "는 " , age, "살이며, " , hobby, "을 아주 좋아해요")
# print(name + "는 어른일까요? " + str(is_adult))
#
# # Quiz1) 변수를 이용하여 다음 문장을 출력하시오
# # 변수명
# #  : station
# # 변수값
# #  : "사당", "신도림", "인천공항"
# # 출력 문장
# #  : XX 행 열차가 들어오고 있습니다.
# station = "신도림"
# print(station + "행 열차가 들어오고 있습니다.")
#
# # 연산자
# print(1+1) # 2
# print(3-2) # 1
# print(5*2) # 10
# print(6/3) # 2
#
# print(2**3) # 2^3 = 8 거듭제곱
# print(5 % 3) # 나머지 구하기 2
# print(10 % 3) # 1 나누기 연산 후 몫이 아닌 나머지를 구함
# print(5//3) # 1 나누기 연산 후 소수점 이하의 수를 버리고, 정수 부분만 구힘
# print(10//3) # 3 나누기 연산 후 소수점 이하의 수를 버리고, 정수 부분만 구힘
#
# print(10 > 3) # True 크다
# print(4 >= 7) # False 크거나 같다
# print(10 < 3) # False 작다
# print(5 <= 5) # True 작거나 같다
#
# print(3 == 3) # True 앞과 뒤 값이 똑같다
# print(4 == 2) # False
# print(3 + 4 == 7) # True
#
# print(1 != 3) # True 앞 뒤가 같지 않다
# print(not(1 != 3)) # False
# print((3 > 0) and(3 < 5)) # True
# print((3 > 0) & (3 < 5)) # True
# print((3 > 0) or (3 < 5)) # True
# print((3 > 0) | (3 < 5)) # True
# print(5 > 4 > 3) # True
# print(5 > 4 > 7) # False
#
# # 간단한 수식
# print(2 + 3 * 4) # 14
# print((2 +3) * 4) # 20
# number = 2 + 3 * 4 # 14
# print(number)
# number = number + 2 # 16
# print(number)
# number += 2 # 18 덧셈
# print(number)
# number *= 2 # 36 곱셈
# print(number)
# number /= 2 # 18 나눗셈
# print(number)
# number -= 2 # 16 뺄셈
# print(number)
#
# number %= 5 # 1 %는 나머지
# print(number)
#
# # 숫자처리 함수
# print(abs(-5)) # 5
# print(pow(4, 2)) # 4^2 = 4*4 = 16
# print(max(5, 12)) # 12
# print(min(5, 12)) # 5
# print(round(3.14)) # 3 반올림
# print(round(4.99)) # 5 반올림
#
# from math import *
# print(floor(4.99)) # 내림. 4
# print(ceil(3.14)) # 올림. 4
# print(sqrt(16)) # 제곱근. 4
#
# # 랜덤 함수
# # from random import *
# # print(random()) # 0.0 ~ 1.0 미만의 임의의 값 생성
# # print(random() * 10) # 0.0 ~ 10.0 미만의 임의의 값 생성
# # print(int(random() * 10)) # 0 ~ 10 미만의 임의의 값 생성
# # print(int(random() * 10)) # 0 ~ 10 미만의 임의의 값 생성
# # print(int(random() * 10)) # 0 ~ 10 미만의 임의의 값 생성
# # print(int(random() * 10)) # 0 ~ 10 미만의 임의의 값 생성
# # print(int(random() * 10)) # 0 ~ 10 미만의 임의의 값 생성
#
# # print(int(random() * 10) + 1) # 1 ~ 10  이하의 임의의 값 생성
# # print(int(random() * 10) + 1) # 1 ~ 10  이하의 임의의 값 생성
# # print(int(random() * 10) + 1) # 1 ~ 10  이하의 임의의 값 생성
# # print(int(random() * 10) + 1) # 1 ~ 10  이하의 임의의 값 생성
# # print(int(random() * 10) + 1) # 1 ~ 10  이하의 임의의 값 생성
# # print(int(random() * 10) + 1) # 1 ~ 10  이하의 임의의 값 생성
# #
# # print(int(random() * 45) + 1) # 1 ~ 45  이하의 임의의 값 생성
# # print(int(random() * 45) + 1) # 1 ~ 45  이하의 임의의 값 생성
# # print(int(random() * 45) + 1) # 1 ~ 45  이하의 임의의 값 생성
# # print(int(random() * 45) + 1) # 1 ~ 45  이하의 임의의 값 생성
# # print(int(random() * 45) + 1) # 1 ~ 45  이하의 임의의 값 생성
# # print(int(random() * 45) + 1) # 1 ~ 45  이하의 임의의 값 생성
# # print(int(random() * 45) + 1) # 1 ~ 45  이하의 임의의 값 생성
# #
# # print(int(random(1, 46)) + 1) # 1 ~ 46  미만의 임의의 값 생성
# # print(int(random(1, 46)) + 1) # 1 ~ 46  미만의 임의의 값 생성
# # print(int(random(1, 46)) + 1) # 1 ~ 46  미만의 임의의 값 생성
# # print(int(random(1, 46)) + 1) # 1 ~ 46  미만의 임의의 값 생성
# # print(int(random(1, 46)) + 1) # 1 ~ 46  미만의 임의의 값 생성
# # print(int(random(1, 46)) + 1) # 1 ~ 46  미만의 임의의 값 생성
#
# # Quiz2) 당신은 최근에 코딩 스터디 모임을 새로 만들었습니다.
# # 월 4회 스터디를 하는데 3번은 온라인으로 하고 1번은 오프라인으로 하기로 했습니다.
# # 아래 조건에 맞는 오프라인 모임 날짜를 정해주는 프로그램을 작성하시오.
# # 조건1 : 랜덤으로 날짜를 뽑아야 함
# # 조건2 : 월별 날짜는 다름을 감안하여 최소 일수인 28 이내로 정함
# # 조건3 : 매월 1~3일은 스터디 준비를 해야 하므로 제외
# # (출력문 예제)
# # 오프라인 스터디 모임 날짜는 매월 x 일로 선정되었습니다.
#
# from random import *
# date = randint(4, 28)
# print("오프라인 스터디 모임 날짜는 매월 " + str(date) +" 일로 선정되었습니다.")
#
# # 문자열
# sentence = '나는 소년입니다.'
# print(sentence)
# sentence2 = "파이썬은 쉬워요"
# print(sentence2)
# sentence3 = """
# 나는 소년이고,
# 파이썬은 쉬워요
# """
# print(sentence3)
#
# # 슬라이싱
# jumin = "990120-1234567"
# print("성별 : " + jumin[7])
# print("연 : " + jumin[0:2]) # 0 부터 2 직전까지 (0,1)
# print("월 : " + jumin[2:4])
# print("일 : " + jumin[4:6])
#
# print("생년월일 : " + jumin[:6]) # 처음부터 6 직전까지
# print("뒤 7자리 : " + jumin[7:14]) # 7 부터 끝까지
# print("뒤 7자리 (뒤에부터) : " + jumin[-7:])
# # 맨 뒤에서 7번째부터 끝까지
#
# # 문자열 처리 함수
# python = "Python is Amazing"
# print(python.lower()) # 소문자
# print(python.upper()) # 대문자
# print(python[0].isupper())
# print(len(python))
# print(python.replace("Python", "Java"))
#
# index = python.index("n")
# print(index)
# index = python.index("n", index + 1)
# print(index)
#
# print(python.find("Java")) # 내가 원하는 값이 변수에 없을 땐 -1을 출력
# # print(python.index("Java")) # 그냥 에러를 내버림 오류를 내면서 프로그램을 종료시킴
# print("hi")
#
# print(python.count("n"))
#
# # 문자열 포맷
# # print("a" + "b")
# # print("a", "b")
#
# # 방법 1
# # print("나는 %d살입니다." % 20) # 정수 값만 ㄱㄴ
# # print("나는 %s을 좋아해요." % "파이썬")
# # print("Apple 은 %c로 시작해요." % "A")
# # %s
# # print("나는 %s살입니다." % 20)
# # print("나는 %s색과 %s색을 좋아해요." % ("파란", "빨간"))
#
# # 방법 2
# print("나는 {}살입니다.".format(20))
# print("나는 {}색과 {}색을 좋아해요." .format ("파란", "빨간"))
# print("나는 {0}색과 {1}색을 좋아해요." .format ("파란", "빨간"))
# print("나는 {1}색과 {0}색을 좋아해요." .format ("파란", "빨간"))
#
# # 방법 3
# print("나는 {age}살이며, {color}색을 좋아해요.".format(age = 20, color="빨간"))
# print("나는 {age}살이며, {color}색을 좋아해요.".format(color="빨간", age = 20))
#
# # 방법 4 (v3.6 이상~)
# age = 20
# color = "빨간"
# print(f"나는 {age}살이며, {color}색을 좋아해요.")
#
# # 탈출 문자
# # \n : 줄바꿈
# print("백문이 불여일견 \n백견이 불여일타")
# # \"\' : 문장 내에서 따옴표
# # 저는 "나도코딩"입니다.
# # print("저는 '나도코딩'입니다.")
# # print('저는 "나도코딩"입니다.')
# # print("저는 \"나도코딩\"입니다.")
# # print("저는 \'나도코딩\'입니다.")
#
# # \\ : 문장 내에서 \
# # print("C:\\Users\\Nadocoding\\Desktop\\PythonWorkspace>")
#
# # \r : 커서를 맨 앞으로 이동
# print("Red Apple\rPine")
#
# # \b : 백스페이스 (한 글자 삭제)
# print("Red\bApple")
#
# # \t : 탭
# print("Red\tApple")
#
# # Quiz3) 사이트별로 비밀번호를 만들어 주는 프로그램을 작성하시오
#
# # 예) http://never.com
# # 규칙1 : http:// 부분은 제외 => never.com
# # 규칙2 : 처음 만나는 점(.) 이후 부분은 제외 => naver
# # 규칙3 : 남은 글자 중 처음 세자리 + 글자 갯수 + 글자 내 'e' 갯수 + "!"로 구성
# #                 (nav)           (5)             (1)         (!)
# # 예) 생성된 비밀번호 : nav51!
#
# url = "http://never.com"
# my_str = url.replace("http://", "") # 규칙1
# # print(my_str)
# my_str = my_str[:my_str.index(".")] # 규칙2
# # my_str[0.5] -> 0 ~ 5 직전까지. (0, 1, 2, 3, 4)
# # print(my_str)
# # password = my_str[:3] + str(len(my_str)) + str(my_str.count("e")) + "!"
# # print("{0} 의 비밀번호는 {1} 입니다.".format(url, password))
#
# # 리스트 []
#
# # 지하철 칸별로 10명, 20명, 30명
# # subway1 = 10
# # subway2 = 20
# # subway3 = 30
#
# # subway = [10, 20, 30]
# # print(subway)
# #
# # subway = ["김태형", "박지민", "전정국"]
# # print(subway)
#
# # 지민씨가 몇 번째 칸에 타고 있는가?
# # print(subway.index("박지민"))
#
# # 윤기씨가 다음 정류장에서 다음 칸에 탐
# # subway.append("민윤기")
# # print(subway)
#
# # 아미를 김태형 / 박지민 사이에 태워봄
# # subway.insert(1, "아미")
# # print(subway)
#
# # 지하철에 있는 사람을 한 명씩 뒤에서 꺼냄
# # print(subway.pop())
# # print(subway)
# #
# # print(subway.pop())
# # print(subway)
# #
# # print(subway.pop())
# # print(subway)
#
# # 같은 이름의 사람이 몇 명 있는지 확인
# # subway.append("김태형")
# # print(subway)
# # print(subway.count("김태형"))
#
# # # 정렬도 가능
# # num_list = [5 , 2, 4, 3, 1]
# # num_list.sort()
# # print(num_list)
# #
# # # 순서 뒤집기 가능
# # num_list.reverse()
# # print(num_list)
# #
# # # 모두 지우기
# # num_list.clear()
# # print(num_list)
#
# # 다양한 자료형 함께 사용
# # num_list = [5, 2, 4, 3, 1]
# # mix_list = ["방탄", 20, True]
# # print(mix_list)
#
# # 리스트 확장
# # num_list.extend(mix_list)
# # print(num_list)
# #
#  # 사전
# # cabinet = {3: "김남준", 100: "김석진"}
# # print(cabinet[3])
# # print(cabinet[100])
#
# # print(cabinet.get(3))
# # print(cabinet[5]) # 5라는 키는 없기 때문에 종료
# # print(cabinet.get(5))
# # print(cabinet.get(5, "사용 가능"))
# # print("hi")
#
# # print(3 in cabinet) # True
# # print(5 in cabinet) # False
#
# # cabinet = {"A-3": "김남준", "B-100": "김석진"}
# # print(cabinet["A-3"])
# # print(cabinet["B-100"])
#
# # 새 손님
# # print(cabinet)
# # cabinet["A-30"] = "정호석"
# # cabinet["C-20"] = "최연준"
# # print(cabinet)
#
# # 간 손님
# # del cabinet["A-3"]
# # print(cabinet)
#
# # key 들만 출력
# # print(cabinet.keys())
#
# # value 들만 출력
# # print(cabinet.values())
#
# # key, value 쌍으로 출력
# # print(cabinet.items())
#
# # 목욕탕 폐점
# # cabinet.clear()
# # print(cabinet)
#
# # 튜플
# # menu = ("돈까스", "치즈돈까스")
# # print(menu[0])
# # print(menu[1])
#
# # menu.add("생선까스")
#
# # name = "강태현"
# # age = 20
# # hobby = "코딩"
# # print(name, age, hobby)
# #
# # (name, age, hobby) = ("강태현", 20, "코딩")
# # print(name, age, hobby)
#
# # 집합 (set)세트
# # 중복 안됨, 순서 없음
# # my_set = {1, 2, 3, 3, 3}
# # print(my_set)
# #
# # java = {"이수호", "백경", "한서준"}
# # python = set(["이수호", "최수빈"])
#
# # 교집합 (java 와 python 을 모두 할 수 있는 개발자)
# # print(java & python)
# # print(java.intersection(python))
#
# # 합집합 (java 도 할 수 있거나 python 할 수 있는 개발자)
# # print(java | python)
# # print(java.union(python))
#
# # 차집합 (java 할 수 있지만 python 은 할 줄 모르는 개발자)
# # print(java - python)
# # print(java.difference(python))
#
# # python 할 줋 아는 사람 늘어남
# # python.add("백경")
# # print(python)
#
# # java 를 잊었어요
# # java.remove("백경")
# # print(java)
#
# # 자료구조의 변경
# # 커피숍
# # menu = {"커피", "우유", "주스"}
# # print(menu, type(menu))
# #
# # menu = list(menu)
# # print(menu, type(menu))
# #
# # menu = tuple(menu)
# # print(menu, tuple(menu))
# #
# # menu = set(menu)
# # print(menu, type(menu))
#
# # Quiz4) 당신의 학교에서는 파이썬 코딩 대회를 주최합니다.
# # 참석률을 높이기 위해 댓글 이벤트를 진행하기로 하였습니다.
# # 댓글 작성자들 중에 추첨을 통해 1명은 치킨, 3명은 커피 쿠폰을 받게 됩니다.
# # 추첨 프로그램을 작성하시오.
#
# # 조건1 : 편의상 댓글은 20명이 작성하였고 아이디어는 1~20 이라고 가정
# # 조건2 : 댓글 내용과 상관 없이 무작위로 추첨하되 중복 불가
# # 조건3 : random 모듈의 shuffle 와 sample 를 활용
#
# # (출력 예제)
# #  -- 당첨자 발표 --
# # 치킨 당첨자 : 1
# # 커피 당첨자 : [2, 3, 4]
# #  -- 축하합니다 --
#
# # (활용 예제)
# # from random import *
# # 1st = [1, 2, 3, 4, 5]
# # print(1st)
# # shuffle(1st)
# # print(1st)
# # print(sample(1st, 1))
#
# # from random import *
# # users = range(1, 21) # 1부터 20까지 숫자를 생성
# # # print(type(users))
# # users = list(users)
# # # print(type(users))
#
# # print(users)
# # shuffle(users)
# # print(users)
# #
# # winners = sample(users, 4) # 4명 중에서 1명은 치킨, 3명은 커피)
# #
# # print(" -- 당첨자 발표 -- ")
# # print("치킨 당첨자 : {0}".format(winners[0]))
# # print("커피 당첨자 : {0}".format(winners[1:]))
# # print(" -- 축하합니다 -- ")
#
# # if
# # weather = input("오늘 날씨는 어때요? ")
# # if weather == "비":
# #     print("우산을 챙기세요")
# # elif weather == "미세먼지":
# #     print("마스크를 챙기세요")
# # else:
# #     print("준비물 필요 없어요.")
#
# # temp = int(input("기온은 어때요? "))
# # if 30 <= temp:
# #     print("너무 더워요. 나가지 마세요")
# # elif 10 <= temp and temp < 30:
# #     print("괜찮은 날씨에요")
# # elif 0 <= temp < 10:
# #     print("외투를 챙기세요")
# # else:
# #     print("너무 추워요. 나가지 마세요")
#
# # for(반복문)
# # print("대기번호 : 1")
# # print("대기번호 : 2")
# # print("대기번호 : 3")
# # print("대기번호 : 4")
#
# # randrange()
# # for waiting_no in range(1, 6): # [0, 1, 2, 3, 4]:
# #     print("대기번호 : {0}".format(waiting_no))
# #
# # starbucks = ["최범규", "휴닝카이", "아이엠 그루트"]
# # for customer in starbucks:
# #     print("{0}, 커피가 준비되었습니다.".format(customer))
#
# # while
# # customer = "휴닝카이"
# # index = 5
# # while index >= 1:
# #     print("{0}, 커피가 준비 되었습니다. {1} 번 남았어요." .format(customer, index))
# #     index -= 1
# #     if index == 0:
# #         print("커피는 폐기처분되었습니다.")
# #
# # customer = "최범규"
# # index = 1
# # while True:
# #     print("{0}, 커피가 준비 되었습니다. 호출 {1} 회" .format(customer, index))
# #     index += 1
#
# # customer = "휴닝카이"
# # person = "Unknown"
# #
# # while person != customer :
# #     print("{0}, 커피가 준비 되었습니다." .format(customer))
# #     person = input("이름이 어떻게 되세요? ")
# #
# # # continue 와 break
# # absent = [2, 5] # 결석
# # no_book = [7] # 책을 깜빡함
# # for student in range(1, 11): # 1,2,3,4,5,6,7,8,9,10
# #     if student in absent:
# #         continue
# #     elif student in no_book:
# #         print("오늘 수업 여기까지. {0}는 교무실로 따라와".format(student))
# #         break
# #     print("{0}, 책을 읽어봐".format(student))
#
# # 한 줄 for
# # 출석번호가 1 2 3 4 앞에 100을 붙이기로 함 -> , 102, 103, 104.
# # student = [1,2,3,4,5]
# # print(student)
# # student = [i+100 for i in student]
# # print(student)
#
# # 학생 이름을 길이로 변횐
# # student = ["Iron man", "Thor", "I am groot"]
# # student = [len(i) for i in student]
# # print(student)
#
# # 학생 이름을 대문자로 변환
# # student = ["Iron man", "Thor", "I am groot"]
# # student = [i.upper() for i in student]
# # print(student)
#
# # Quiz5) 당신은 Cocoa 서비스를 이용하는 택시기사님입니다.
# # 50명의 승객과 매칭 기회가 있을 때, 총 답승 승객 수를 구하는 프로그램을 작성하시오.
#
# # 조건1 : 승객별 운행 요소 시간은 5분 ~ 50분 사이의 난수로 정해집니다.
# # 조건2 : 당신은 소요 시간 5분 ~ 15분 사이의 승객만 매칭해야 합니다.
# # (출력문 예제)
# # [0] 1번째 손님 (소요시간 : 15분)
# # [ ] 2번째 손님 (소요시간 : 50분)
# # [0] 3번째 손님 (소요시간 : 5분)
# # ...
# # [] 50번째 손님 (소요시간 : 16분)
#
# # 총 탑승 승객 : 2 분
#
# # from random import *
# # cnt = 0 # 총 탑승 승객 수
# # for i in range(1, 51): # 1 ~ 50 이라는 수 (승객)
# #     time = randrange(5, 51) # 5분 ~ 50분 소요 시간
# #     if 5 <= time <= 15: # 5분 ~ 15분 이내의 손님 (매칭 성공), 탑승 승객 수 증가 처리
# #         print("[0] {0}번째 손님 (소요시간 : {1}분".format(i, time))
# #         cnt += 1
# #     else: # 매칭 실패한 경우
# #         print("[ ] {0}번째 손님 (소요시간 : {1}분".format(i, time))
# #
# # print("총 탑승 승객 : {0} 분".format(cnt))
#
# # 함수
# def open_account():
#     print("새로운 계좌가 생성되었습니다.")
#
# def deposit(balance, money): # 입금
#     print("입금이 완료되었습니다. 잔액은 {0} 원입니다.".format(balance + money))
#     return balance + money
#
# def withdraw(balance, money): # 출금
#     if balance >= money: # 잔액이 출금보다 많으면
#         print("출금이 완료되었습니다. 잔액은 {0} 원입니다.".format(balance - money))
#         return balance - money
#     else:
#         print("출금이 완료되지 않았습니다. 잔액은 {0} 원입니다.".format(balance))
#         return balance
#
# def withdraw_night(balance, money): # 저녁에 출금
#     commission = 100 # 수수료 100원
#     return commission, balance - money - commission
#
# balance = 0 # 잔액
# balance = deposit(balance, 1000)
# # balance = withdraw(balance, 2000)
# # balance = withdraw(balance, 500)
# commission, balance = withdraw_night(balance, 500)
# print("수수료는 {0} 원이며, 잔액은 {1} 원입니다.".format(commission, balance))
#
# # 기본값
# # def profile(name, age, main_lang):
# #     print("이름 : {0}\t나이 : {1}\t주 사용 언어: {2}" \ # 줄바꿈
# #           .format(name, age, main_lang))
# # profile("RM", 20, "파이썬")
# # profile("J-HOPE", 20, "자바")
#
# # 같은 학교 같은 학년 같은 반 같은 수업.
#
# # def profile(name, age=17, main_lang="파이썬"):
# #     print("이름 : {0}\t나이 : {1}\t주 사용 언어: {2}" \
# #           .format(name, age, main_lang))
# #
# # profile("RM")
# # profile("J-HOPE")
# #
# # # 키워드 값
# # def profile(name, age, main_lang):
# #     print(name, age, main_lang)
# #
# # profile(name="V", main_lang="파이썬", age=20)
# # profile(main_lang="자바", age=25, name="JK")
# #
# # # 가변 인자
# # def profile(name, age, *language): # lang1,lang2,lang3,lang4,lang5
# #     print("이름 : {0}\t나이 : {1}\t".format(name, age), end=" ") # 두 문장이 하나에 줄에 출력됨
# #     for lang in language: # print(lang1,lang2,lang3,lang4,lang5)
# #         print(lang, end=" ")
# #     print()
# #
# # profile("JM", 20, "Python", "Java", "C", "C++", "C샵")
# # profile("SUGA", 25, "Kotlin", "Swift")
#
# # 지역변수와 전역변수
# gun = 10
#
# def checkpoint(soldiers): # 경계근무
#     global gun # 전역 공간에 있는 gun 사용
#     gun = gun - soldiers
#     print("[함수 내] 남은 총 : {0}".format(gun))
#
# def checkpoint_ret(gun, soldiers):
#     gun = gun - soldiers
#     print("[함수 내] 남은 총 : {0}".format(gun))
#     return gun
#
# print("전체 총 : {0}".format(gun))
# # checkpoint(2) # 2명이 경계 근무 나감
# print("남은 총 : {0}".format(gun))

# Quiz6) 표준 체중을 구하는 프로그램을 작성하시오

# * 표준 체중 : 각 개인의 키에 적당한 체중
#
# (성별에 따른 공식)
# 남자 : 키(m) x 키(m) x 22
# 여자 : 키(m) x 키(m) x 21
#
# 조건1 : 표준 체중은 별도의 함수 내에서 계산
#     * 함수명 : std_weight
#     * 전달값 : 키(height), 성별(gender)
# 조건2 : 표준 체중은 소수점 둘째자리까지 표시
#
# (출력 예제)
# 키 175cm 남자의 표준 체중은 67.38kg 입니다.

# def std_weight(height, gender): # 키 m단위 (실수), 성별 "남자" / "여자"
#     if gender == "남자":
#         return height * height * 22
#     else:
#         return height * height * 21
#
# height = 175 # cm 단위
# gender = "남자"
# weight = round(std_weight(height / 100, gender), 2)
# print("키 {0}cm {1}의 표준 체중은 {2}kg 입니다.".format(height, gender, weight))


# Quiz7) 당신의 회사에서는 매주 1회 작성해야 하는 보고서가 있습니다.
# 보고서는 항상 아래와 같은 형태로 출력되어야
# print(합니다)
# - x 주차 주간보고 -
# 부서 :
# 이름 :
# 업무 요약 :
#
# 1주차부터 50주차까지의 보고서 파일을 만드는 프로그램을
# print(작성하시오)조건 : 파일명은 '1주차.txt', '2주차.txt', ...와 같이 만듭니다.

# for i in range(1, 51):
#     with open(str(i) + "주차.txt", "w", encoding="utf8") as report_file:
#         report_file.write("- {0} 주차 보고 -".format(i))
#         report_file.write("\n부서 :")
#         report_file.write("\n이름 :")
#         report_file.write("\n업무 요약 :")


# # 클래스
# # 마린 : 공격 유닛, 군인. 총을 쏠 수 있음
# name = "마린" # 유닛의 이름
# hp = 40 # 유닛의 체력
# damage = 5 # 유닛의 공격력
#
# print("{0} 유닛이 생성되었습니다.".format(name))
# print("체력 {0}, 공격력 {1}\n".format(hp, damage))
#
# # 탱크 : 공격 유닛, 탱크. 포를 쏠 수 있는데, 일반 모드 / 시즈 모드.
# tank_name = "탱크"
# tank_hp = 150
# tank_damage = 35
#
# print("{0} 유닛이 생성되었습니다.".format(tank_name))
# print("체력 {0}, 공격력 {1}\n".format(tank_hp, tank_damage))
#
# tank2_name = "탱크"
# tank2_hp = 150
# tank2_damage = 35
#
# print("{0} 유닛이 생성되었습니다.".format(tank2_name))
# print("체력 {0}, 공격력 {1}\n".format(tank2_hp, tank2_damage))
#
# def attack(name, location, damage):
#     print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]".format(name, location, damage))
#
# attack(name, "1시", damage)
# attack(tank_name, "1시", tank_damage)
# attack(tank2_name, "1시", tank2_damage)
#
#
# # __init__
# class Unit:
#     def __init__(self, name, hp, damage):
#         self.name = name # 멤버변수 name 에 전달값 name 저장
#         self.hp = hp
#         self.damage = damage
#         print("{0} 유닛이 생성되었습니다.".format(self.name))
#         print("체력 {0}, 공격력 {1}".format(self.hp, self.damage))
#
# # marine1 = Unit("마린", 40, 5)
# # marine2 = Unit("마린", 40, 5)
# # tank = Unit("탱크", 150, 35)
#
#
# # 멤버 변수
# # 레이스 : 공중 유닛,  비행기, 클로킹 (상대방에게 보이지 않음)
# wraith1 = Unit("레이스", 80, 5)
# print("유닛 이름 : {0}, 공격력 : {1}".format(wraith1.name, wraith1.damage))
#
# # 마인드 컨트롤  : 상대방 유닛을 내 것으로 만드는 것 (빼앗음)
# wraith2 = Unit("빼앗음 레이스", 80, 5)
# wraith2.clocking = True
#
# if wraith2.clocking == True:
#     print("{0} 는 현재 클로킹 상태입니다.".format(wraith2.name))
#
#
# # 메소드
# class AttackUnit:
#     def __init__(self, name, hp, damage):
#         self.name = name
#         self.hp = hp
#         self.damage = damage
#
#     def attack(self, location):
#         print("{0} : {1} 방향으로 적군을 공격 합합니다.[공격력{2}]"\
#               .format(self.name, location, self.damage))
#
#     def damage(self, damage):
#         print("{0} : {1} 데미지를 입었습니다. ".format(self.name, self.damage))
#         self.hp -= damage
#         print("{0} : 현재 체력은 {1} 입니다. ".format(self.name, self.hp))
#         if self.hp <= 0:
#             print("{0} : 파괴되었습니다. ".format(self.name))
#
# # # 파이어뱃 : 공격 유닛, 화염방사기.
# # firebat1 = AttackUnit("파이어뱃", 50, 16)
# # firebat1.attack("5시")
#
# # # 공격 2번 받는다고 가정
# # firebat1.damage(25)
# # firebat1.damage(25)
#
#
# # 상속, 다중상속
# # 드랍쉽 : 공중 유닛, 수송기. 마린 / 파이어뱃 / 탱크 등을 수송. 공격 X
# class Flyable:
#     def __init__(self, flying_speed):
#         self.flying_speed = flying_speed
#
#     def fly(self, name, location):
#         print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]"\
#               .format(name, location, self.flying_speed))
#
# # 공중 공격 유닛 클래스
# class FlyableAttackUnit(AttackUnit, Flyable):
#     def __init__(self, name, hp, damage, flying_speed):
#         AttackUnit.__init__(self, name, hp, damage)
#         Flyable.__init__(self, flying_speed)
#
# # 발키리 : 공중 공격 유닛, 한번에 14발 미사일 발사.
# valkrie = FlyableAttackUnit("발키리", 200, 6, 5)
# valkrie.fly(valkrie.name, "3시")
#
#
# # 메소드 오버라이딩
# # 일반 유닛
# class Unit:
#     def __init__(self, name, hp, speed):
#         self.name = name
#         self.hp = hp
#         self. speed = speed
#
#     def move(self, location):
#         print("[지상 유닛 이동")
#         print("{0} : {1} 방향으로 이동합니다. [속도 {2}]".format(self.name, location, self.speed))
# # 공격 유닛
# class AttackUnit(Unit):
#     def __init__(self, name, hp, speed, dam__init__(self, name, hp, speed, damage)):
#         Unit.__init__(self, name, hp, speed)
#         self.damage = damage
#     def attack(self, location):
#         print("{0} : {1} 방향으로 적군을 공격 합니다. [공격력 {2}]")
# # 날 수 있는 기능을 가진 클래스
# class Flyable:
#     def __init__(selfself, flying_speed):
#         self.flying_speed = flying_speed
#
#     def fly(selfself, name, location):
#         print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]".format(name, location, self.flying_speed))
#
# # 공중 공격 유닛 클래스
# class FlyableAttackUnit(AttackUnit, Flyable):
#     def __init__(self, name, hp, damage, flying_speed):
#         AttackUnit.__init__(self, name, hp, damage)

# # 벌쳐 : 지상 유닛, 기동성이 좋음
# vulture = AttackUnit("벌쳐", 80, 10,20)
#
# # 배틀크루저 : 공중 유닛, 체력도 굉장히 좋음, 공격력도 좋음.
# battlecruiser = FlyableAttackUnit("배틀크루저", 500, 25, 3)
#
# vulture.move("11시")
# # battlecruiser.fly(battlecruiser.name, "9시")
# battlecruiser.move("9시")

# pass
# 건물
# class BuildingUnit(Unit):
#     def __init__(self, name, hp, location):
#         pass

# 서플라이 디폿 : 건물, 1개 건물 = 8 유닛.
# supply_depot = BuildingUnit("서플라이 디폿", 500, "7시")
#
# def game_start():
#      print("[알림] 새로운 게임을 시작합니다.")
#
# def game_over():
#     pass
#
# game_start()
# game_over()


# # 일반 유닛
# class Unit:
#     def __init__(self, name, hp, speed): # speed 추가
#         self.name = name
#         self.hp = hp
#         self.speed = speed # 지상 이동 속도
#
#     def move(self, location): # 이동 함수 정의
#         print("[지상 유닛 이동]")
#         print("{0} : {1} 방향으로 이동합니다. [속도 {2}]"\
#             .format(self.name, location, self.speed))

# # 공격 유닛
# class AttackUnit(Unit):
#     def __init__(self, name, hp, speed, damage): # speed 추가
#         Unit.__init__(self, name, hp, speed) # speed 추가
#         self.damage = damage
#
#     def attack(self, location): # 공격 방향
#         print("{0} : {1} 방향으로 적군을 공격 합니다. [공격력 {2}]" \
#             .format(self.name, location, self.damage)) # 공간이 좁아서 2줄에 걸쳐 출력
#
#     def damaged(self, damage): # damage 만큼 유닛 피해
#         print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage)) # 데미지 정보 출력
#         self.hp -= damage # 유닛의 체력에서 전달받은 damage 만큼 감소
#         print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp)) # 남은 체력 출력
#         if self.hp <= 0: # 남은 체력이 0 이하이면?
#             print("{0} : 파괴되었습니다.".format(self.name)) # 유닛 파괴 처리
#
# #드랍쉽 : 공중 유닛, 수송기. 마린 / 파이어뱃 / 탱크 등을 수송. 공격 x

# # 날 수 있는 기능을 가진 클래스
# class Flyable:
#     def __init__(self, flying_speed): # 공중 이동 속도
#         self.flying_speed = flying_speed
#
#     def fly(self, name, location): # 유닛 이름, 이동 방향
#         print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]"\
#             .format(name, location, self.flying_speed))

# # 공중 공격 유닛
# class FlyableAttackUnit(AttackUnit, Flyable):
#     def __init__(self, name, hp, damage, flying_speed):
#         AttackUnit.__init__(self, name, hp, 0, damage) # 지상 speed 0
#         Flyable.__init__(self, flying_speed)
#
#     def move(self, location):
#         print("[공중 유닛 이동]")
#         self.fly(self.name, location)

# # 건물
# class BuildingUnit(Unit):
#     def __init__(self, name, hp, location):
#         super().__init__(name, hp, 0) # 부모 클래스 접근. self 없이 사용
#         self.location = location


# # 일반 유닛
# class Unit:
#     def __init__(self, name, hp, speed):
#         self.name = name
#         self.hp = hp
#         self.speed = speed
#         print("{0} 유닛이 생성되었습니다.".format(name))
#
#     def move(self, location):
#         # print("[지상 유닛 이동]") # 출력문 제외
#         print("{0} : {1} 방향으로 이동합니다. [속도 {2}]"\
#             .format(self.name, location, self.speed))
#
#     def damaged(self, damage): # damage 만큼 유닛 피해
#         print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage)) # 데미지 정보 출력
#         self.hp -= damage # 유닛의 체력에서 전달받은 damage 만큼 감소
#         print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp)) # 남은 체력 출력
#         if self.hp <= 0: # 남은 체력이 0 이하이면?
#             print("{0} : 파괴되었습니다.".format(self.name)) # 유닛 파괴 처리
# # 공격 유닛
# class AttackUnit(Unit):
#     def __init__(self, name, hp, speed, damage): # speed 추가
#         Unit.__init__(self, name, hp, speed) # speed 추가
#         self.damage = damage
#
#     def attack(self, location): # 공격 방향
#         print("{0} : {1} 방향으로 적군을 공격 합니다. [공격력 {2}]" \
#             .format(self.name, location, self.damage)) # 공간이 좁아서 2줄에 걸쳐 출력

# # 마린
# class Marine(AttackUnit):
#     def __init__(self):
#         AttackUnit.__init__(self, "마린", 40, 1, 5) # 이름, 체력, 이동속도, 공격력
#
#     # 스팀팩 : 일정 시간 동안 이동 및 공격 속도를 증가, 체력 10 감소
#     def stimpack(self):
#         if self.hp > 10:
#             self.hp -= 10 # 체력 10 소모
#             print("{0} : 스팀팩을 사용합니다. (HP 10 감소)".format(self.name))
#         else:
#             print("{0} : 체력이 부족하여 스팀팩을 사용하지 않습니다".format(self.name))

# # 탱크
# class Tank(AttackUnit):
#     # 시즈모드 : 탱크를 지상에 고정시켜, 더 높은 파워로 공격 가능. 이동 불가.
#     siege_developed = False # 시즈모드 개발여부
#
#     def __init__(self):
#         AttackUnit.__init__(self, "탱크", 150, 1, 35)
#         self.siege_mode = False
#
#     def set_siege_mode(self):
#         if Tank.siege_developed == False:  # 시즈모드가 개발되지 않은 경우 메소드 탈출
#             return
#
#         # 현재 시즈모드가 아닐 때 -> 시즈모드
#         if self.siege_mode == False:
#             print("{0} : 시즈모드로 전환합니다.".format(self.name))
#             self.damage *= 2  # 공격력 2배로 증가
#             self.siege_mode = True  # 시즈 모드 설정
#         # 현재 시즈모드일 때 => 시즈모드 해제
#         else:
#             print("{0} : 시즈모드를 해제합니다.".format(self.name))
#             self.damage /= 2  # 공격력 절반으로 감소
#             self.siege_mode = False  # 시즈 모드 해제
#
# #드랍쉽 : 공중 유닛, 수송기. 마린 / 파이어뱃 / 탱크 등을 수송. 공격 x

# # 날 수 있는 기능을 가진 클래스
# class Flyable:
#     def __init__(self, flying_speed): # 공중 이동 속도
#         self.flying_speed = flying_speed
#
#     def fly(self, name, location): # 유닛 이름, 이동 방향
#         print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]"\
#             .format(name, location, self.flying_speed))

# # 공중 공격 유닛 클래스
# class FlyableAttackUnit(AttackUnit, Flyable):
#     def __init__(self, name, hp, damage, flying_speed):
#         AttackUnit.__init__(self, name, hp, 0, damage) # 지상 speed 0
#         Flyable.__init__(self, flying_speed)
#
#     def move(self, location):
#         self.fly(self.name, location)

# # 레이스
# class Wraith(FlyableAttackUnit):
#     def __init__(self):
#         FlyableAttackUnit.__init__(self, "레이스", 80, 20, 5) # 체력, 공격력, 공중 이동 속도
#         self.cloaked = False # 클로킹 모드 (해제 상태)
#
#         def cloaking(self):
#             if self.cloaked == True: # 클로킹 모드 -> 모드 해제
#                 print("{0} : 클로킹 모드 해제합니다.".format(self.name))
#                 self.cloaked = False
#             else: # 클로킹 모드 해제 -> 모드 설정
#                 print("{0} : 클로킹 모드 설정합니다.".format(self.name))
#                 self.cloaked = True


# from random import *
#
# # 일반 유닛
# class Unit:
#     def __init__(self, name, hp, speed):
#         self.name = name
#         self.hp = hp
#         self.speed = speed
#         print("{0} 유닛이 생성되었습니다.".format(name))
#
#     def move(self, location):
#         print("{0} : {1} 방향으로 이동합니다. [속도 {2}]"\
#             .format(self.name, location, self.speed))
#
#     def damaged(self, damage): # damage 만큼 유닛 피해
#         print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage)) # 데미지 정보 출력
#         self.hp -= damage # 유닛의 체력에서 전달받은 damage 만큼 감소
#         print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp)) # 남은 체력 출력
#         if self.hp <= 0: # 남은 체력이 0 이하이면?
#             print("{0} : 파괴되었습니다.".format(self.name)) # 유닛 파괴 처리
# # 공격 유닛
# class AttackUnit(Unit):
#     def __init__(self, name, hp, speed, damage): # speed 추가
#         Unit.__init__(self, name, hp, speed) # speed 추가
#         self.damage = damage
#
#     def attack(self, location): # 공격 방향
#         print("{0} : {1} 방향으로 적군을 공격 합니다. [공격력 {2}]" \
#             .format(self.name, location, self.damage)) # 공간이 좁아서 2줄에 걸쳐 출력
#
# # 마린
# class Marine(AttackUnit):
#     def __init__(self):
#         AttackUnit.__init__(self, "마린", 40, 1, 5) # 이름, 체력, 이동속도, 공격력
#
#     # 스팀팩 : 일정 시간 동안 이동 및 공격 속도를 증가, 체력 10 감소
#     def stimpack(self):
#         if self.hp > 10:
#             self.hp -= 10 # 체력 10 소모
#             print("{0} : 스팀팩을 사용합니다. (HP 10 감소)".format(self.name))
#         else:
#             print("{0} : 체력이 부족하여 스팀팩을 사용하지 않습니다".format(self.name))
#
# # 탱크
# class Tank(AttackUnit):
#     # 시즈모드 : 탱크를 지상에 고정시켜, 더 높은 파워로 공격 가능. 이동 불가.
#     siege_developed = False # 시즈모드 개발여부
#
#     def __init__(self):
#         AttackUnit.__init__(self, "탱크", 150, 1, 35)
#         self.siege_mode = False
#
#     def set_siege_mode(self):
#         if Tank.siege_developed == False:  # 시즈모드가 개발되지 않은 경우 메소드 탈출
#             return
#
#         # 현재 시즈모드가 아닐 때 -> 시즈모드
#         if self.siege_mode == False:
#             print("{0} : 시즈모드로 전환합니다.".format(self.name))
#             self.damage *= 2  # 공격력 2배로 증가
#             self.siege_mode = True  # 시즈 모드 설정
#         # 현재 시즈모드일 때 => 시즈모드 해제
#         else:
#             print("{0} : 시즈모드를 해제합니다.".format(self.name))
#             self.damage /= 2  # 공격력 절반으로 감소
#             self.siege_mode = False  # 시즈 모드 해제
#
# #드랍쉽 : 공중 유닛, 수송기. 마린 / 파이어뱃 / 탱크 등을 수송. 공격 x
#
# # 날 수 있는 기능을 가진 클래스
# class Flyable:
#     def __init__(self, flying_speed): # 공중 이동 속도
#         self.flying_speed = flying_speed
#
#     def fly(self, name, location): # 유닛 이름, 이동 방향
#         print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]"\
#             .format(name, location, self.flying_speed))
#
# # 공중 공격 유닛 클래스
# class FlyableAttackUnit(AttackUnit, Flyable):
#     def __init__(self, name, hp, damage, flying_speed):
#         AttackUnit.__init__(self, name, hp, 0, damage) # 지상 speed 0
#         Flyable.__init__(self, flying_speed)
#
#     def move(self, location):
#         self.fly(self.name, location)

# # 레이스
# class Wraith(FlyableAttackUnit):
#     def __init__(self):
#         FlyableAttackUnit.__init__(self, "레이스", 80, 20, 5) # 체력, 공격력, 공중 이동 속도
#         self.cloaked = False # 클로킹 모드 (해제 상태)
#
#     def cloaking(self):
#         if self.cloaked == True:  # 클로킹 모드 -> 모드 해제
#             print("{0} : 클로킹 모드 해제합니다.".format(self.name))
#             self.cloaked = False
#         else: # 클로킹 모드 해제 -> 모드 설정
#             print("{0} : 클로킹 모드 설정합니다.".format(self.name))
#             self.cloaked = True

# def game_start():
#     print("[알림] 새로운 게임을 시작합니다.")
#
# def game_over():
#     print("Player : gg") # good game
#     print("[Player] 님이 게임에서 퇴장하셨습니다.")

# # 실제 게임 진행
# game_start()
# # 마린 3기 생성
# m1 = Marine()
# m2 = Marine()
# m3 = Marine()
#
# # 탱크 2기 생성
# t1 = Tank()
# t2 = Tank()
#
# # 레이스 1기 생성
# w1 = Wraith()
#
# # 유닛 일괄 관리 (생성된 모든 유닛 append)
# attack_units = []
# attack_units.append(m1)
# attack_units.append(m2)
# attack_units.append(m3)
# attack_units.append(t1)
# attack_units.append(t1)
# attack_units.append(w1)

# # 전군 이동
# for unit in attack_units:
#     unit.move("1시")
#
# # 탱크 시즈모드 개발
# Tank.siege_developed = True
# print("[알림] 탱크 시즈 모드 개발이 완료되었습니다.")

# # 공격 모드 준비 (마린 : 스팀팩, 탱크 : 시즈모드, 레이스 : 클로킹)
# for unit in attack_units:
#     if isinstance(unit, Marine):
#         unit.stimpack()
#     elif isinstance(unit, Tank):
#         unit.set_siege_mode()
#     elif isinstance(unit, Wraith):
#         unit.cloaking()
#
# # 전군 공격
# for unit in attack_units:
#     unit.attack("1시")
#
# # 전군 피해
# for unit in attack_units:
#     unit.damaged(randint(5, 20)) # 공격은 랜덤으로 받음 (5 ~ 20)
#
# # 게임 종료
# game_over()


# Quiz8) 주어진 코드를 활용하여 부동산 프로그램을 작성하시오.
# (출력 예제)
# 총 3대의 매물이 있습니다.
# 강남 아파트 매매 10억 2010년
# 마포 오피스텔 전세 5억 2007년
# 송파 빌라 월세 500/50 2000년
#
# class House:
#     # 매물 초기화 : 위치, 건물 종류, 매물 종류, 가격, 준공년도
#     def __init__(self, location, house_type, deal_type, price, completion_year):
#         self.location = location
#         self.house_type = house_type
#         self.deal_type = deal_type
#         self.price = price
#         self.completion_year = completion_year

#     # 매물 정보 표시
#     def show_detail(self):
#         print(self.location, self.house_type, self.deal_type, self.price, self.completion_year)
#
# houses = []
# house1 = House("강남", "아파트", "매매", "10억", "2010년")
# house2 = House("마포", "오피스텔", "전세", "5억", "2007년")
# house3 = House("송파", "빌라", "월세", "500/50", "2000년")
# houses.append(house1)
# houses.append(house2)
# houses.append(house3)

# print("총 {0}대의 매물이 있습니다.".format(len(houses)))
# for house in houses:
#     house.show_detail()

# N = int(input())
# nList = [str(i) for i in range(1, N+1)]
#
# for num in nList:
#     cnt = 0
#     if '3' in num:
#         cnt += num.count('3')
#     if '6' in num:
#         cnt += num.count('6')
#     if '9' in num:
#         cnt += num.count('9')
#     if cnt > 0:
#         print('-'*cnt, end=' ')
#     else:
#         print(num, end=' ')


# 모듈
# import theater_modlule
# theater_modlule.price(3)
# theater_modlule.price_morning(4)
# theater_modlule.price_soldier(5)
#
# import theater_modlule as mv
# mv.price(3)
# mv.price_morning(4)
# mv.price_soldier(5)
#
# from theater_modlule import *
# # from random import *
# price(3)
# price_morning(4)
# price_soldier(5)

# from theater_modlule import price, price_morning
# price(5)
# price_morning(6)
# price_soldier(7)
#
# from theater_modlule import price_soldier as price
# price(5)


# 패키지
# # from theater_module import price_soldier as price
# # price(5)
#
# import travel.thailand
# import travel.thailand.ThailandPackage
# trip_to = travel.thailand.ThailandPackage()
# trip_to.detail()

# from travel.thailand import ThailandPackage
# trip_to = ThailandPackage()
# trip_to.detail()

# from travel import vietnam
# trip_to = vietnam.VietnamPackage()
# trip_to.detail()

# #from random import *
# from travel import *
# # trip_to = vietnam.VietnamPackage()
# trip_to = thailand.ThailandPackage()
# trip_to.detail()

# import  inspect
# import  random
# print(inspect.getfile(random))
# print(inspect.getfile(thailand))







