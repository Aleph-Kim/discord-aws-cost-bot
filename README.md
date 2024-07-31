# 📊 Discord AWS Cost Bot 💸
Discord AWS Cost Bot은 매일 00시에 디스코드 채널에 이번 달 AWS 서버 비용을 발송하는 봇입니다! 아래는 사용법과 디렉토리 구조를 설명입니다.

사용법에 대한 설명은 블로그에서도 확인할 수 있습니다! [Aleph Kim의 IT 블로그](https://dev-kimchi.tistory.com/entry/Discord-AWS-%EC%9A%94%EA%B8%88-%EC%95%8C%EB%A6%BC-%EB%B4%87)

---

## 📚 라이브러리 설명

1. `boto3`: AWS SDK for Python으로, AWS 서비스와의 상호작용을 쉽게 할 수 있게 해줍니다. S3, EC2, DynamoDB 등 다양한 AWS 서비스의 API를 간편하게 호출할 수 있습니다.

2. `requests`: 간단하고 직관적인 HTTP 요청을 보낼 수 있게 해주는 Python 라이브러리입니다. REST API 호출 시 유용하게 사용할 수 있습니다.

3. `CurrencyConverter`: 실시간 환율 정보를 제공하여 다양한 통화를 간편하게 변환할 수 있도록 도와주는 Python 라이브러리입니다. AWS 비용을 다양한 통화로 변환할 때 유용합니다.

4. `APScheduler`: 작업 스케줄링을 쉽게 할 수 있게 해주는 Python 라이브러리입니다. 크론 표현식을 사용하여 주기적으로 작업을 실행할 수 있으며, 시간 기반 작업을 간편하게 설정할 수 있습니다.

---

## 🗂 디렉토리 구조
```
discord-aws-cost-bot/
├── Dockerfile.dev
├── Dockerfile.prod
├── docker-compose.yml
├── main.py
├── requirements.txt
├── scheduler.py
└── .env
```

---

## 📄 파일 설명
- `Dockerfile.dev`: 개발 환경을 위한 도커파일입니다. 개발 시 봇을 즉시 실행할 수 있도록 설정되어 있습니다.

- `Dockerfile.prod`: 프로덕션 환경을 위한 도커파일입니다. 스케줄러를 사용하여 매일 정오(00시)에 봇을 실행하도록 설정되어있습니다.

- `docker-compose.yml`: 도커 컴포즈 파일로, 개발 및 프로덕션 환경 설정을 포함하고 있습니다.

- `main.py`: 봇의 주요 로직을 포함한 파일입니다. AWS 비용을 가져오고, 이를 디스코드 채널에 발송하는 기능을 담당합니다.

- `requirements.txt`: 프로젝트에서 필요한 python 라이브러리를 명시한 파일입니다.

- `scheduler.py`: APScheduler 라이브러리를 이용해 매일 00시에 main.py의 작업을 실행하도록 스케줄링하는 파일입니다.

---

## 🚀 설치 및 사용법
1. 저장소 클론
```
git clone https://github.com/Aleph-Kim/discord-aws-cost-bot
cd discord-aws-cost-bot
```
2. 환경 변수 설정
  .env 파일을 생성하고 AWS 및 디스코드 토큰 등 필요한 환경 변수를 설정합니다.

3. 도커 이미지 빌드 및 컨테이너 실행
```
# 개발 환경
docker-compose up dev --build

# 프로덕션 환경
docker-compose up prod --build
```

---

## 🛠 주요 기능
- 💰 AWS 비용 조회
- 📢 디스코드 채널에 메시지 발송
- 🕛 매일 00시에 작업 실행

필요에 따라 코드를 수정하여 시간대를 변경하거나 문구를 변경하셔도 됩니다!
자유롭게 수정 / 배포하며 사용해주세요

🌟 Happy Coding! 🌟
