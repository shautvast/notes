--- query foreign keys on all tables (local/remote) matching a pattern

```SQL
SELECT OBJECT_NAME(f.parent_object_id) as tablename,
	COL_NAME(fc.parent_object_id, fc.parent_column_id),
	f.name as fk_name,
	OBJECT_NAME(f.referenced_object_id) as remote_tablename,
	COL_NAME(fc.referenced_object_id, fc.referenced_column_id)
FROM sys.foreign_keys as f
INNER JOIN sys.foreign_key_columns as fc
ON	f.object_id = fc.constraint_object_id 
WHERE OBJECT_NAME(f.referenced_object_id) not like 'SWE_%'
AND OBJECT_NAME(f.parent_object_id) like 'SWE_%'
order by tablename;
```
