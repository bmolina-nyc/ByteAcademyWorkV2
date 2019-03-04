import sqlite3
from app.orm import ORM

class MyNHL(ORM):
    tablename="nhl"
    fields = ["Rk", "Player", "Age"]
    
    def __init__(self, *args, **kwargs):
        self.pk = kwargs.get('pk')
        self.Rk = kwargs.get("Rk")
        self.Player = kwargs.get("Player")
        self.Age = kwargs.get("Age")
       
    @classmethod
    def remove_player_by_pk(cls):
       pk = input("enter the id to remove")
       cls.delete("WHERE pk =?", (pk,))

    @classmethod
    def get_player_by_name(cls, name):
        return cls.get_one_from("WHERE Player = ?", (name,))
    
    @classmethod
    def update_player_by_name(cls):
        name = input("enter the name to update")
        age = input("enter new age")
        sql_object = cls.get_player_by_name(name)
        sql_object.Age = age
        sql_object.save()

    
    @classmethod
    def select_players_by_age(cls,age):
        return cls.select_many_by("Where Age = ?", (age,))
   
