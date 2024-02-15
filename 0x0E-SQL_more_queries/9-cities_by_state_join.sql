-- a script that lists all cities contained in the database
SELECT cities.id, cities.name, states.name
FROM cities AS c
ON INNER JOIN hbtn_0d_usa.states AS s
WHERE c.id = s.id
ORDER BY c.id ASCE;
