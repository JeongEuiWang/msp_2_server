# MSP Server

FastAPI와 MySQL을 사용하는 마이크로서비스 프로젝트입니다.

## 기술 스택

- Python 3.12
- Poetry 2.1.1
- FastAPI
- MySQL
- Alembic (데이터베이스 마이그레이션)

## 시작하기

### 환경 설정

1. `.env` 파일을 생성하고 다음과 같이 설정하세요:

```
# 데이터베이스 설정
DB_HOST=localhost
DB_PORT=3306
DB_USER=username
DB_PASSWORD=password
DB_NAME=database_name
```

### 실행 방법

Makefile을 이용하여 다음 명령어로 프로젝트를 설정하고 실행할 수 있습니다:

```bash
# 의존성 설치 및 가상환경 설정
make setup

# 서버 실행
make run
```

## 데이터베이스 마이그레이션

Alembic을 사용하여 데이터베이스 마이그레이션을 관리합니다.

```bash
# 마이그레이션 생성
alembic revision --autogenerate -m "설명"

# 마이그레이션 적용
alembic upgrade head
``` 