from bearlibterminal import terminal as blt


class GameObject:
    pass
    # constructor

    def __init__(self, engine):
        self.engine = engine

    def update(self):
        pass

    def render(self):
        pass


class Map:

    def __init__(self):
        pass


class Room:

    # constructor
    def __init__(self, name, description, exits=[], people=[]):
        self.name = name
        self.description = description
        self.exits = exits
        self.people = people


class GameController(GameObject):

    def __init__(self, game_engine):
        super().__init__(game_engine) # look up super() method!
        self.current_room = Room(
            'Room name',
            'Description',
            exits=['N', 'S', 'E', 'W'],
            # cool-kids room:
            people=['Bashinerox', 'pRyapus22', 'kuchkiAizen', 'MarkDTS', 'rhymu8354']
            )


    def list_exits(self, room):
        return ", ".join(room.exits)


    def list_people(self, room):
        return ", ".join(room.people)
        

    def render(self):
        room_description = f"""Location : {self.current_room.name}
{self.current_room.description}

Exits:
{self.list_exits(self.current_room)}

Other people:
{self.list_people(self.current_room)}"""
        blt.printf(1, 0, room_description)


    # gonna do stuff like get user input and change the room, move the player, 
    

