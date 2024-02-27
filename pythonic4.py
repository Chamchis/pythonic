# 4. 오류는 결코 조용히 지나가지 않아야 한다 (Errors should never pass silently)
# 오류를 명확히 하고, 적절하게 처리하세요.
# 예외 처리:
def process_data(data):
    return int(data)
data = '일이삼'
try:
    process_data(data)
except ValueError as e:
    print(f'Value Error :{e}')
except Exception as e:
    process_data(f"Unexpected error : {e}")
    # raise
