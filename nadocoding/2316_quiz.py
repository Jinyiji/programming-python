'''
3. Quiz
3-1.주민등록번호 앞 6자리를 변수 id_number에 넣고,
출생년도 끝 두자리\n출생 월일\n그 두개의 합 출력

예시
id_number = 020316 일 때

출력 예시
02
0316
632
'''

# id_number = "020316"
# print(id_number[0:2])     # year = id_number[0:2], [:2], [-6:-4]
# print(id_number[2:6])     # month_day = id_number[2:6], [2:], [-4:] // 끝까지라 [2:]만 적어도 됨
# a = id_number[0:2]        # print(year)
# b = id_number[2:6]        # print(month_day)
# print(int(a)*int(b))      # print(int(year) * int(month_day))


# 3-2. 집 전화번호를 phone_number에 넣고,
# 지역번호\n맨 끝 네 자리 출력하기(지역번호의 자리수와 상관없이 동작하도록 하자)

# 예시
# phone_number = 02-1234-5678 또는 032-9876-4321

# 출력 예시
# 02 또는 032
# 5678 또는 4321

# phone_number = "02-1234-5678"
# x = phone_number.index('-')       # 없으면,valueError    ,find() 없으면 -1
# print(phone_number[0:x])          # [:2]
# print(phone_number[-4:])          # [8:]
#
# phone_number2 = "032-1234-5678"
# x = phone_number2.index('-')
# print(phone_number2[0:x])         # [:3]
# print(phone_number2[-4:])         # [9:]

# 전화번호 입력시, -가 있든, -가 없든, 찰떡같이 알아먹기
# phone_number1 = '010-1234-5678'
# phone_number2 = '01098765432'
# phone_number3 = '010 1111 2222'
#
# phone_number = phone_number3
# result = phone_number.replace('-', '').replace(' ', '')
# print(result)


# Quiz2-1)
# 학번을 student_number 변수에 넣고, 학급을 출력하고, 학과를 출력하기
# 반이 0 미만이거나 7 이상이면 "잘못 입력했습니다." 출력하기
# student_number = '2100' 또는 student_number = '2000'
# <출력 예시>
# 1반 뉴미디어소프트웨어과 또는 잘못 입력했습니다.

# student_number = '2316'
# number = student_number[1]         #[1:2]       #'3'
# number = int(number)               # str -> int

# if student_number[1]=='1':
#     print(f"{number}반 뉴미디어소프트웨어과")
# elif student_number[1]=='2':
#     print(f"{number}반 뉴미디어소프트웨어과")
# elif student_number[1] == '3':
#     print(f"{number}반 뉴미디어웹솔루션과")
# elif student_number[1] == '4':
#     print(f"{number}반 뉴미디어웹솔루션과")
# elif student_number[1] == '5':
#     print(f"{number}반 뉴미디어디자인과")
# elif student_number[1] == '6':
#     print(f"{number}반 뉴미디어디자인과")
# else:
#     print("잘못 입력했습니다.")
# majors = ['뉴미디어소프트웨어과', '뉴미디어소프트웨어과', '뉴미디어웹솔루션과', '뉴미디어웹솔루션과', '뉴미디어디자인과', '뉴미디어디자인과']
# print(f'{number}반 {majors[number-1]}')

# majors = ['뉴미디어소프트웨어과', '뉴미디어웹솔루션과', '뉴미디어디자인과']
# if 1 <= number <= 6:            # 1 <= number && number <= 6 in java
#     print(f'{number}반 {majors[(number - 1) // 2]}')
# else:
#     print("잘못입력했습니다.")


# Quiz2-2)
# 학번을 함수의 인수(argument)로 전달하여 호출하면 학년과 학과를 리턴하는 함수 만들기
# <함수 호출>
# grade, major = get_major('2100')
# print(major, grade)       #뉴미디어소프트웨어과 2

