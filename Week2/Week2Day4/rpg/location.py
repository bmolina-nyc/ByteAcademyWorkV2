import monster

class Location:
    short_description = None
    long_description = None
    end = False
    monster = None
    paths = None
    
    def __init__(self, short_desc = None, long_desc = None, end = False):
        self.short_description = short_desc
        self.long_description = long_desc
        self.end = end
        self.paths = {}

    def attach_path(self, option, location):
        self.paths[option] = location

    def attach_monster(self, monster):
        self.monster = monster

    def remove_monster(self):
        self.monster = None

    def __str__(self):
        return self.short_description
