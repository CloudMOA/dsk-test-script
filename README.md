# dsk-test-script

```
docker run --name db-execute-query -d \
  -e PG_DB_HOST=10.10.43.100 \
  -e PG_DB_PORT=31301 \
  -e PG_DB_NAME=tpcc \
  -e PG_DB_USER=root \
  -e PG_DB_PASSWD=root \
  -e PG_SLEEP=60 \
  -e MARIA_DB_HOST=10.10.43.100 \
  -e MARIA_DB_PORT=31302 \
  -e MARIA_DB_NAME=tpcc \
  -e MARIA_DB_USER=root \
  -e MARIA_DB_PASSWD=root \
  -e MARIA_SLEEP=60 \
  -e MYSQL_DB_HOST=10.10.43.100 \
  -e MYSQL_DB_PORT=31303 \
  -e MYSQL_DB_NAME=tpcc \
  -e MYSQL_DB_USER=root \
  -e MYSQL_DB_PASSWD=root \
  -e MYSQL_SLEEP=60 \
  nexus2.exem-oss.org/saas/dsk-test-script:db-execute-query
```

