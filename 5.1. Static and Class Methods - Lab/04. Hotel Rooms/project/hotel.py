from project.room import Room


class Hotel:
    def __init__(self, name):
        self.name = name
        self.rooms = []
        self.guests = 0

    @classmethod
    def from_stars(cls, stars_count):
        return cls(f"{stars_count} stars Hotel")

    def add_room(self, room):
        self.rooms.append(room)

    def take_room(self, room_number, people):
        room = next(x for x in self.rooms if x.number == room_number)
        room.take_room(people)

    def free_room(self, room_number):
        room = next(x for x in self.rooms if x.number == room_number)
        room.free_room()

    def status(self):
        total_guests = sum(x.guests for x in self.rooms if x.is_taken)
        free_rooms = f"{', '.join((str(x.number) for x in self.rooms if not x.is_taken))}"
        taken_rooms = f"{', '.join((str(x.number) for x in self.rooms if x.is_taken))}"
        return f"Hotel {self.name} has {total_guests} total guests\nFree rooms: {free_rooms}\nTaken rooms: {taken_rooms}"

