# 파이썬 객체 그대로 저장
import pickle
from person import Person

if __name__ == 'main__':
    번호1 = Person('박지민', 'love nwantiti')
    번호3 = Person('김석진', '곰세마리')
    절친 = [번호1, 번호3]

    with open('object.bin', 'wb') as f:
        pickle.dump(번호1, f)

    with open('objects.bin', 'wb') as f:
        pickle.dump(절친, f)

    with open('object.bin', 'rb') as f:
        data = pickle.load(f)
    print(f'load한 데이터: {data}')
