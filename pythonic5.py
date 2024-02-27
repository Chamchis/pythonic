# 5. 명시적이 암시적인 것보다 낫다 (Explicit is better than implicit)
from math import sqrt
print(sqrt(4))

def make_request(url, timeout = 5):
    pass
make_request('http://naver.com',3)
make_request('http://naver.com',timeout=3)

def get_position():
  return 100, 200

x , y = get_position()

position = get_position()
x = position[0]
y = position[1]
print(x,y)

