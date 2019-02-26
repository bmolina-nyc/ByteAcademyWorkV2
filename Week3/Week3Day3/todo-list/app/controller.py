from app import view
from app.user import User

def run():
    user_args = view.get_user()
    user = user_args[0]
    pin = user_args[1]
    user = User(username=user, pin=pin)
    user.save()