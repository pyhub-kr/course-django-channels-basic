# [인프런] 파이썬/장고와 함께 웹소켓 채팅 서비스 만들기 (기본편)

[![인프런 배너](./assets/banner.png)](https://inf.run/aaW4)

## 실행 방법

1. 가상환경 생성 및 활성화, 팩키지 설치

```
python -m venv venv

venv\Scripts\activate  # windows
source ./venv/bin/activate  # mac/linux

pip install -r requirements/dev.txt
```

2. 유저 간 채팅을 위해 Redis 서버 설치가 필요합니다. 도커가 설치되어있으시다면 아래 명령으로 redis 서버를 로컬에 구동하실 수 있습니다.

```
docker run -p 6379:6379 -d redis:7
```

3. 환경변수 `CHANNEL_LAYER_REDIS_URL`로 아래와 같이 redis 접속 정보를 지정합니다.

프로젝트 루트에 `.env` 파일을 생성하셔도, `mysite/settings.py` 내에서 로딩합니다.

```
CHANNEL_LAYER_REDIS_URL=redis://:@localhost:6379
```

4. 개발서버 구동

```
python manage.py migrate

python manage.py runserver
```

