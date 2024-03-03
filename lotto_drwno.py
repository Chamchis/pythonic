import requests

def get_lotto_info(draw_no):
    url = f'https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo={draw_no}'
    response = requests.get(url)
    data = response.json()

    numbers = [data[f'drwtNo{i}'] for i in range(1, 7)]
    bonus_number = data['bnusNo']

    return numbers, bonus_number

def print_lotto_info(draw_no):
    winning_numbers, bonus_number = get_lotto_info(draw_no)
    print(f"당첨 번호: {winning_numbers}")
    print(f"보너스 번호: {bonus_number}")

draw_no = input('원하시는 로또 회차를 입력해주세요: ')
print_lotto_info(draw_no)


import requests
number = input("회차:")
if int(number)<= 1108:
  url = f'https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo={number}'
  response = requests.get(url)
  output = response.json()
  result = []
  result = [output[f'drwtNo{i+1}'] for i in range (6)]
  result.append(output['bnusNo'])
  print(result)
else:pass