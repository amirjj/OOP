
class User:
    def __init__(self, username, password, fullname, email):
        self.username = username
        self.password = password
        self.fullname = fullname
        self.email = email

    def check_password(self, password):
        return self.password == password

<<<<<<< HEAD
    @classmethod
    def create(cls, username, password, fullname, email):
        if len(password) < 3:  # prevent creating object with password less than
            # 3 characters
            print("Password need to be longer thant 3")
            return None
        return cls(username, password, fullname, email)

    @staticmethod
    def validate_password(password):
        # staticmethod has no difference with a function written outside the
        # class, just because semantically it's related to a particular
        # class it's better to write it in the class
        return len(password) > 3

=======
>>>>>>> 945ff8d0d00c144367ff8d98539dde6910e28443

class Customer(User):
    counter = 0  # class variable

    def __init__(self, username, password, fullname, email):
        super().__init__(username, password, fullname, email)
<<<<<<< HEAD
        # private variable, can't be access from outside this class
        self.__wallet_amount = 0
        self.is_enable = False
        Customer.counter += 1  # counting number of objects created

=======
        self.wallet_amount = 0
        self.is_enable = False
>>>>>>> 945ff8d0d00c144367ff8d98539dde6910e28443

    def __str__(self):
        return self.username

    def set_enable(self):
        self.is_enable = True

<<<<<<< HEAD
    @property
    def wallet(self):  # convert method to attr
        return self.__wallet_amount

=======
>>>>>>> 945ff8d0d00c144367ff8d98539dde6910e28443

class Reseller(User):
    def __init__(self, brand, logo, *args, **kwargs):
        self.brand = brand
        self.logo = logo
        super().__init__(*args, **kwargs)

    def __str__(self):
        return f"name: {self.username}"


class Product:
    product_list = list()  # class variable

    def __init__(self, upc, name, price=0, description='', reseller=None):
        self.upc = upc  # object variables
        self.name = name
        self.price = price
        self.description = description
        Product.product_list.append(self)
        # This called composition
        # This means that a class Composite can contain an object of another
        # class Component
        self.reseller = reseller

    def __str__(self):
        return f"name: {self.name},\t upc: {self.upc}"

    def is_free(self):
        return self.price == 0

# https://realpython.com/inheritance-composition-python/
# Usage of Abstract methods explained
# Abstract Base Class: exist to be inherited, but never instantiated