# def get_major(number):
#     major = "잘못입력했습니다."
#     grade = number[0]
#     if number[1] == '1' or number[1] == '2':
#         major = "뉴미디어소프트웨어과"
#     elif number[1] == '3' or number[1] == '4':      # '4' == True
#         major = "뉴미디어웹솔루션과"
#     elif number[1] == '5' or number[1] == '6':
#         major = "뉴미디어디자인과"
#     return major, grade
# major, grade = get_major("2316")
# print(major, grade)

# Quiz2-3)
# 인수의 개수에 상관없이 인수로 숫자를 여러개 넣고, 함수를 호출하면 그 인수들의 평균을 구하여 리턴하는 함수 만들기
# <함수 호출>
# print(average(10, 20, 30)) #20.0
# print(average(4, 23)) #13.5

# def average(*num):
#     sum=0
#     for n in num:
#         sum+=n
#     return sum/len(num)
# print(average(10, 20, 30)) #20.0
# print(average(4, 23)) #13.5


# Quiz2-4)
# 키(cm)와 몸무게(kg)를 인수로 넣고, 함수를 호출하여 BMI 지수를 리턴하는 함수 만들기
# (소수 첫째자리까지 반올림)
# * BMI 지수 계산법: 체중(kg) ÷ 키의 제곱(m²)
# 18.5 미만: 저체중
# 18.5 이상 23 미만: 보통
# 23 이상 25 미만: 과체중
# 25 이상: 비만

# <함수 호출>
# bmi = get_bmi(176, 69)
# print(bmi) #22.3

# def get_bmi(height, weight):
#     # height /= 100
#     bim = round((weight/ (height**2))*10000, 1)
#     return bim
#
# bmi = get_bmi(178.8, 62)
# # print(bmi)
# if bmi < 18.5:
#     print('저체중')
# elif bmi < 23:
#     print('정상')
# elif bmi < 25:
#     print('과체중')
# elif 25 <= bmi:
#     print('비만')

# 구구단 7단 출력하기
# for i in range(1, 9 + 1):    # i : 1~9
#     print(f'7 x {i} = {7 * i}')

# 구구단 2~9단 출력하기
# for dan in range(2, 10):    # dan : 2~9
#     for i in range(1, 9 + 1):    # i : 1~9
#         print(f'{dan} x {i} = {dan * i}')
#     print('-' * 10) # 1번

# 구구단 2~7단까지 출력하기
# for dan in range(2, 9 + 1):    # dan : 2~9
#     for i in range(1, 9 + 1):    # i : 1~9
#         print(f'{dan} x {i} = {dan * i}')
#     print('-' * 10)
#     if dan == 7:
#         break

# 구구단 2~7단 출력하되, x1, x3, x5, x7, x9 인 것만 출력하기
# for dan in range(2, 9 + 1):    # dan : 2~9
#     for i in range(1, 9 + 1):    # i : 1~9
#         if i % 2 == 0:   # i == 2 or 4 or i == 6 or i == 8:
#             continue
#         print(f'{dan} x {i} = {dan * i}')
#     print('-' * 10)
#     if dan == 7:
#         break


# '''
# Quiz3-1. n_sum() 함수를 만든다.
# 함수의 인수(argument)로 10자리 숫자보다 작은 숫자를 넣으면,
# 각 자리의 숫자의 합계를 리턴한다. 10자리 이상이면 -1 리턴한다.
# '''
# # argument 가 원래 숫자
# def n_sum(argument):
#     num = str(argument)  # str 문자열 |글자 길이 수를 구하기 위해 str 문자열로 바꾸기
#     if len(num) >= 10: return -1  # num 의 길이가 10보다 크면은 -1을 리턴,
#     elif 10 > argument: return argument   # 10보다 작을 경우 다시 argument 를 리턴해서
#     sum = 0
#     for n in range(0, len(num)):  # for 문을 통해 0부터 num 의 길이만큼 sum 에다가 num 값을 더한다
#         sum += int(num[n])
#     return sum

