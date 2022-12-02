SET DATESTYLE TO DMY;

-------------------------------------------------------
--                      STATIONS                     --
-------------------------------------------------------

INSERT INTO station
VALUES (
    1001,
    'Allies'' Enclave',
    'local'
);

INSERT INTO station
VALUES (
    1002,
    'The Wardrobe',
    'local'
);

INSERT INTO station
VALUES (
    1003,
    'The Lamp Post',
    'local'
);

INSERT INTO station
VALUES (
    1004,
    'Beaver''s Dam',
    'local'
);

INSERT INTO station
VALUES (
    0001,
    'Mr. Tumms',
    'inter-town'
);

INSERT INTO station
VALUES (
    2001,
    'Aslan''s Clamp',
    'inter-town'
);

INSERT INTO station
VALUES (
    3001,
    'Cauldron Pool',
    'inter-town'
);

INSERT INTO station
VALUES (
    4001,
    'Cherry Tree',
    'inter-town'
);

INSERT INTO station
VALUES (
    5001,
    'Father Christmas',
    'inter-town'
);

INSERT INTO station
VALUES (
    6001,
    'Dancing Lawn',
    'inter-town'
);

INSERT INTO station
VALUES (
    7001,
    'Anvard',
    'inter-town'
);

INSERT INTO station
VALUES (
    8001,
    'The Stone Table',
    'inter-town'
);

