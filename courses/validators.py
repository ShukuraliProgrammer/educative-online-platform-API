from accounts.models import StudentUser
from courses.models import Course, Cart

def cart_check(data):
    carts = Cart.objects.all()
    if data in carts:
        return False
    else:
        return True
