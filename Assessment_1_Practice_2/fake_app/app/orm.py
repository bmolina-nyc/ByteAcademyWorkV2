import sqlite3


class ORM:
    fields = []
    dbpath = "data/practice_db.db"
    tablename = ""

    def save(self):
        if self.pk is None:
            self._insert()
        else:
            self._update()

    def _insert(self):
        with sqlite3.connect(self.dbpath) as conn:
            curs = conn.cursor()
            fieldlist = ", ".join(self.fields)
            qmarks = ", ".join(["?" for _ in self.fields])
          
            values = [getattr(self, field) for field in self.fields]
            SQL = """INSERT INTO {tablename} ({fieldlist})
                     VALUES({qmarks});""".format(
                         tablename = self.tablename, fieldlist = fieldlist, qmarks = qmarks) 
            curs.execute(SQL, values)

    def _update(self):
        with sqlite3.connect(self.dbpath) as conn:
            curs = conn.cursor()
            assignments = ", ".join([
                "{} = ?".format(field) for field in self.fields])
          
        SQL = """ UPDATE {tablename} SET {assignments}
                  WHERE pk = ?;""".format(
                      tablename = self.tablename, assignments=assignments)
        
        values= [getattr(self, field) for field in self.fields]
        values.append(self.pk)
        curs.execute(SQL, values)
        conn.commit()

    @classmethod
    def delete(cls, whereclause="", pk=""):
        # if not cls.pk:
        #     raise KeyError(cls.__repr__() +
        #         " does not appear in the database")
        with sqlite3.connect(cls.dbpath) as conn:
            curs = conn.cursor()
            SQL = """ DELETE FROM {tablename} {whereclause}; """.format(
                tablename=cls.tablename, whereclause=whereclause
            )
            curs.execute(SQL, pk)

    @classmethod
    def get_one_from(cls, whereclause="", value=""):
        with sqlite3.connect(cls.dbpath) as conn:
            conn.row_factory = sqlite3.Row
            curs = conn.cursor()
        SQL = """SELECT * FROM {tablename} {whereclause};""".format(
            tablename = cls.tablename, whereclause = whereclause)
        curs.execute(SQL, value)
        result = curs.fetchone()
        
        if not result:
            return None 
        else:
            return cls(**result)
    
    @classmethod
    def select_many_by(cls, whereclause="", age=""):
        with sqlite3.connect(cls.dbpath) as conn:
            curs = conn.cursor()
        SQL = """SELECT * FROM {tablename} {whereclause};""".format(
            tablename = cls.tablename, whereclause = whereclause)
        curs.execute(SQL, age)
        values = curs.fetchall()
        return values