INSERT INTO station
VALUES (
    9001,
    'Witch''s Camp',
    'inter-town'
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

-------------------------------------------------------
--                       ROUTES                      --
-------------------------------------------------------

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

-------------------------------------------------------
--                       TRAINS                      --
-------------------------------------------------------

INSERT INTO train
VALUES
    (451621, 'S', 333, 120, 70, 7, True, False, True, True, True, False),
    (238951, 'S', 333, 120, 70, 7, True, False, True, True, True, False),
    (824895, 'S', 555, 200, 150, 10, True, True, True, True, True, True),
    (16176, 'A', 420, 150, 100, 7, True, False, True, True, True, False),
    (24852, 'A', 420, 150, 100, 7, True, False, True, True, True, False),
    (53157, 'A', 333, 150, 100, 7, True, False, False, False, False, False),
    (61835, 'A', 333, 150, 100, 7, True, False, False, False, False, False),
    (23813, 'A', 555, 150, 100, 7, True, False, False, False, False, False),
    (25901, 'A', 555, 150, 100, 7, True, False, False, False, False, False); 

-------------------------------------------------------
--                     MAINTENANCE                   --
-------------------------------------------------------

INSERT INTO maintenance_certificate
VALUES (
    nextval('maintenance_certificate_certificate_no_seq'),
    451621
);

INSERT INTO maintenance_certificate
VALUES (
    nextval('maintenance_certificate_certificate_no_seq'),
    238951
);

INSERT INTO maintenance_certificate
VALUES (
    nextval('maintenance_certificate_certificate_no_seq'),
    824895
);

INSERT INTO maintenance_certificate
VALUES (
    nextval('maintenance_certificate_certificate_no_seq'),
    16176
);

INSERT INTO maintenance_certificate
VALUES (
    nextval('maintenance_certificate_certificate_no_seq'),
    24852
);

INSERT INTO maintenance_certificate
VALUES (
    nextval('maintenance_certificate_certificate_no_seq'),
    53157
);

INSERT INTO maintenance_certificate
VALUES (
    nextval('maintenance_certificate_certificate_no_seq'),
    61835
);

INSERT INTO maintenance_certificate
VALUES (
    nextval('maintenance_certificate_certificate_no_seq'),
    23813
);

INSERT INTO maintenance_certificate
VALUES (
    nextval('maintenance_certificate_certificate_no_seq'),
    25901
);

-------------------------------------------------------
--                        CREW                       --
-------------------------------------------------------

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

INSERT INTO maintenance_crew
VALUES (
    nextval('maintenance_crew_crew_no_seq'),
    'Chic',
    'Haron'
);

INSERT INTO maintenance_crew
VALUES (
    nextval('maintenance_crew_crew_no_seq'),
    'Longg',
    'Anisa'
);

INSERT INTO maintenance_crew
VALUES (
    nextval('maintenance_crew_crew_no_seq'),
    'Sini',
    'Gang'
);

INSERT INTO maintenance_crew
VALUES (
    nextval('maintenance_crew_crew_no_seq'),
    'Beta',
    'Max'
);

INSERT INTO maintenance_crew
VALUES (
    nextval('maintenance_crew_crew_no_seq'),
    'Lech',
    'On'
);

INSERT INTO maintenance_crew
VALUES (
    nextval('maintenance_crew_crew_no_seq'),
    'Tap',
    'Silog'
);

INSERT INTO maintenance_crew
VALUES (
    nextval('maintenance_crew_crew_no_seq'),
    'Toc',
    'Ino'
);

INSERT INTO maintenance_crew
VALUES (
    nextval('maintenance_crew_crew_no_seq'),
    'Kwek',
    'Kwek'
);

INSERT INTO maintenance_crew
VALUES (
    nextval('maintenance_crew_crew_no_seq'),
    'Ban',
    'Gus'
);

-------------------------------------------------------
--                  CREW CERTIFICATE                 --
-------------------------------------------------------

INSERT INTO crew_certificate
VALUES (
nextval('crew_certificate_crew_cert_id_seq'),
1,
1,
'08/01/2016',
'Excellent',
'Cleaning'
);

INSERT INTO crew_certificate
VALUES (
    nextval('crew_certificate_crew_cert_id_seq'),
    2,
    1,
    '09/01/2016',
    'Very Good',
    'Replacement of brake discs'
);

INSERT INTO crew_certificate
VALUES (
    nextval('crew_certificate_crew_cert_id_seq'),
    3,
    1,
    '10/01/2016',
    'Excellent',
    'Complete oil change'
);

INSERT INTO crew_certificate
VALUES (
    nextval('crew_certificate_crew_cert_id_seq'),
    2,
    2,
    '10/10/2016',
    'Okay',
    'Cleaning'
);

INSERT INTO crew_certificate
VALUES (
    nextval('crew_certificate_crew_cert_id_seq'),
    5,
    2,
    '09/10/2016',
    'Good',
    'Toilet repair'
);

INSERT INTO crew_certificate
VALUES (
    nextval('crew_certificate_crew_cert_id_seq'),
    9,
    2,
    '09/02/2015',
    'Very Good',
    'Axle check-up'
);

INSERT INTO crew_certificate
VALUES (
    nextval('crew_certificate_crew_cert_id_seq'),
    4,
    3,
    '23/02/2013',
    'Okay',
    'Cleaning'
);

INSERT INTO crew_certificate
VALUES (
    nextval('crew_certificate_crew_cert_id_seq'),
    12,
    3,
    '09/10/2014',
    'Good',
    'Toilet repair'
);

INSERT INTO crew_certificate
VALUES (
    nextval('crew_certificate_crew_cert_id_seq'),
    11,
    3,
    '09/02/2015',
    'Bad',
    'Replacement of brake discs'
);

INSERT INTO crew_certificate
VALUES (
    nextval('crew_certificate_crew_cert_id_seq'),
    10,
    3,
    '13/02/2016',
    'Bad',
    'Door repair'
);

INSERT INTO crew_certificate
VALUES (
    nextval('crew_certificate_crew_cert_id_seq'),
    1,
    4,
    '23/02/2013',
    'Okay',
    'Seat repair'
);

INSERT INTO crew_certificate
VALUES (
    nextval('crew_certificate_crew_cert_id_seq'),
    4,
    4,
    '09/10/2016',
    'Good',
    'Cleaning'
);

INSERT INTO crew_certificate
VALUES (
    nextval('crew_certificate_crew_cert_id_seq'),
    2,
    4,
    '09/02/2014',
    'Bad',
    'PA system repair'
);

INSERT INTO crew_certificate
VALUES (
    nextval('crew_certificate_crew_cert_id_seq'),
    1,
    5,
    '02/06/2015',
    'Very Bad',
    'Cleaning'
);

INSERT INTO crew_certificate
VALUES (
    nextval('crew_certificate_crew_cert_id_seq'),
    4,
    5,
    '19/11/2014',
    'Good',
    'Cleaning'
);

INSERT INTO crew_certificate
VALUES (
    nextval('crew_certificate_crew_cert_id_seq'),
    2,
    6,
    '09/02/2014',
    'Bad',
    'Cleaning'
);

INSERT INTO crew_certificate
VALUES (
    nextval('crew_certificate_crew_cert_id_seq'),
    2,
    7,
    '25/12/2016',
    'Very Good',
    'Axle check-up'
);

INSERT INTO crew_certificate
VALUES (
    nextval('crew_certificate_crew_cert_id_seq'),
    6,
    7,
    '23/11/2015',
    'Very Bad',
    'Exhaust repair'
);

INSERT INTO crew_certificate
VALUES (
    nextval('crew_certificate_crew_cert_id_seq'),
    8,
    7,
    '23/09/2016',
    'Excellent',
    'Cleaning'
);

INSERT INTO crew_certificate
VALUES (
    nextval('crew_certificate_crew_cert_id_seq'),
    7,
    8,
    '23/09/2016',
    'Excellent',
    'Cleaning'
);

INSERT INTO crew_certificate
VALUES (
    nextval('crew_certificate_crew_cert_id_seq'),
    8,
    8,
    '25/12/2015',
    'Very Good',
    'Brake check-up'
);

INSERT INTO crew_certificate
VALUES (
    nextval('crew_certificate_crew_cert_id_seq'),
    9,
    8,
    '23/11/2013',
    'Very Bad',
    'Door check-up'
);

INSERT INTO crew_certificate
VALUES (
    nextval('crew_certificate_crew_cert_id_seq'),
    10,
    8,
    '23/09/2014',
    'Excellent',
    'Cleaning'
);

INSERT INTO crew_certificate
VALUES (
    nextval('crew_certificate_crew_cert_id_seq'),
    12,
    9,
    '23/09/2016',
    'Excellent',
    'Cleaning'
);

-------------------------------------------------------
--                       TRIPS                       --
-------------------------------------------------------

INSERT INTO trip_date
VALUES 
    ('11/12/2016'),
    ('12/12/2016'),
    ('13/12/2016'),
    ('14/12/2016'),
    ('15/12/2016');

INSERT INTO trip
VALUES
    (1, 16176, '11/12/2016', '09:41:00', 'inter-town'),
    (2, 53157, '11/12/2016', '12:48:00', 'inter-town'),
    (3, 23813, '11/12/2016', '01:55:00', 'inter-town'),
    (4, 61835, '11/12/2016', '02:30:00', 'inter-town'),
    (5, 23813, '12/12/2016', '09:41:00', 'inter-town'),
    (6, 16176, '12/12/2016', '12:44:00', 'inter-town'),
    (7, 23813, '12/12/2016', '02:55:00', 'inter-town'),
    (8, 61835, '12/12/2016', '03:30:00', 'inter-town'),
    (9, 23813, '12/12/2016', '09:41:00', 'inter-town'),
    (10, 16176, '13/12/2016', '12:44:00', 'inter-town'),
    (11, 24852, '13/12/2016', '02:55:00', 'inter-town'),
    (12, 53157, '13/12/2016', '03:30:00', 'inter-town'),
    (13, 61835, '14/12/2016', '09:41:00', 'inter-town'),
    (14, 16176, '14/12/2016', '12:44:00', 'inter-town'),
    (15, 25901, '14/12/2016', '01:55:00', 'inter-town'),
    (16, 53157, '14/12/2016', '12:30:00', 'inter-town'),
    (17, 61835, '15/12/2016', '09:41:00', 'inter-town'),
    (18, 16176, '15/12/2016', '03:44:00', 'inter-town'),
    (19, 25901, '15/12/2016', '04:55:00', 'inter-town'),
    (20, 53157, '15/12/2016', '05:30:00', 'inter-town'),

    (21, 451621, '11/12/2016', '12:48:00', 'local'),
    (22, 238951, '11/12/2016', '13:11:00', 'local'),
    (23, 238951, '11/12/2016', '14:48:00', 'local'),
    (24, 451621, '11/12/2016', '15:52:00', 'local'),
    (25, 451621, '12/12/2016', '11:48:00', 'local'),
    (26, 238951, '12/12/2016', '12:33:00', 'local'),
    (27, 824895, '12/12/2016', '17:48:00', 'local'),
    (28, 824895, '12/12/2016', '16:44:00', 'local'),
    (29, 451621, '13/12/2016', '01:48:00', 'local'),
    (30, 238951, '13/12/2016', '02:22:00', 'local'),
    (31, 238951, '13/12/2016', '07:48:00', 'local'),
    (32, 824895, '13/12/2016', '06:55:00', 'local'),
    (33, 451621, '14/12/2016', '21:48:00', 'local'),
    (34, 238951, '14/12/2016', '22:22:00', 'local'),
    (35, 824895, '14/12/2016', '17:48:00', 'local'),
    (36, 824895, '14/12/2016', '16:55:00', 'local'),
    (37, 451621, '15/12/2016', '16:48:00', 'local'),
    (38, 238951, '15/12/2016', '22:22:00', 'local'),
    (39, 824895, '15/12/2016', '04:48:00', 'local'),
    (40, 824895, '15/12/2016', '02:55:00', 'local');

INSERT INTO inter_town_trip
VALUES
    (1, 1),
    (2, 2),
    (3, 3),
    (4, 4),
    (5, 5),
    (6, 6),
    (7, 7),
    (8, 8),
    (9, 9),
    (10, 10),
    (11, 11),
    (12, 12),
    (13, 13),
    (14, 14),
    (15, 15),
    (16, 16),
    (17, 17),
    (18, 18),
    (19, 19),
    (20, 20);

INSERT INTO local_trip
VALUES
    (21, 1001),
    (22, 1002),
    (23, 1003),
    (24, 1004),
    (25, 1001),
    (26, 1002),
    (27, 1003),
    (28, 1004),
    (29, 1001),
    (30, 1002),
    (31, 1003),
    (32, 1004),
    (33, 1001),
    (34, 1002),
    (35, 1003),
    (36, 1004),
    (37, 1001),
    (38, 1002),
    (39, 1003),
    (40, 1004);
