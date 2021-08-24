class Icecream:
    def __init__(self, name, flavor):
        self.name =name
        self.flavor = flavor
    # 맛: taste, flavor, 설명: descripiton

    def set_description(self, descripiton):
        self.description = descripiton

    def __str__(self):
        return f'이름: {self.name}\t맛: {self.flavor}'

# 엄마는외계인 = Icecream('엄마는외계인', '초콜릿, 화이트무스')
# 엄마는외계인.set_description('밀크 초콜릿, 다크 초콜릿, 화이트 무스 세 가지 아이스크림에 달콤 바삭한 초코볼이 더해진 아이스크림')
# print(엄마는외계인)
# print(엄마는외계인.description)
#
# 해피버스데이 = Icecream('해피버스데이', '케이크맛', '바닐라향, 큐브')
# print(해피버스데이)
#
# 오레오쿠키앤크림 = Icecream('오레오쿠키앤크림', '바닐라향', '오레오')
# print(오레오쿠키앤크림)

class Cup:
    _CUP_CATEGORIES = ['싱글컵', '더블컵', '파인트']
    _PRICES = [4000, 6200, 8200]
    # _CUP_CATEGORIES[0]
    def __init__(self, name, count_flavor):
        self.name = name
        self.count_flavor = count_flavor
        self.price = Cup._PRICES[self.count_flavor - 1]
        self.menu = []
        self.add_menu()
        self.order_menu = []

    def add_menu(self):
        엄마는외계인 = Icecream('엄마는외계인', '초콜릿, 화이트무스')
        # 엄마는외계인.set_description('밀크 초콜릿, 다크 초콜릿, 화이트 무스 세 가지 아이스크림에 달콤 바삭한 초코볼이 더해진 아이스크림')

        해피버스데이 = Icecream('해피버스데이', '케이크맛, 케이크큐브')

        오레오쿠키앤크림 = Icecream('오레오쿠키앤크림', '바닐라,오레오')

        self.menu.append(엄마는외계인)
        self.menu.append(해피버스데이)
        self.menu.append(오레오쿠키앤크림)

    def show_menu(self):
        for index, icecream in enumerate(self.menu):
            print(index+1, icecream)

    def order(self):
        for n in range(self.count_flavor):
            self.show_menu()                    # 메뉴 보여주기
            flavor = input('맛을 고르세요: ')     # 사용자 선택
            flavor = int(flavor)                # 인덱스를 위해 문자 -> 숫자
            icecream = self.menu[flavor - 1]    # 메뉴에서 인덱스로 가져오기
            self.order_menu.append(icecream)    # 주문한 메뉴 추가
        print('주문한 아이스크림입니다.')
        for icecream in self.order_menu:        # 주문 내역 보여주기
            print(icecream)


    def __str__(self):
        return f'이름: {self.name}\t가격: {self.price}원\t종류: {Cup._CUP_CATEGORIES[self.count_flavor-1]}'

이지꺼 = Cup('더블컵', 2)
print(이지꺼)
이지꺼.order()
