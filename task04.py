from abc import ABC, abstractmethod


# Abstract base class
class Passenger(ABC):
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    @property
    def name(self):
        return self.__name

    @property
    def age(self):
        return self.__age

    @abstractmethod
    def get_discount(self):
        pass

    @abstractmethod
    def get_type(self):
        pass


# Inheritance: Regular passenger
class RegularPassenger(Passenger):
    def get_discount(self):
        return 0.0

    def get_type(self):
        return "Regular"


# Inheritance: Student passenger
class StudentPassenger(Passenger):
    def get_discount(self):
        return 0.10

    def get_type(self):
        return "Student"


# Flight class
class Flight:
    def __init__(self, code, airline, source, destination, seats, fare):
        self.__code = code
        self.__airline = airline
        self.__source = source
        self.__destination = destination
        self.__seats = seats
        self.__fare = fare

    @property
    def code(self):
        return self.__code

    @property
    def airline(self):
        return self.__airline

    @property
    def source(self):
        return self.__source

    @property
    def destination(self):
        return self.__destination

    @property
    def seats(self):
        return self.__seats

    @property
    def fare(self):
        return self.__fare

    def has_seats(self, count):
        return count <= self.__seats

    def reserve_seats(self, count):
        if count <= 0 or not self.has_seats(count):
            return False

        self.__seats -= count
        return True

    def display(self):
        print(
            f"{self.code:<10} {self.airline:<15} "
            f"{self.source:<15} {self.destination:<15} "
            f"{self.seats:<10} Rs.{self.fare}"
        )


# Booking class
class Booking:
    def __init__(self, booking_id, flight, passenger, tickets):
        self.booking_id = booking_id
        self.flight = flight
        self.passenger = passenger
        self.tickets = tickets

        self.subtotal = flight.fare * tickets
        self.discount = self.subtotal * passenger.get_discount()
        self.total = self.subtotal - self.discount

    def display_summary(self):
        print("\n========== BOOKING SUMMARY ==========")
        print("Booking ID:", self.booking_id)
        print("Passenger Name:", self.passenger.name)
        print("Passenger Age:", self.passenger.age)
        print("Passenger Type:", self.passenger.get_type())
        print("Flight Code:", self.flight.code)
        print("Airline:", self.flight.airline)
        print("Route:", self.flight.source, "to", self.flight.destination)
        print("Number of Tickets:", self.tickets)
        print(f"Base Fare per Ticket: Rs.{self.flight.fare:.2f}")
        print(f"Subtotal: Rs.{self.subtotal:.2f}")
        print(
            f"Discount ({self.passenger.get_discount() * 100:.0f}%): "
            f"Rs.{self.discount:.2f}"
        )
        print(f"Final Amount: Rs.{self.total:.2f}")
        print("=====================================")


# Main booking system
class FlightBookingSystem:
    def __init__(self):
        self.__flights = [
            Flight("PN101", "Kiran Air", "Pune", "Delhi", 20, 4000),
            Flight("MB202", "Sky India", "Mumbai", "Bengaluru", 30, 3500),
            Flight("PN303", "Air Connect", "Pune", "Hyderabad", 25, 3000)
        ]

        self.__bookings = []
        self.__next_booking_id = 1001

    def display_flights(self):
        print("\n================ AVAILABLE FLIGHTS ================")
        print(
            f"{'Code':<10} {'Airline':<15} {'Source':<15} "
            f"{'Destination':<15} {'Seats':<10} {'Base Fare'}"
        )
        print("-" * 85)

        for flight in self.__flights:
            flight.display()

        print("=" * 85)

    def find_flight(self, code):
        for flight in self.__flights:
            if flight.code.lower() == code.strip().lower():
                return flight
        return None

    def validate_details(self, flight, name, age, tickets):
        if flight is None:
            print("Error: Flight code does not exist.")
            return False

        if not name.strip():
            print("Error: Passenger name cannot be blank.")
            return False

        if age <= 0:
            print("Error: Age must be greater than zero.")
            return False

        if tickets <= 0:
            print("Error: Ticket count must be greater than zero.")
            return False

        if not flight.has_seats(tickets):
            print("Booking failed: Not enough seats available.")
            return False

        return True

    def book_flight(self):
        self.display_flights()

        code = input("Enter flight code: ").strip()
        flight = self.find_flight(code)

        name = input("Enter passenger name: ").strip()

        try:
            age = int(input("Enter age: "))
            passenger_type = input(
                "Passenger type (Regular/Student): "
            ).strip().lower()
            tickets = int(input("Enter number of tickets: "))
        except ValueError:
            print("Error: Age and ticket count must be integers.")
            return

        # Create the appropriate passenger object
        if passenger_type == "regular":
            passenger = RegularPassenger(name, age)
        elif passenger_type == "student":
            passenger = StudentPassenger(name, age)
        else:
            print("Error: Passenger type must be Regular or Student.")
            return

        # Validate everything before changing seat counts
        if not self.validate_details(flight, name, age, tickets):
            print("No booking was created. Seat counts remain unchanged.")
            return

        # Reserve seats only after successful validation
        if not flight.reserve_seats(tickets):
            print("Booking failed: Not enough seats available.")
            return

        booking = Booking(
            f"BK{self.__next_booking_id}",
            flight,
            passenger,
            tickets
        )

        self.__next_booking_id += 1
        self.__bookings.append(booking)

        print("\nBooking confirmed!")
        booking.display_summary()

    def view_booking(self):
        if not self.__bookings:
            print("\nNo confirmed bookings found.")
            return

        print("\nMost Recent Confirmed Booking:")
        self.__bookings[-1].display_summary()

    def run(self):
        while True:
            print("\nWelcome to Kiran Air Booking")
            print("1. View Flights")
            print("2. Book Flight")
            print("3. View Booking")
            print("4. Exit")

            choice = input("Enter choice: ").strip()

            if choice == "1":
                self.display_flights()

            elif choice == "2":
                self.book_flight()

            elif choice == "3":
                self.view_booking()

            elif choice == "4":
                print("Thank you for using Kiran Air Booking!")
                break

            else:
                print("Invalid choice. Please select 1, 2, 3, or 4.")


# Program entry point
if __name__ == "__main__":
    system = FlightBookingSystem()
    system.run()