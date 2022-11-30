DROP DATABASE IF EXISTS tirian_trains;

CREATE DATABASE tirian_trains;

\c tirian_trains

CREATE TABLE train(
    train_id SERIAL NOT NULL UNIQUE PRIMARY KEY, 
    series VARCHAR(1) NOT NULL DEFAULT 0,
    model_number INT NOT NULL DEFAULT 0,
    max_speed FLOAT NOT NULL DEFAULT 0,
    seats INT NOT NULL DEFAULT 0,
    toilets INT NOT NULL DEFAULT 0,
    reclining_seats BOOLEAN NOT NULL DEFAULT FALSE,
    luggage_storage BOOLEAN NOT NULL DEFAULT FALSE,
    folding_tables BOOLEAN NOT NULL DEFAULT FALSE,
    vending_machines BOOLEAN NOT NULL DEFAULT FALSE,
    disability_access BOOLEAN NOT NULL DEFAULT FALSE,
    food_services BOOLEAN NOT NULL DEFAULT FALSE
);

CREATE TABLE maintenance_crew(
    crew_no SERIAL NOT NULL UNIQUE PRIMARY KEY,
    last_name VARCHAR(255) NOT NULL,
    given_name VARCHAR(255) NOT NULL
);

CREATE TABLE maintenance_certificate(
    certificate_no SERIAL NOT NULL UNIQUE PRIMARY KEY,
    train_id INT NOT NULL,
    FOREIGN KEY (train_id) REFERENCES train(train_id) ON DELETE CASCADE 
);

CREATE TABLE crew_certificate(
    crew_cert_id SERIAL PRIMARY KEY NOT NULL,
    crew_no INT NOT NULL,
    certificate_no INT NOT NULL,
    maintenance_date DATE NOT NULL DEFAULT '01/01/2000',
    condition VARCHAR(255) NOT NULL DEFAULT 'Okay',
    task VARCHAR(255) NOT NULL DEFAULT 'Cleaning',
    FOREIGN KEY (crew_no) REFERENCES maintenance_crew(crew_no),
    FOREIGN KEY (certificate_no) REFERENCES maintenance_certificate(certificate_no)
);

--https://www.postgresql.org/docs/current/datatype-enum.html
CREATE TYPE GENDER AS ENUM('Male','Female','Other');

CREATE TABLE customer(
    customer_id SERIAL NOT NULL UNIQUE PRIMARY KEY,
    last_name VARCHAR(255) NOT NULL DEFAULT '',
    given_name VARCHAR(255) NOT NULL DEFAULT '',
    middle_initial VARCHAR(255),
    birth_date DATE NOT NULL DEFAULT '01/01/2000',
    current_gender GENDER NOT NULL DEFAULT 'Male'
);

CREATE TABLE ticket(
    ticket_id SERIAL NOT NULL UNIQUE PRIMARY KEY,
    customer_id INT NOT NULL,
    date_purchased DATE NOT NULL DEFAULT '01/01/2000',
    FOREIGN KEY (customer_id) REFERENCES customer(customer_id) ON DELETE CASCADE 
);

CREATE TABLE station(
    station_id SERIAL NOT NULL UNIQUE PRIMARY KEY,
    station_name VARCHAR(255) NOT NULL DEFAULT 'Tirian Trains Station', 
    type VARCHAR(255) NOT NULL
);

CREATE TABLE local_station(
    station_id SERIAL NOT NULL UNIQUE PRIMARY KEY,
    destination_id INT,
    trip_cost FLOAT NOT NULL,
    FOREIGN KEY (destination_id) REFERENCES local_station(station_id) ON DELETE CASCADE
);

CREATE TABLE town_station(
    station_id SERIAL NOT NULL UNIQUE PRIMARY KEY
);

CREATE TABLE inter_town_route(
    route_id SERIAL NOT NULL PRIMARY KEY,
    origin_id INT NOT NULL,
    destination_id INT NOT NULL,
    travel_time FLOAT DEFAULT 5,
    trip_cost INT NOT NULL DEFAULT 0,
    FOREIGN KEY (origin_id) REFERENCES town_station(station_id) ON DELETE CASCADE,
    FOREIGN KEY (destination_id) REFERENCES town_station(station_id) ON DELETE CASCADE
);

CREATE TABLE trip_date(
    date DATE NOT NULL PRIMARY KEY
);

CREATE TABLE trip(
    trip_id SERIAL NOT NULL UNIQUE PRIMARY KEY,
    train_id INT NOT NULL,
    trip_date DATE NOT NULL DEFAULT '01/01/2000',
    departure_time TIME NOT NULL DEFAULT '00:00:00',
    type VARCHAR(255) NOT NULL,
    FOREIGN KEY (train_id) REFERENCES train(train_id) ON DELETE CASCADE,
    FOREIGN KEY (trip_date) REFERENCES trip_date(date) ON DELETE CASCADE,
    CHECK (type in ('local', 'inter-town'))
);

CREATE TABLE local_trip(
    trip_id SERIAL NOT NULL UNIQUE PRIMARY KEY,
    station_id INT NOT NULL,
    FOREIGN KEY (station_id) REFERENCES local_station(station_id)
);
CREATE TABLE inter_town_trip(
    trip_id SERIAL NOT NULL UNIQUE PRIMARY KEY,
    route_id INT NOT NULL,
    FOREIGN KEY (route_id) REFERENCES inter_town_route(route_id)
);

CREATE TABLE ticket_trip(
    ticket_trip_id SERIAL NOT NULL UNIQUE PRIMARY KEY,
    trip_id INT NOT NULL,
    ticket_id INT NOT NULL,
    FOREIGN KEY (trip_id) REFERENCES trip(trip_id) ON DELETE CASCADE,
    FOREIGN KEY (ticket_id) REFERENCES ticket(ticket_id) ON DELETE CASCADE 
);