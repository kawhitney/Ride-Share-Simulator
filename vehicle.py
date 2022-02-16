class Vehicle:
    # Variables: vehicle id, array of customers(capacity=5), current location, next destination, path, miles
    def __init__(self, vehicleID, currentPosition):
        self.vehicleID = vehicleID
        self.currentPosition = currentPosition
        self.customers = []
        self.path = []
        self.destination = currentPosition
        self.miles = 0
        self.customer_in_queue = None
        self.is_busy = False

    def add_customer(self, customer):
        self.customers.append(customer)

    def remove_customer(self, customer):
        self.customers.remove(customer)

    def move_position(self, newPosition):
        self.currentPosition = newPosition

    def set_path(self, path):
        self.path = path

    def change_busy(self):
        if self.is_busy == False:
          self.is_busy = True
        else:
          self.is_busy = False

class Customer:
    # Variables: customer id, pick-up point, drop-off location
    def __init__(self, customerID, pickup, dropoff):
        self.customerID = customerID
        self.pickup = pickup
        self.dropoff = dropoff
