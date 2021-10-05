# 파일 저장
with open('my_favorite_music.txt', 'w', encoding='utf-8') as f:
    f.write('진이지: only(이하이)\n')
    f.write('주서영: 낙하\n')


# 파일 불러오자
with open('my_favorite_music.txt', 'r', encoding='utf-8') as f:
    while True:
        line = f.readline()     # '진이지: only(이하이)\n'
        if line == '':
            break
        # 이름: 진이지[Tab] 좋아하는 음악: only(이하이)
        line_list = line.split(':')     # ['진이지', ' only(이하이)\n']
        name = line_list[0]
        music = line_list[1].rsplit()
        print(f'이름: {name}\t좋아하는 음악: {music}')
        # print(line_list)
        # print(line.rstripe())

