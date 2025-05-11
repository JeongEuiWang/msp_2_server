.PHONY: setup run migrate migrate-up migrate-down

# 가상환경 및 의존성 설치
setup:
	@pip install poetry==2.1.1 setuptools
	@poetry env use python3.12
	@poetry install

# 서버 실행
run:
	@poetry run uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload

# 마이그레이션 생성
migrate:
	@poetry run alembic revision --autogenerate -m "$(m)"

# 마이그레이션 적용
migrate-up:
	@poetry run alembic upgrade head

# 마이그레이션 롤백
migrate-down:
	@poetry run alembic downgrade base