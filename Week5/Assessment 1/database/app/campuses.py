from app.orm import ORM

class Campuses(ORM):
    tablename = 'campuses'
    fields = ["student_pk", "city", "state"]

    def __init__(self, *args, **kwargs):
        self.pk = kwargs.get('pk')
        self.student_pk = kwargs.get('student_pk')
        self.city = kwargs.get('city')
        self.state = kwargs.get('state')