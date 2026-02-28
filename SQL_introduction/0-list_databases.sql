-- Lists all databases of the MySQL server sorted alphabetically
SELECT schema_name
FROM information_schema.schemata
ORDER BY schema_name;
