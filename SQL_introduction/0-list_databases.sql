-- Lists all databases of the MySQL server sorted alphabetically
SELECT schema_name AS `Database`
FROM information_schema.schemata
ORDER BY schema_name;
