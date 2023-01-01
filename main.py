<<<<<<< HEAD
from models import Customer, Product, Reseller, User
=======
from models import Customer, Product, Reseller
>>>>>>> 945ff8d0d00c144367ff8d98539dde6910e28443

if __name__ == "__main__":
    r1 = Reseller(
        'brand', 'logo', 'username', 'password', 'fullname', 'email@email'
    )
    print(r1.username)
    p1 = Product('1', 'p1', 100, 'desc', r1)
    print(r1, p1)
    print(type(r1), type(p1))
    print(p1.reseller.username)
<<<<<<< HEAD
    u1 = User.create('username', 'pa', 'fullname', 'email')
    print(u1)

=======
>>>>>>> 945ff8d0d00c144367ff8d98539dde6910e28443
