#  정석
# try:
#     f = open('text.txt', 'w')
#
#     f.write('hello')
#     f.write('월드')
# except:
#     pass
# finally:
#     f.close()

f = open('text.txt', 'w', encoding='utf-8')

f.write('hello')
f.write('\n')
f.write('월드')

f.close()

print('with')
with open('text.txt', 'w', encoding='utf-8') as f:
    f.write('hello')
    f.write('\n')
    f.write('월드')