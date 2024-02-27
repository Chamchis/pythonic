# 특정 회차 정보를 가져오려면 어떻게 해야 되나? -> 함수
# 그 회차의 당첨번호, 보너스 번호는 몇번인가? -> 함수

import requests

drwno = input('원하시는 로또 회차를 입력해주세요 : ')
numbers = [int(input('당신의 번호 6자리 + 보너스 번호 1자리를 입력하세요 : ')) for i in range(7)]

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
    bonus_number = output['bnusNo']
    return drwt_numbers, bonus_number

def check_winning(numbers,result_no):
    drwt_numbers, bonus_number = result_no
    your_numbers = numbers[:6]
    your_bonus_number = numbers[6]

    if all(num in drwt_numbers for num in your_numbers) and your_bonus_number == bonus_number:
        print('축하합니다! 로또에 당첨되셨습니다!')
    else:
        print('아쉽지만 로또에 당첨되지 않았습니다.')

# 로또 정보
output = lotto_drwNo(drwno)
print(f'로또 {drwno} 회차의 정보는 다음과 같습니다!.')
print(f'날짜 : {output["drwNoDate"]}')
print(f'총 상금액 : {output["totSellamnt"]}')
print(f'1등 상금액 : {output["firstWinamnt"]}')
print(f'1등 당첨 총 금액 : {output["firstAccumamnt"]}')
print(f'당첨번호 1번 : {output["drwtNo1"]}')
print(f'당첨번호 2번 : {output["drwtNo2"]}')
print(f'당첨번호 3번 : {output["drwtNo3"]}')
print(f'당첨번호 4번 : {output["drwtNo4"]}')
print(f'당첨번호 5번 : {output["drwtNo5"]}')
print(f'당첨번호 6번 : {output["drwtNo6"]}')
print(f'보너스 번호 : {output["bnusNo"]}')


result_no = lotto_drwt_n_bonusNo(output)
print(f'당첨 번호와 보너스 번호는 {result_no} 입니다!.')
check_winning(numbers,result_no)


#zzzzzz
# 깃허브 데스크탑입니다ㅋㅋㅋ