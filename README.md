# dsk-test-script

```
docker run --name postgres-slow-query -d \
  -e DB_HOST=10.10.43.100 \
  -e DB_PORT=32233 \
  -e DB_NAME=manager \
  -e DB_USER=postgres \
  -e DB_PASSWD=root \
  nexus2.exem-oss.org/saas/dsk-test-script:postgres-slow-query
```

