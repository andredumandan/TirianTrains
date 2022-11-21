CREATE DATABASE tiriantrains

CREATE TABLE maintenance_crew{
    crew_no SERIAL PRIMARY KEY INT NOT NULL
};

CREATE TABLE train{
    train_id SERIAL NOT NULL UNIQUE PRIMARY KEY, 
    series INT NOT NULL DEFAULT 0,
    model_number INT NOT NULL DEFAULT 0,
    max_speed INT NOT NULL DEFAULT 0,
    seats INT NOT NULL 0,
    reclining_seats? BOOLEAN NOT NULL DEFAULT FALSE,
    luggage_storage? BOOLEAN NOT NULL DEFAULT FALSE,
    folding_tables? BOOLEAN NOT NULL DEFAULT FALSE,
    vending_machines? BOOLEAN NOT NULL DEFAULT FALSE,
    disability_access? BOOLEAN NOT NULL DEFAULT FALSE,
    food_services? BOOLEAN NOT NULL DEFAULT FALSE
};

CREATE TABLE maintenance_certificate{
    certificate_no SERIAL NOT NULL UNIQUE PRIMARY KEY,
    crew_no INT NOT NULL,
    train_id INT NOT NULL,
    maintenance_date DATE NOT NULL DEFAULT '01/01/2000',
    condition VARCHAR(255) NOT NULL DEFAULT 'Okay',
    FOREIGN KEY (crew_no) REFERENCES maintenance_crew(crew_no) ON DELETE RESTRICT,
    FOREIGN KEY (train_id) REFERENCES train(train_id) ON DELETE RESTRICT 
};

CREATE TABLE task{
    certificate_no INT NOT NULL,
    task VARCHAR(255) NOT NULL DEFAULT 'Cleaning',
    FOREIGN KEY (certificate_no) REFERENCES maintenance_certificate(certificate_no) ON DELETE RESTRICT 
};

--https://www.postgresql.org/docs/current/datatype-enum.html
CREATE TYPE GENDER AS ENUM('Male','Female','Other');

CREATE TABLE passenger{
    customer_id SERIAL NOT NULL UNIQUE PRIMARY KEY,
    last_name VARCHAR(255) NOT NULL DEFAULT '',
    given_name VARCHAR(255) NOT NULL DEFAULT '',
    middle_initial VARCHAR(255),
    birth_date DATE NOT NULL DEFAULT '01/01/2000',
    current_gender GENDER NOT NULL DEFAULT 'Male'
};

CREATE TABLE ticket{
    ticket_id SERIAL NOT NULL UNIQUE PRIMARY KEY,
    customer_id INT NOT NULL,
    date_purchased DATE NOT NULL DEFAULT '01/01/2000',
    FOREIGN KEY (customer_id) REFERENCES passenger(customer_id) ON DELETE RESTRICT 
}

/*CREATE TABLE itinerary{
    ticket_id INT NOT NULL,
    
}*/

CREATE TABLE station{
    station_id SERIAL NOT NULL UNIQUE PRIMARY KEY,
    station_name VARCHAR(255) NOT NULL DEFAULT 'Tirian Trains Station'   
}

CREATE TABLE local_station{

}

CREATE TABLE town_station{

}

CREATE TABLE inter-town_route{
    departure_station_id INT NOT NULL,
    arrival_station_id INT NOT NULL,
    travel_time FLOAT DEFAULT 5,
    trip_cost INT NOT NULL DEFAULT 0,
    FOREIGN KEY (train_id) REFERENCES train(train_id) ON DELETE RESTRICT
}

CREATE TABLE trip{
    trip_id SERIAL NOT NULL UNIQUE PRIMARY KEY,
    train_id INT NOT NULL,
    departure_station_id INT NOT NULL,
    arrival_station_id INT NOT NULL,
    trip_date DATE NOT NULL DEFAULT '01/01/2000',
    departure_time TIME NOT NULL DEFAULT '00:00:00',
    arrival_time TIME NOT NULL DEFAULT '00:00:00',
    FOREIGN KEY (train_id) REFERENCES train(train_id) ON DELETE RESTRICT
}

CREATE TABLE ticket_trip{
    ticket_trip_id SERIAL NOT NULL UNIQUE PRIMARY KEY,
    trip_id INT NOT NULL,
    ticket_id INT NOT NULL,
    FOREIGN KEY (trip_id) REFERENCES trip(trip_id) ON DELETE RESTRICT,
    FOREIGN KEY (ticket_id) REFERENCES ticket(ticket_trip) ON DELETE RESTRICT 
}
