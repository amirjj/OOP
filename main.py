from models import Customer, Product, Reseller, User


if __name__ == "__main__":
    r1 = Reseller(
        'brand', 'logo', 'username', 'password', 'fullname', 'email@email'
    )
    print(r1.username)
    p1 = Product('1', 'p1', 100, 'desc', r1)
    print(r1, p1)
    print(type(r1), type(p1))
    print(p1.reseller.username)
    u1 = User.create('username', 'pa', 'fullname', 'email')
    print(u1)

