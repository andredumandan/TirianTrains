-- TRAINS VIEW
SELECT train_id AS "TRAIN ID", CONCAT(series,'-', model_number) AS "MODEL"
FROM train;

-- TRAIN MAINTENANCE VIEW
SELECT train_id AS "TRAIN ID", CONCAT(series, '-', model_number) AS "MODEL", max_speed AS "MAX SPEED (KPH)", seats AS "NO. OF SEATS", toilets AS "NO. OF TOILETS", reclining_seats AS "RECLINING SEATS", luggage_storage AS "LUGGAGE STORAGE", folding_tables AS "FOLDING TABLES", vending_machines AS "VENDING MACHINES", disability_access AS "DISABILITY ACCESS", food_services AS "FOOD SERVICES"
FROM train;

-- TRAIN MAINTENANCE HISTORY VIEW
SELECT cert.maintenance_date AS "DATE", CONCAT(crew.last_name,' ', crew.given_name) AS "CREW IN CHARGE", cert.task AS "TASKS",cert.condition AS "CONDITION"
FROM crew_certificate cert, maintenance_crew crew, maintenance_certificate mc
WHERE cert.crew_no=crew.crew_no
AND cert.certificate_no=mc.certificate_no
ORDER BY cert.maintenance_date;

-- TOWN STATIONS VIEW
SELECT station_name AS "STATION"
FROM station;

-- LOCAL ROUTES VIEW
SELECT origin.station_name AS "ORIGIN", destination.station_name AS "DESTINATION", 5 AS "DURATION", local_station.trip_cost AS "COST"
FROM local_station LEFT JOIN station origin
ON local_station.station_id = origin.station_id
LEFT JOIN station destination
ON local_station.destination_id = destination.station_id;

-- INTER-TOWN ROUTES VIEW
SELECT origin.station_name AS "ORIGIN", destination.station_name AS "DESTINATION", inter_town_route.travel_time AS "DURATION", inter_town_route.trip_cost AS "COST"
FROM inter_town_route LEFT JOIN station origin
ON inter_town_route.origin_id = origin.station_id
LEFT JOIN station destination
ON inter_town_route.destination_id = destination.station_id;

-- TRIP SCHEDULE VIEW
SELECT trip_date AS "DATE", COUNT(trip_id) AS "NO. OF TRIPS"
FROM trip
GROUP BY trip_date;

-- CUSTOMERS VIEW
SELECT CONCAT(last_name, ' ', given_name) AS "NAME", birth_date AS "BIRTH DATE"
FROM customer;
