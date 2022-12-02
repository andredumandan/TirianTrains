SET DATESTYLE TO DMY;

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