# 특정 회차 정보를 가져오려면 어떻게 해야 되나? -> 함수
# 그 회차의 당첨번호, 보너스 번호는 몇번인가? -> 함수

import requests

drwno = input('원하시는 로또 회차를 입력해주세요 : ')

def lotto_drwNo(drwno):
    url = 'https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo={}'.format(drwno)
    response = requests.get(url)
    print(response)  # <Response [200]>은 서버로부터의 요청이 성공적으로 처리되었음을 나타내는 상태 코드
    output = response.json()
    return output

def lotto_drwt_n_bonusNo(output):
    drwt_numbers = []
    for i in range(1, 7):
        drwt_numbers.append(output[f'drwtNo{i}'])
    bnus_number = output['bnusNo']
    return drwt_numbers, bnus_number


output = lotto_drwNo(drwno)
print(f'로또 {drwno} 회차의 정보는 {output} 입니다!.')
result_no = lotto_drwt_n_bonusNo(output)
print(f'당첨 번호와 보너스 번호는 {result_no} 입니다!.')