--STATIONS AND ROUTES
INSERT INTO station
VALUES (
    1001,
    'Allies'' Enclave'
);

INSERT INTO station
VALUES (
    1002,
    'The Wardrobe'
);

INSERT INTO station
VALUES (
    1003,
    'The Lamp Post'
);

INSERT INTO station
VALUES (
    1004,
    'Beaver''s Dam'
);

INSERT INTO local_station
VALUES (
    1001,
    NULL,
    2
);

INSERT INTO local_station
VALUES (
    1004,
    1001,
    2
);

INSERT INTO local_station
VALUES (
    1003,
    1004,
    2
);

INSERT INTO local_station
VALUES (
    1002,
    1003,
    2
);

UPDATE local_station
SET destination_id = 1002
WHERE station_id = 1001;

INSERT INTO station
VALUES (
    0001,
    'Mr. Tumms'
);

INSERT INTO station
VALUES (
    2001,
    'Aslan''s Clamp'
);

INSERT INTO station
VALUES (
    3001,
    'Cauldron Pool'
);

INSERT INTO station
VALUES (
    4001,
    'Cherry Tree'
);

INSERT INTO station
VALUES (
    5001,
    'Father Christmas'
);

INSERT INTO station
VALUES (
    6001,
    'Dancing Lawn'
);

INSERT INTO station
VALUES (
    7001,
    'Anvard'
);

INSERT INTO station
VALUES (
    8001,
    'The Stone Table'
);

INSERT INTO station
VALUES (
    9001,
    'Witch''s Camp'
);

INSERT INTO town_station
VALUES (
    0001
);

INSERT INTO town_station
VALUES (
    1001
);

INSERT INTO town_station
VALUES (
    2001
);

INSERT INTO town_station
VALUES (
    3001
);

INSERT INTO town_station
VALUES (
    4001
);

INSERT INTO town_station
VALUES (
    5001
);

INSERT INTO town_station
VALUES (
    6001
);

INSERT INTO town_station
VALUES (
    7001
);

INSERT INTO town_station
VALUES (
    8001
);

INSERT INTO town_station
VALUES (
    9001
);

INSERT INTO inter_town_route
VALUES (
    nextval('inter_town_route_route_id_seq'),
    0001,
    1001,
    5,
    3
);
INSERT INTO inter_town_route
VALUES (
    nextval('inter_town_route_route_id_seq'),
    1001,
    0001,
    5,
    3
);

INSERT INTO inter_town_route
VALUES (
    nextval('inter_town_route_route_id_seq'),
    1001,
    2001,
    6,
    4
);

INSERT INTO inter_town_route
VALUES (
    nextval('inter_town_route_route_id_seq'),
    2001,
    1001,
    6,
    4
);

INSERT INTO inter_town_route
VALUES (
    nextval('inter_town_route_route_id_seq'),
    1001,
    3001,
    127,
    6
);

INSERT INTO inter_town_route
VALUES (
    nextval('inter_town_route_route_id_seq'),
    3001,
    1001,
    127,
    6
);

INSERT INTO inter_town_route
VALUES (
    nextval('inter_town_route_route_id_seq'),
    1001,
    6001,
    240,
    25
);

INSERT INTO inter_town_route
VALUES (
    nextval('inter_town_route_route_id_seq'),
    6001,
    1001,
    240,
    25
);

INSERT INTO inter_town_route
VALUES (
    nextval('inter_town_route_route_id_seq'),
    3001,
    4001,
    510,
    20
);

INSERT INTO inter_town_route
VALUES (
    nextval('inter_town_route_route_id_seq'),
    4001,
    3001,
    510,
    20
);

INSERT INTO inter_town_route
VALUES (
    nextval('inter_town_route_route_id_seq'),
    3001,
    5001,
    5,
    3
);

INSERT INTO inter_town_route
VALUES (
    nextval('inter_town_route_route_id_seq'),
    5001,
    3001,
    5,
    3
);

INSERT INTO inter_town_route
VALUES (
    nextval('inter_town_route_route_id_seq'),
    5001,
    4001,
    5,
    3
);

INSERT INTO inter_town_route
VALUES (
    nextval('inter_town_route_route_id_seq'),
    4001,
    5001,
    5,
    3
);

INSERT INTO inter_town_route
VALUES (
    nextval('inter_town_route_route_id_seq'),
    5001,
    9001,
    7,
    5
);

INSERT INTO inter_town_route
VALUES (
    nextval('inter_town_route_route_id_seq'),
    9001,
    5001,
    7,
    5
);

