
class User:
    def __init__(self, username, password, fullname, email):
        self.username = username
        self.password = password
        self.fullname = fullname
        self.email = email

    def check_password(self, password):
        return self.password == password


class Customer(User):
    counter = 0  # class variable

    def __init__(self, username, password, fullname, email):
        super().__init__(username, password, fullname, email)
        self.wallet_amount = 0
        self.is_enable = False

    def __str__(self):
        return self.username

    def set_enable(self):
        self.is_enable = True


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
        self.reseller = reseller

    def __str__(self):
        return f"name: {self.name},\t upc: {self.upc}"

    def is_free(self):
        return self.price == 0
