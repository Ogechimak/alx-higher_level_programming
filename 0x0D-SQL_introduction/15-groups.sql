-- a script that lists the number of records
-- update score using name col
SELECT score, COUNT(*) AS number
FROM second_table
GROUP BY score
ORDER BY number DESC;