# 함수에 값을 넘기고 리턴값을 result 에 담고 출력
# result = n_sum(10)
# print(result)         # 1
# result = n_sum(331)
# print(result)         # 7
# result = n_sum(408)
# print(result)         # 12
# result = n_sum(1000000000)
# print(result)         # -1
#
#
# '''
# Quiz3-2. get_subway_fare() 함수를 만든다.
# 이 함수는 인수로 가는 거리(km)를 숫자로 넣으면, 요금을 리턴한다.
# * 지하철 요금계산법 10km 이내: 720원(청소년),
# 10~50km: 5km 마다 100원, 50km 초과 시 8km마다 100원
# '''
# / : 두 수를 나눈다
# // : 두 수를 나눠 몫을 출력한다
# % : 두 수를 나눠 나머지를 출력한다
# import math #
# def get_subway_fare(km):
#     money = 720
#     if 10 > km:  # 10km 이내인 경우 720원을 바로 리턴해주고,
#         return money
#     elif 10 <= km <= 50: # 10부터 50사이
#         return money + math.ceil((km-10)/5)*100  # ceil 로 올림함수
#         # 기본요금 720원과 5km 마다 생기는 추가요금을 구해 리턴.
#     else:
#         return money + ((50-10) / 5 * 100) + math.ceil((km - 50) / 8) * 100 # 40 나누기 5곱하기 100
# 그리고 50km 초과 시에는 기본요금과 10~50km 사이의 추가 요금, 50km의 추가요금을 구해 리턴.

# 함수에 값을 넘기고 리턴값을 result 에 담고 출력
# fare = get_subway_fare(5)
# print(fare)        # 720
# fare = get_subway_fare(25)
# print(fare)        # 1020
# fare = get_subway_fare(26)
# print(fare)        # 1120
# fare = get_subway_fare(61)
# print(fare)        # 1720
#
#
# '''
# Quiz3-3. get_three_six_nine() 함수를 만든다.
# 이 함수에 숫자를 입력하면 369 게임에  해당하는 답변을 리턴한다.
# * 369게임: 숫자의 어느 자리든 3 또는 6 또는 9가 있다면
# 그 갯수만큼 '짝'을 외치고, 아니면 그냥 숫자를 외친다.
# '''
# # 숫자타입으로 넘어오는 number 를 문자열로 형변환
# def get_three_six_nine(number):
#     # if('3' in number) or ('6' in number) or ('9' in number):
#     count = str(number).count('3') + str(number).count('6') + str(number).count('9')
#     # 문자열의 갯수를 세는 count 를 이용해서 3,6,9가 들어간 갯수를 세서 count 변수에 담은 뒤
#     if count == 0:  # count 의 갯수가 0인 경우는 number 을 그대로 리턴
#         return number
#     else:
#         return ("짝" * count)  # count 의 갯수만큼 "짝"을 곱해서 리턴

# 함수에 값을 넘기고 리턴값을 result 에 담고 출력
# result = get_three_six_nine(1)
# print(result)        # 1
# result = get_three_six_nine(3)
# print(result)        # 짝
# result = get_three_six_nine(16)
# print(result)        # 짝
# result = get_three_six_nine(36)
# print(result)        # 짝짝
#

# ''
# # Quiz3-4. 나만의 재미난 문제를 만들어보세요. 단, 조건이 있습니다.
# # 1. 함수의 이름을 정해준다.
# # 2. 인수로 넣어야하는 자료형이나 개수를 말해준다.
# # 3. 리턴하는 것을 말해준다.
# # 4. 출력 예시를 보여준다.
# # 5. 내가 낸 문제의 답안을 제출한다.

# # 소수판별 함수
# def PrimeNumber(number):
#     if number != 1:
#         for i in range(2, number):
#             if number % i == 0:
#                 return False
#     else:
#         return False
#     return True
# # i가 공약수 공약수가 있으면 소수가 아닌 걸로 출력
# # 다 나눴을 때 0이 안 되면 num숫자 제외 소수입니다로 출력됨
# # 문제점 1이 아닌 모든 숫자가 소수라고 뜬다.
# num = input("숫자를 입력하세요 : ")
# if PrimeNumber(int(num)):
#     print(num+"은 소수 입니다.")
# else:
#     print(num+"은 소수가 아닙니다.")


