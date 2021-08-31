import math
print(math.ceil(3.5))       # 4 천장 올림
print(math.ceil(3.4))       # 4
print(math.floor(3.5))      # 3
print(math.floor(3.4))      # 3
print(round(3.5))           # 4 반올림
print(round(3.4))           # 3
print(math.pow(2, 10))      # 1024.0
print(math.sin(math.pi/2))  # 1.0


import random
print('-'*20)
print(random.random())          # 0.0 <= r < 1.0
print(random.randrange(1, 10))  # 1 <= r < 10 정수
print(random.randint(1, 10))    # 1 <= r <= 10 정수
list1 = ['김치찌개', '비빔면', '안 먹고 잠']
print(random.choice(list1))

print('before: ', list1)
random.shuffle(list1)
print('after: ', list1)

print(random.sample(list1, 2))


import datetime
print('-'*20)
now = datetime.datetime.now()
print(now)
birthday = datetime.datetime(2004, 10, 14, 15, 58)
print(birthday)
print(now - birthday)
