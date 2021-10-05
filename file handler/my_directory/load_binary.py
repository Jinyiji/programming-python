import array
import os

with open('binary.bin', 'rb') as f:
    data = f.read()
print(data)

# array 로 가져오자
data = array.array('B')
with open('binary.bin', 'rb') as f:
    f.seek(0, os.SEEK_END)  # 파일 끝으로 간다.
    filesize = f.tell()     # 파일 끝 위치, 즉 파일 사이즈
    f.seek(0)
    data.fromfile(f, filesize)     # 11111111_00000000_01111111
for item in data:
    print(item)