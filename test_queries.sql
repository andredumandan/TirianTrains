-- TRAINS VIEW
SELECT train_id AS "TRAIN ID", CONCAT(series,'-', model_number) AS "MODEL"
FROM train;

-- TRAIN MAINTENANCE VIEW

-- TRAIN MAINTENANCE HISTORY VIEW
SELECT cert.maintenance_date AS "DATE", CONCAT(crew.last_name,' ', crew.given_name) AS "CREW IN CHARGE", cert.task AS "TASKS",cert.condition AS "CONDITION"
FROM crew_certificate cert, maintenance_crew crew, maintenance_certificate mc
WHERE cert.crew_no=crew.crew_no
AND cert.certificate_no=mc.certificate_no
ORDER BY cert.maintenance_date;

-- TRAIN ROUTES VIEW
SELECT

-- TRIP SCHEDULE VIEW
SELECT trip_date AS "DATE", COUNT(trip_id) AS "NO. OF TRIPS"
FROM trip
GROUP BY trip_date;

-- TRIPS VIEW

-- TICKETS VIEW

-- TRIP ITENIRARY VIEW

-- CUSTOMERS VIEW
SELECT CONCAT(last_name, ' ', given_name) AS "NAME", birth_date AS "BIRTH DATE"
FROM customer;

-- TRAVEL HISTORY VIEW