INSERT INTO inter_town_route
VALUES (
    nextval('inter_town_route_route_id_seq'),
    9001,
    8001,
    5,
    3
);

INSERT INTO inter_town_route
VALUES (
    nextval('inter_town_route_route_id_seq'),
    8001,
    9001,
    5,
    3
);

INSERT INTO inter_town_route
VALUES (
    nextval('inter_town_route_route_id_seq'),
    8001,
    6001,
    5,
    3
);

INSERT INTO inter_town_route
VALUES (
    nextval('inter_town_route_route_id_seq'),
    6001,
    8001,
    5,
    3
);

INSERT INTO inter_town_route
VALUES (
    nextval('inter_town_route_route_id_seq'),
    6001,
    7001,
    5,
    3
);

INSERT INTO inter_town_route
VALUES (
    nextval('inter_town_route_route_id_seq'),
    7001,
    6001,
    5,
    3
);

--TRAINS AND MAINTENANCE

INSERT INTO train
VALUES (
    451621, 
    'S', 
    393, 
    120, 
    70, 
    7, 
    True, 
    False, 
    True, 
    True, 
    True, 
    False
); 

INSERT INTO train
VALUES (
    16176, 
    'A', 
    420, 
    150, 
    100, 
    7, 
    True, 
    False, 
    True, 
    True, 
    True, 
    False
); 

INSERT INTO train
VALUES (
    53157, 
    'A', 
    420, 
    150, 
    100, 
    7, 
    True, 
    False, 
    False, 
    False, 
    False, 
    False
); 
INSERT INTO train
VALUES (
    23813, 
    'A', 
    420, 
    150, 
    100, 
    7, 
    True, 
    False, 
    False, 
    False, 
    False, 
    False
);

INSERT INTO maintenance_certificate
VALUES (
    nextval('maintenance_certificate_certificate_no_seq'),
    451621
);

INSERT INTO maintenance_crew
VALUES (
    nextval('maintenance_crew_crew_no_seq'),
    'Baho',
    'Ramoh'
);
INSERT INTO maintenance_crew
VALUES (
    nextval('maintenance_crew_crew_no_seq'),
    'Ngek',
    'Khitsu'
);
INSERT INTO maintenance_crew
VALUES (
    nextval('maintenance_crew_crew_no_seq'),
    'Char',
    'Itson'
);

INSERT INTO crew_certificate
VALUES (
    nextval('crew_certificate_crew_cert_id_seq'),
    1,
    1,
    '08/01/2016',
    'Excellent'
);

INSERT INTO task
VALUES (
    nextval('task_task_id_seq'),
    1,
    'Cleaning'
);

INSERT INTO crew_certificate
VALUES (
    nextval('crew_certificate_crew_cert_id_seq'),
    2,
    1,
    '09/01/2016',
    'Very Good'
);

INSERT INTO task
VALUES (
    nextval('task_task_id_seq'),
    1,
    'Replacement of brake discs'
);

INSERT INTO crew_certificate
VALUES (
    nextval('crew_certificate_crew_cert_id_seq'),
    3,
    1,
    '10/01/2016',
    'Excellent'
);

INSERT INTO task
VALUES (
    nextval('task_task_id_seq'),
    1,
    'Complete oil change'
);

--TRIPS

INSERT INTO trip
VALUES (
    1,
    16176,
    '12/11/2016',
    '09:41:00',
    'Inter-town'
);

INSERT INTO inter_town_trip
VALUES (
    1,
    5
);

INSERT INTO trip
VALUES (
    2,
    53157,
    '12/11/2016',
    '12:48:00',
    'Inter-town'
);

INSERT INTO inter_town_trip
VALUES (
    2,
    7
);

INSERT INTO trip
VALUES (
    3,
    23813,
    '12/11/2016',
    '12:48:00',
    'Inter-town'
);

INSERT INTO inter_town_trip
VALUES (
    3,
    9
);

--CUSTOMERS

INSERT INTO customer
VALUES (
    nextval('customer_customer_id_seq'),
    'Grove',
    'Adam',
    'K',
    '06/01/1972',
    'Male'
);

--TICKETS

INSERT INTO ticket
VALUES (
    nextval('ticket_ticket_id_seq'),
    1,
    '12/11/2016'
);

INSERT INTO ticket_trip
VALUES (
    nextval('ticket_trip_ticket_trip_id_seq'),
    1,
    1
);
INSERT INTO ticket_trip
VALUES (
    nextval('ticket_trip_ticket_trip_id_seq'),
    3,
    1
);