# Quiz4-1. [학생퀴즈] 소수판별하기
# (소수: 1이나 자기자신으로만 나누어 떨어지는 수)
# is_prime() 함수를 만든다. 인수로 1개의 숫자를 받는다.
# 인수로 넘어온 숫자가 소수(prime number)이면 "소수" 아니면,
# "소수 아님" 리턴한다.
# def is_prime(x):
#   for i in range(2, x):
#     if x % i == 0:
#     	return '소수아님'
#   return '소수'
#
# result = is_prime(2)
# print(result)     #소수
# result = is_prime(13)
# print(result)     #소수
# result = is_prime(36)
# print(result)     #소수 아님


#
# Quiz4-2. [학생퀴즈] get_compliment() 함수를 만든다.
# 이 함수에 '고구마' 또는 '맛있는'이 들어가는 말을 입력하면
# 그에 해당하는 답변을 리턴한다. '고구마'가 들어가는 말을 입력하면
# '왓쇼이!', '맛있는'이 들어가는 말을 입력하면 '우마이!',
# '놀랄 만한', '황당한', '굉장한'이 들어가는 말을 입력하면
# '요모야..!', 특정 단어가 하나라도 들어가지 않는다면 '으무!'를 리턴한다.

# def get_compliment(word):
#     if '고구마'in word:
#         return '왓쇼이!'
#     elif '맛있는'in word:
#         return '우마이!'
#     elif '놀랄 만한'in word:
#         return '요모야..!'
#     elif '황당한'in word:
#         return '요모야..!'
#     elif '굉장한'in word:
#         return '요모야..!'
#     else:
#         return '으무!'
#
# result = get_compliment('고구마 된장국')
# print(result) # 왓쇼이!
# result = get_compliment('맛있는 크레이프')
# print(result) # 우마이!
# result = get_compliment('놀랄 만한 상황')
# print(result) # 요모야..!
# result = get_compliment('좋은 마음가짐이다!')
# print(result) # 으무!



# Quiz5-1. 모듈이란?
# 필요한 것들끼리 부품처럼 만들어진 파일, 모듈의 확장자는 .py
# 부품만 교체하거나 추가할 수 있는, 코드의 재사용이 수월해지는 장점을 가짐.
# 함수 정의나 클래스 등의 파이썬 문장들을 담고 있는 파일을 모듈이라 한다.

# Quiz5-2.패키지란? 모듈들을 모아놓은 집합. 하나의 디렉터리에 여러 모듈 파일들을 모아놓은 것.
# 하나의 디렉터리에 여러 모듈 파일들을 모아놓은 것.

# Quiz5-3. theater_module.py 모듈(파일)의 price 함수를
# p학번 라는 이름으로 호출 하도록 import문을 작성하세요
# import theater_module
# p학번.price(3)

# Quiz5-4. __all__의 역할은?
# 그 구문에 대한 정보를 가져올 수 있다.
# 모듈의 이름을 담는 리스트

# Quiz5-5. 지금 파이썬 파일을 직접실행할 때만 실행되고,
# 다른 모듈에서 import 할 때는 실행되지 않도록 하는 제어문은?
# if __name__ == "__main__":

# Quiz5-6. travel 패키지(폴더) 안에 vietnam.py
# 모듈(파일) 안의 ThailandPackage 클래스를 생성하고
# detail 함수를 호출하는 < 가 >, < 나 >, < 다 > 에 들어갈 각 방법은?
# import travel.vietnam
# < 가 >
# trip_to = travel.vietnam.VietnamePackage()
# trip_to.detail()

# from travel import vietnam
# < 나 >
# trip_to = vietnam.VietnamePackage()
# trip_to.detail()

# from travel.vietnam import ThailandPackage
#
# < 다 >
# trip_to = VietnamePackage()
# trip_to.detail()






