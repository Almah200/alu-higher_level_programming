-- script to list all cities of carlifonia
SELECT name, cities.id
FROM states
WHERE name = california
ORDER BY cities.id ASC;
