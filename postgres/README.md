# pg 부하기 (HammerDB)

## Sample
```
sudo docker run --name db-create-pg -d --rm \
  -e DB_HOST=10.10.43.105 \
  -e DB_PORT=31302 \
  -e DB_NAME=tpcc \
  -e DB_USER=root \
  -e DB_PASSWD=root \
  -e DB_POSTGRES_PASSWD=postgres \
  -e ACTION=create \
  nexus2.exem-oss.org/saas/dsk-test-script:db-load-pg

sudo docker run --name db-run-pg -d \
  -e DB_HOST=10.10.43.105 \
  -e DB_PORT=31302 \
  -e DB_NAME=tpcc \
  -e DB_USER=root \
  -e DB_PASSWD=root \
  -e DB_POSTGRES_PASSWD=postgres \
  -e EXE_MINUTES=5 \
  -e SLEEP_SECONDS=60 \
  -e ACTION=run \
  nexus2.exem-oss.org/saas/dsk-test-script:db-load-pg

sudo docker run --name db-delete-pg -d --rm \
  -e DB_HOST=10.10.43.105 \
  -e DB_PORT=31302 \
  -e DB_NAME=tpcc \
  -e DB_USER=root \
  -e DB_PASSWD=root \
  -e DB_POSTGRES_PASSWD=postgres \
  -e ACTION=delete \
  nexus2.exem-oss.org/saas/dsk-test-script:db-load-pg
```

## 환경변수
- DB_HOST : DB 호스트
- DB_PORT : DB 포트
- DB_NAME : DB 이름
- DB_USER : DB 사용자
- DB_PASSWD : DB 비밀번호
- EXE_MINUTES : 실행 시간 (분)
- SLEEP_SECONDS : 실행 후 대기 시간 (초)
- ACTION : create, run, delete