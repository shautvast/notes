--- query foreign keys on all tables (local/remote) matching a pattern
SELECT 
	OBJECT_NAME(f.parent_object_id) as tablename,
	OBJECT_NAME(f.referenced_object_id) as remote_tablename
FROM sys.foreign_keys as f
WHERE OBJECT_NAME(f.referenced_object_id) not like 'SWE_%'
AND OBJECT_NAME(f.parent_object_id) like 'SWE_%'
order by tablename;
