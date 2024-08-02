import os
import boto3
import datetime
import requests
import calendar
from currency_converter import CurrencyConverter

# 환율 정보를 가져오는 함수


def get_exchange_rate():
    url = 'https://www.ecb.europa.eu/stats/eurofxref/eurofxref-hist.zip'
    # ECB에서 제공하는 환율 데이터를 사용하여 CurrencyConverter 객체 생성
    c_list = CurrencyConverter(url)
    # USD에서 KRW로 변환하는 환율 반환
    return c_list.convert(1, 'USD', 'KRW')

# AWS 비용을 가져오는 함수


def get_aws_cost():
    # AWS Cost Explorer 클라이언트 생성
    client = boto3.client(
        'ce',
        aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
        aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY')
    )

    # 현재 시간 가져오기
    now = datetime.datetime.utcnow()
    # 이번 달의 시작 날짜와 마지막 날짜 설정
    start = now.replace(day=1).strftime('%Y-%m-%d')
    last_day_of_month = calendar.monthrange(now.year, now.month)[1]
    end = now.replace(day=last_day_of_month).strftime('%Y-%m-%d')

    # 비용과 사용량 데이터를 요청
    response = client.get_cost_and_usage(
        TimePeriod={
            'Start': start,
            'End': end
        },
        Granularity='MONTHLY',
        Metrics=['UnblendedCost'],
        GroupBy=[
            {
                'Type': 'DIMENSION',
                'Key': 'SERVICE'
            }
        ]
    )

    # 총 비용 계산
    total_cost = 0
    for result in response['ResultsByTime']:
        for group in result['Groups']:
            total_cost += float(group['Metrics']['UnblendedCost']['Amount'])

    return total_cost

# 디스코드로 메시지를 보내는 함수
def send_to_discord(cost_usd, cost_krw):
    webhook_url = os.getenv('DISCORD_WEBHOOK_URL')
    # 메시지 데이터 생성
    data = {
        "content": f"{datetime.datetime.now().strftime('%Y년 %m월 %d일')}까지의 피같은 AWS 비용은 \n```달러로 {cost_usd:,.2f}$\n한화로 {cost_krw:,.2f}원```입니다. :sob: "
    }
    # 디스코드 웹훅 URL로 POST 요청 보내기
    response = requests.post(webhook_url, json=data)
    if response.status_code != 204:
        raise Exception(
            f"Request to discord returned an error {response.status_code}, the response is:\n{response.text}")

# 메인 함수
def main():
    # AWS 비용 가져오기
    cost_usd = get_aws_cost()
    # 환율 정보 가져오기
    exchange_rate = get_exchange_rate()
    # USD 비용을 KRW로 변환
    cost_krw = cost_usd * exchange_rate
    # 디스코드로 메시지 전송
    send_to_discord(cost_usd, cost_krw)


if __name__ == '__main__':
    main()
