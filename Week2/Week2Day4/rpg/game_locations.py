from location import Location
from monster import Tiger, Kitten

location_start = Location(
    "Grand Central Station", """You are in Grand Central Station.

This is a gargantuan train station. It seems like the whole world passes
through here."""
)

location_platform = Location(
    "A Train Platform", """You are on a train platform.

Strangely there are no other passengers waiting here.""")

location_office = Location(
    "A Desolate Office Lobby",
    """You are in the lobby of a desolate office building.

You are in the lobby of a desolate office building. A cackling voice on a 
loudspeaker says something about a fire alarm."""
)

location_train = Location(
    "A Train Home",
    """You board a train heading home.

You leave the city. Your adventure is over.""",
    end=True)

location_byte = Location(
    "The 35th Floor", """You step off the elevator and enter Byte Academy.

The raw brainpower in this place is overwhelming.""")

location_start.attach_path("Go Downstairs", location_platform)
location_platform.attach_path("Go Upstairs", location_start)
location_platform.attach_path("Board Train", location_train)
location_start.attach_path("Walk South", location_office)
location_office.attach_path("Walk North", location_start)
location_office.attach_path("Take Elevator Up", location_byte)
location_byte.attach_path("Take Elevator Down", location_office)

location_platform.attach_monster(Kitten())
location_byte.attach_monster(Tiger())
