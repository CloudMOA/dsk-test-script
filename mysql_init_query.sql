
UPDATE performance_schema.setup_consumers SET ENABLED='YES' WHERE NAME LIKE 'statements_current';
ALTER USER 'root' IDENTIFIED WITH mysql_native_password BY 'root';
SET GLOBAL innodb_undo_log_truncate=ON;
