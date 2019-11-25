-- List records which has name, score descendent
SELECT score, name FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;
