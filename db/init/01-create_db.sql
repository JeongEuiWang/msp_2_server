-- 데이터베이스가 없으면 생성
CREATE DATABASE IF NOT EXISTS msp_db;

-- 권한 설정
GRANT ALL PRIVILEGES ON msp_db.* TO 'root'@'%';
FLUSH PRIVILEGES;