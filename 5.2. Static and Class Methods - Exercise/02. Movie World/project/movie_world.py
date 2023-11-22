from project.customer import Customer
from project.dvd import DVD


class MovieWorld:
    def __init__(self, name):
        self.name = name
        self.customers = []
        self.dvds = []

    @staticmethod
    def dvd_capacity():
        return 15

    @staticmethod
    def customer_capacity():
        return 10

    def add_customer(self, customer: Customer):
        if len(self.customers) < self.customer_capacity():
            self.customers.append(customer)

    def add_dvd(self, dvd: DVD):
        if len(self.dvds) < self.dvd_capacity():
            self.dvds.append(dvd)

    def rent_dvd(self, customer_id, dvd_id):
        renting_customer = next(x for x in self.customers if x.id == customer_id)
        searched_dvd = next(x for x in self.dvds if x.id == dvd_id)

        if searched_dvd.is_rented:
            if searched_dvd in renting_customer.rented_dvds:
                return f"{renting_customer.name} has already rented {searched_dvd.name}"
            return "DVD is already rented"

        if renting_customer.age < searched_dvd.age_restriction:
            return f"{renting_customer.name} should be at least {searched_dvd.age_restriction} to rent this movie"

        renting_customer.rented_dvds.append(searched_dvd)
        searched_dvd.is_rented = True
        return f"{renting_customer.name} has successfully rented {searched_dvd.name}"

    def return_dvd(self, customer_id, dvd_id):
        renting_customer = next(x for x in self.customers if x.id == customer_id)
        searched_dvd = next(x for x in self.dvds if x.id == dvd_id)

        if searched_dvd not in renting_customer.rented_dvds:
            return f"{renting_customer.name} does not have that DVD"

        renting_customer.rented_dvds.remove(searched_dvd)
        searched_dvd.is_rented = False
        return f"{renting_customer.name} has successfully returned {searched_dvd.name}"

    def __repr__(self):
        result = []
        for customer in self.customers:
            result.append(customer.__repr__())
        for dvd in self.dvds:
            result.append(dvd.__repr__())
        return '\n'.join(result)




