import numpy as np
import random

class Vehicle:
    '''
        Variables: array of customers(capacity=5), current location, next destination (path?)
    '''
    def __init__(self):
        self.current_position = random.randrange(0, 200)
        self.customers = np.array([])
        self.destination = None

    def add_customer(self, customer):
        self.customers.append(customer)

    def remove_customer(self, customer):
        self.customers.remove(customer)

    def move_position(self, new_position):
        self.current_position = new_position

    def set_desitnation(self, destination):
        self.desitnation = destination

class Customer:
    '''
        Variables: pick-up point, drop-off location, pick-up time(?)
    '''
    def __init__(self, pickup, dropoff, distance):
        self.pickup = pickup
        self.dropoff = dropoff
        # self.pickup_time =
