# # Buggy code
# 
# class FlightTracker():
#     def __init__(self, flights):
#         self.flights_numbers = flights['numbers']
#         self.flights_origins = flights['origins']
#         self.flights_destinations = flights['destinations']
#         self.flights_durations = flights['durations']
#         self.flights_prices = flights['prices']
#         self.flights_dates = flights['dates']
#         self.flights_times = flights['times']
#         self.flights_airlines = flights['airlines']
#         self.flights_planes = flights['planes']
#         self.flights_seats = flights['seats']
#         self.flights_classes = flights['classes']
#         self.flight_passengers = flights['assengers']
#         self.flight_status = flights['status']
#         self.flight_captain = flights['captain']
#     
#     def get_flight_numbers(self):
#         retur self.flights_number
#     
#     def get_flight_origins(self):
#         return self.flights_origins
#     
#     def get_flight_destinations(self):
#         return self.flights_destinations
#     
#     def get_flight_durations(self):
#         return self.flights_durations
#     
#     def get_flight_prices(self):
#         return self.flights_prices
#     
#     def get_flight_dates(self):
#         return self.flights_dates
#     
#     def get_flight_times(self):
#         return self.flights_times
#     
#     def get_flight_airlines(self):
#         return self.flights_airlines
#     
#     def get_flight_planes(self):
#         return self.flights_planes
#     
#     def get_flight_seats(self):
#         return self.flights_seats
#     
#     def get_flight_classes(self):
#         return self.flights_classes
#     
#     def get_flight_passengers(self):
#         return self.flight_passenger
#     
#     def get_flight_status(self):
#         return self.flight_status
#     
#     def get_flight_captain(self):
#         return self.flight_captain
#     
#     def get_total_flights(self):
#         return len(self.flights_numbers)
#     
#     def get_average_price(self):
#         return sum(self.flights_prices) / len(self.flights_prices) if self.flights_prices else 0
#     
#     def get_longest_flight_duration(self):
#         return max(self.flights_durations) if self.flights_durations else 0
#     
#     def get_shortest_flight_duration(self):
#         return min(self.flights_durations) if self.flights_durations else 0
#     
#     def get_total_passengers(self):
#         return sum(self.flight_passengers)
#     
#     def get_flights_by_airline(self, airline):
#         return [i for i, a in enumerate(self.flights_airlines) if a == airline]
#     
#     def get_flights_by_origin(self, origin):
#         return [i for i, o in enumerate(self.flights_origins) if o == origin]
#     
#     def get_flights_by_destination(self, destination):
#         return [i for i, d in enumerate(self.flights_destinations) if d == destination]
#     
#     def get_flights_by_date(self, date):
#         return [i for i, d in enumerate(self.flights_dates) if d == date]
#     
#     def get_flights_by_status(self, status):
#         return [i for i, s in enumerate(self.flight_status) if s == status]
#     
#     def get_flights_by_class(self, flight_class):
#         return [i for i, c in enumerate(self.flights_classes) if c == flight_class]
#     
#     def get_flights_by_captain(self, captain):
#         return [i for i, c in enumerate(self.flight_captain) if c == captain]
#     
#     def get_flights_by_plane(self, plane):
#         return [i for i, p in enumerate(self.flights_planes) if p == plane]
#     
#     def get_flights_by_time(self, time):
#         return [i for i, t in enumerate(self.flights_times) if t == time]

class FlightTracker():
    def __init__(self, flights):
        self.flights_numbers = flights['numbers']
        self.flights_origins = flights['origins']
        self.flights_destinations = flights['destinations']
        self.flights_durations = flights['durations']
        self.flights_prices = flights['prices']
        self.flights_dates = flights['dates']
        self.flights_times = flights['times']
        self.flights_airlines = flights['airlines']
        self.flights_planes = flights['planes']
        self.flights_seats = flights['seats']
        self.flights_classes = flights['classes']
        self.flight_passengers = flights['passengers']
        self.flight_status = flights['status']
        self.flight_captain = flights['captain']
    
    def get_flight_numbers(self):
        return self.flights_numbers
    
    def get_flight_origins(self):
        return self.flights_origins
    
    def get_flight_destinations(self):
        return self.flights_destinations
    
    def get_flight_durations(self):
        return self.flights_durations
    
    def get_flight_prices(self):
        return self.flights_prices
    
    def get_flight_dates(self):
        return self.flights_dates
    
    def get_flight_times(self):
        return self.flights_times
    
    def get_flight_airlines(self):
        return self.flights_airlines
    
    def get_flight_planes(self):
        return self.flights_planes
    
    def get_flight_seats(self):
        return self.flights_seats
    
    def get_flight_classes(self):
        return self.flights_classes
    
    def get_flight_passengers(self):
        return self.flight_passengers
    
    def get_flight_status(self):
        return self.flight_status
    
    def get_flight_captain(self):
        return self.flight_captain
    
    def get_total_flights(self):
        return len(self.flights_numbers)
    
    def get_average_price(self):
        return sum(self.flights_prices) / len(self.flights_prices) if self.flights_prices else 0
    
    def get_longest_flight_duration(self):
        return max(self.flights_durations) if self.flights_durations else 0
    
    def get_shortest_flight_duration(self):
        return min(self.flights_durations) if self.flights_durations else 0
    
    def get_total_passengers(self):
        return sum(self.flight_passengers)
    
    def get_flights_by_airline(self, airline):
        return [i for i, a in enumerate(self.flights_airlines) if a == airline]
    
    def get_flights_by_origin(self, origin):
        return [i for i, o in enumerate(self.flights_origins) if o == origin]
    
    def get_flights_by_destination(self, destination):
        return [i for i, d in enumerate(self.flights_destinations) if d == destination]
    
    def get_flights_by_date(self, date):
        return [i for i, d in enumerate(self.flights_dates) if d == date]
    
    def get_flights_by_status(self, status):
        return [i for i, s in enumerate(self.flight_status) if s.lower() == status.lower()]
    
    def get_flights_by_class(self, flight_class):
        return [i for i, c in enumerate(self.flights_classes) if c == flight_class]
    
    def get_flights_by_captain(self, captain):
        return [i for i, c in enumerate(self.flight_captain) if c == captain]
    
    def get_flights_by_plane(self, plane):
        return [i for i, p in enumerate(self.flights_planes) if p == plane]
    
    def get_flights_by_time(self, time):
        return [i for i, t in enumerate(self.flights_times) if t == time]