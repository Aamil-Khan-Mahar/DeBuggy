# Correct Code

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
        return [i for i, s in enumerate(self.flight_status) if s == status]
    
    def get_flights_by_class(self, flight_class):
        return [i for i, c in enumerate(self.flights_classes) if c == flight_class]
    
    def get_flights_by_captain(self, captain):
        return [i for i, c in enumerate(self.flight_captain) if c == captain]
    
    def get_flights_by_plane(self, plane):
        return [i for i, p in enumerate(self.flights_planes) if p == plane]
    
    def get_flights_by_time(self, time):
        return [i for i, t in enumerate(self.flights_times) if t == time]
    
flights_data = {
    'numbers': [101, 102, 103],
    'origins': ['NYC', 'LAX', 'CHI'],
    'destinations': ['LON', 'PAR', 'BER'],
    'durations': [420, 540, 360],
    'prices': [500, 700, 600],
    'dates': ['2023-10-01', '2023-10-02', '2023-10-03'],
    'times': ['10:00', '12:00', '14:00'],
    'airlines': ['Delta', 'United', 'American'],
    'planes': ['Boeing 747', 'Airbus A320', 'Boeing 737'],
    'seats': [200, 180, 150],
    'classes': ['Economy', 'Business', 'First'],
    'passengers': [150, 160, 140],
    'status': ['On Time', 'Delayed', 'Cancelled'],
    'captain': ['John Doe', 'Jane Smith', 'Jim Brown']
}

tracker = FlightTracker(flights_data)

print("Total flights:", tracker.get_total_flights())
print("Average price:", tracker.get_average_price())
print("Longest flight duration:", tracker.get_longest_flight_duration())
print("Shortest flight duration:", tracker.get_shortest_flight_duration())
print("Total passengers:", tracker.get_total_passengers())
print("Flights by airline 'Delta':", tracker.get_flights_by_airline('Delta'))
print("Flights by origin 'NYC':", tracker.get_flights_by_origin('NYC'))
print("Flights by destination 'LON':", tracker.get_flights_by_destination('LON'))
print("Flights by date '2023-10-01':", tracker.get_flights_by_date('2023-10-01'))
print("Flights by status 'On Time':", tracker.get_flights_by_status('On Time'))
print("Flights by class 'Economy':", tracker.get_flights_by_class('Economy'))
print("Flights by captain 'John Doe':", tracker.get_flights_by_captain('John Doe'))
print("Flights by plane 'Boeing 747':", tracker.get_flights_by_plane('Boeing 747'))
print("Flights by time '10:00':", tracker.get_flights_by_time('10:00'))