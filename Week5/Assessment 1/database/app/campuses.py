from app.orm import ORM

class Campuses(ORM):
    tablename = 'campuses'
    fields = ["city", "state"]

    def __init__(self, *args, **kwargs):
        self.pk = kwargs.get('pk')
        self.city = kwargs.get('city')
        self.state = kwargs.get('state')