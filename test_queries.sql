-- SELECT route.route_id, o_station.station_name, d_station.station_name 
-- FROM inter_town_route "route", station "o_station", station "d_station"
-- WHERE route.origin_id = o_station.station_id
-- AND route.destination_id = d_station.station_id;


-- SELECT trip.trip_id, trip.train_id, o_station.station_name, d_station.station_name, trip.departure_time, inter_town_route.travel_time, inter_town_route.trip_cost
-- FROM trip
-- LEFT JOIN inter_town_trip ON trip.trip_id = inter_town_trip.trip_id
-- INNER JOIN inter_town_route ON inter_town_trip.route_id = inter_town_route.route_id
-- JOIN station AS o_station ON o_station.station_id = inter_town_route.origin_id
-- JOIN station AS d_station ON d_station.station_id = inter_town_route.destination_id
-- WHERE trip.trip_date = '12/11/2016' ;


-- SELECT trip.trip_id, trip.train_id, o_station.station_name, d_station.station_name, trip.departure_time, inter_town_route.travel_time, inter_town_route.trip_cost
-- FROM trip
-- LEFT JOIN inter_town_trip ON trip.trip_id = inter_town_trip.trip_id
-- INNER JOIN inter_town_route ON inter_town_trip.route_id = inter_town_route.route_id
-- JOIN station AS o_station ON o_station.station_id = inter_town_route.origin_id
-- JOIN station AS d_station ON d_station.station_id = inter_town_route.destination_id
-- WHERE trip.trip_id IN (
--     SELECT ticket_trip.trip_id
--     FROM ticket_trip
--     JOIN ticket ON ticket.ticket_id = ticket_trip.ticket_id
--     WHERE ticket.ticket_id = 1
-- );