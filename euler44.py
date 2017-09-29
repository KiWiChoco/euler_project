#euler 44

import math

# pentagonal_list = [n * ((3*n-1)/2) for n in range(2,4000)]
pentagonal_list = set(n * ((3*n-1)/2) for n in range(2,4000))

for i in pentagonal_list:
    for j in pentagonal_list:
        if i + j in pentagonal_list and j - i in pentagonal_list:
            print(math.fabs(j-i))
        else : continue


#오늘도 하나배움 리스트가 존나게 크고 그 안에서 수를 search해야할때는 리스트 쓰지말자 리스트는 허벌나게 느리다
# '''why faster set than list python''' 이라고 구글링해보니 엄청나게 큰 범위의 리스트나 set에서 search할때는 set이 훨배 빠르다고한다
#실제 결과도 그렇다 리스트 개느림 set하면 순식간에 나오고