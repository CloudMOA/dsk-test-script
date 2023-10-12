
UPDATE performance_schema.setup_consumers SET ENABLED='YES' WHERE NAME LIKE 'statements_current';
SET GLOBAL innodb_undo_log_truncate=ON;
SET GLOBAL max_connections=300;
SET GLOBAL wait_timeout=180;