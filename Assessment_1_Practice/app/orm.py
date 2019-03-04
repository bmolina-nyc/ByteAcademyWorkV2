import sqlite3

class ORM:
    fields = [] 
    dbpath = "data/books_words.db"
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

            SQL = """ INSERT INTO {tablename} ({fieldlist})
                      VALUES ({qmarks}); """.format(
                tablename=self.tablename, fieldlist=fieldlist, qmarks=qmarks)

            values = [getattr(self, field) for field in self.fields]
            curs.execute(SQL, values)

            self.pk = curs.lastrowid

    def _update(self):
        with sqlite3.connect(self.dbpath) as conn:
            curs = conn.cursor()
            assignments = ", ".join([
                "{} = ?".format(field) for field in self.fields])

            SQL = """ UPDATE {tablename} SET {assignments}
                      WHERE pk = ?; """.format(
                tablename=self.tablename, assignments=assignments)

            values = [getattr(self, field) for field in self.fields]
            values.append(self.pk)

            curs.execute(SQL, values)

    @classmethod
    def select_one_from(cls, whereclause="", value=""):
        with sqlite3.connect(cls.dbpath) as conn:
            # conn.row_factory = sqlite3.Row
            curs = conn.cursor()

        SQL = """ SELECT * FROM {tablename} {whereclause};""".format(
          tablename = cls.tablename, whereclause=whereclause)
        curs.execute(SQL, value)
        result = curs.fetchone()
       
        if not result:
            return None
        return result

    # def delete(self):
    #     if not self.pk:
    #         raise KeyError(self.__repr__() + " does not appear in the database")
    #     with sqlite3.connect(self.dbpath) as conn:
    #         curs = conn.cursor()
    #         SQL = """ DELETE FROM {tablename} WHERE pk = ?; """

    #         curs.execute(SQL, (self.pk, ))

        
 