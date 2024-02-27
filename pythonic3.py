# ### **3. 가독성이 중요하다 (Readability counts)**
# 코드는 한 번 작성되고, 많이 읽힙니다. 가독성을 높이세요.
# 적절한 줄바꿈과 들여쓰기:
# 가독성 낮음
result = some_function_that_takes_a_lot_of_parameters(param1, param2, param3, param4, param5)
# 가독성 높음
result = some_function_that_takes_a_lot_of_parameters(
    param1, 
    param2,
    param3, 
    param4,
    param5
)

# 의미 있는 주석 추가:
# 현재 시간에서 일주일을 더함
next_week = current_time + timedelta(weeks=1)

# 함수와 변수의 적절한 분리:
# 가독성 낮음
print("Result:", process_data(data))
# 가독성 높음
result = process_data(data)
print("Result:", result)

# 적절한 변수명 사용:
# 낮은 가독성
d = datetime.now() + timedelta(days=1)

# 높은 가독성
tomorrow = datetime.now() + timedelta(days=1)

# 함수 분리와 적절한 주석:
# 주석 없이 긴 함수
def process():
    # 많은 코드
    pass

# 함수 분리와 주석
def load_data():
    """데이터 로딩 로직"""
    pass

def clean_data(data):
    """데이터 클리닝 로직"""
    pass

# 중첩 제한하기:
# 깊은 중첩
items = [(i,i*3)for i in range(10)]

for item in items:
    if item:
        for value in item.values():
            # Do something
            pass

# 중첩 제한
for item in items:
    if not item:
        continue
    for value in item.values():
        # Do something
        pass