
UPDATE performance_schema.setup_consumers SET ENABLED='YES' WHERE NAME LIKE 'statements_current';
SET GLOBAL innodb_undo_log_truncate=ON;
