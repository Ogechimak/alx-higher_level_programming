-- a script that lists all records of the table
-- update score using name col
SELECT score, name FROM second_table
WHERE name != 'NULL'
ORDER BY score DESC;
