# 2. 단순함이 복잡함보다 낫다 (Simple is better than complex)
# 리스트 컴프리헨션 사용:
# 복잡
result = []
for i in range(10):
    if i % 2 == 0:
        result.append(i*i)
# 단순
result = [i*i for i in range(10) if i % 2 == 0]

# 함수 분리:
# 복잡
def process_data(data):
    # 데이터 전처리
    # 데이터 처리
    # 결과 반환
# 단순
def preprocess_data(data):
    pass
def process_data(data):
    pass
def return_data(data):
    pass

# 내장 함수 사용:
# 복잡
nums = [i for i in range(100)]
total = 0
for num in nums:
    total += num
average = total / len(nums)
# 단순
average = sum(nums) / len(nums)

# 조건문 간소화:
# 복잡함
if status == "success" or status == "complete" or status == "finished":
    pass

# 단순함
if status in ["success", "complete", "finished"]:
    pass

# Loop 대신 List Comprehension 사용:
# 복잡함
result = []
for i in range(10):
    if i % 2 == 0:
        result.append(i**2)

# 단순함
result = [i**2 for i in range(10) if i % 2 == 0]