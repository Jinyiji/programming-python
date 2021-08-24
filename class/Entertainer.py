class Entertainer:  # 키, 얼굴, 인성, 이름
    def __init__(self, name):
        self.name = name

    def set_height(self, height):
        self.height = height

    def set_face(self, face):
        self.face = face

    def set_kind(self, kind):   # 인성
        self.kind = kind

    def set_name(self, name):
        self.name = name

    def info(self):
        print(f'이름: {self.name}\t키: {self.height}\t얼굴: {self.face}\t인성: {self.kind}')

    def __str__(self):
        return f'이름: {self.name}\t키: {self.height}\t얼굴: {self.face}\t인성: {self.kind}'

뷔 = Entertainer('뷔')
# 아이유.set_name('이지은')
뷔.set_height('179cm')
뷔.set_face('진이지 이상형')
뷔.set_kind('착함 그 자체')
print(뷔)

class Singer(Entertainer):
    def __init__(self, name, song):
        super().__init__(name)
        self.song = song

    def __str__(self):
        return super().__str__() + f'\t대표곡: {self.song}'

class Talent(Entertainer):
    def __init__(self, name, drama):
        super().__init__(name)
        self.drama = drama

    def __str__(self):
        return super().__str__() + f'\t드라마: {self.drama}'

뷔 = Singer('뷔', 'Love Maze')
뷔.set_height('179cm')
뷔.set_face('진이지 이상형')
뷔.set_kind('That\'s very good and cute.')
print(뷔)

송강 = Talent('송강', '스위트홈')
송강.set_height('185cm')
송강.set_face('비율최강')
송강.set_kind('착한듯')
print(송강)

지민 = Singer('지민', 'Save Me')
지민.set_height('174cm')
지민.set_face('강양이상')
지민.set_kind('천사임')
print(지민)

방탄소년단 = []
방탄소년단.append(뷔)
방탄소년단.append(지민)
print(방탄소년단)


