# Write classes for the following class hierarchy:
#
#  [Vehicle]->[FlightVehicle]->[Starship]
#      |                |
#      v                v
# [GroundVehicle]      [Airplane]
#   |       |
#   v       v
# [Car]  [Motorcycle]
#
# Each class can simply "pass" for its body. The exercise is about setting up
# the hierarchy.
#
# e.g.
#
# class Whatever:
#     pass
#
# Put a comment noting which class is the base class

# Base class for FlightVehicle and GroundVehicle


class Vehicle:
    pass

# Base class for Starship and Airplane


class FlightVehicle(Vehicle):
    def __init__(self):
        # just to show that we're inheriting something
        super().__init__()
        pass


# Base class for Car and Motorcycle
class GroundVehicle(Vehicle):
    def __init__(self):
        # just to show that we're inheriting something
        super().__init__()
        pass


# inheriting from FlightVehicle Class
class Airplane(FlightVehicle):
    def __init__(self):
        # just to show that we're inheriting something
        super().__init__()
        pass


class Starship(FlightVehicle):
    def __init__(self):
        # just to show that we're inheriting something
        super().__init__()
        pass

# inheriting from GroundVehicle Class


class Car(GroundVehicle):
    def __init__(self):
        # just to show that we're inheriting something
        super().__init__()
        pass


class Motorcycle(GroundVehicle):
    def __init__(self):
        # just to show that we're inheriting something
        super().__init__()
        pass
