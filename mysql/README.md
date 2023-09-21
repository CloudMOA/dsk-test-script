# Mysql 부하기 (HammerDB)

```
docker run --name db-load-mysql -d \
  -e DB_HOST=10.10.43.100 \
  -e DB_PORT=31301 \
  -e DB_NAME=tpcc \
  -e DB_USER=root \
  -e DB_PASSWD=root \
  -e SLEEP=60 \
  nexus2.exem-oss.org/saas/dsk-test-script:db-load-mysql
```