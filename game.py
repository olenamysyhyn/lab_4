"""
Module contains classes for the game "Блукачка"
"""
class Room:
    """
    class Room for defining the room tou are in
    """
    def __init__(self, name):
        self.name = name
        self.description = None
        self.linked_rooms = {}
        self.character = None
        self.item = None

    def set_description(self, description):
        """
        Methods sets the description of the room
        """
        self.description = description

    def get_description(self):
        """
        return the description of the exact room
        """
        return self.description

    def get_name(self):
        """
        return the name
        """
        return self.name

    def describe(self):
        """
        method for description
        """
        print(self.get_description())

    def link_room(self, room_to_link, direction):
        """
        method links the direction to another room
        """
        self.linked_rooms[direction] = room_to_link

    def get_details(self):
        """
        method for details of the room
        """
        print(f"You are in the {self.name}.")
        print(self.get_description())
        for direction, room in self.linked_rooms.items():
            print(f"The {room.get_name()} is {direction}.")
        if self.character:
            print(f"{self.character.get_name()} is here!")

    def set_character(self, character):
        """
        method sets character
        """
        self.character = character

    def get_character(self):
        """
        for getting character
        """
        return self.character

    def set_item(self, item):
        """
        sets item
        """
        self.item = item

    def get_item(self):
        """
        for getting item
        """
        return self.item

    def move(self, direction):
        """
        methods for making a move
        """
        if direction in self.linked_rooms:
            return self.linked_rooms[direction]
        print('This way is wrong')
        return self

class Character:
    """
    class Character for defining a hero
    """
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.conversation = None

    def describe(self):
        """
        methos prints description
        """
        # print(f"{self.name} is here!")
        print(self.description)

    def set_conversation(self, conversation):
        """
        sets conversation
        """
        self.conversation = conversation

    def talk(self):
        """
        for defining a talk
        """
        if self.conversation:
            print(f"[{self.name} says]: {self.conversation}")
        else:
            print(f"{self.name} does not have a wish to talk.")

class Enemy(Character):
    """
    class Enemy for defining your enemies
    """
    def __init__(self, name, description):
        super().__init__(name, description)
        self.weakness = None
        self.defeated = 0

    def set_weakness(self, weakness):
        """
        for setting weakness
        """
        self.weakness = weakness

    def get_weakness(self):
        """
        fo getting weakness
        """
        return self.weakness

    def get_name(self):
        """
        for getting a name
        """
        return self.name

    def fight(self, item):
        """
        for making a fight with enemy
        """
        if item == self.weakness:
            print(f"You fend {self.name} off with the {item}.")
            self.defeated += 1
            return True
        else:
            print(f"{self.name} crushes you, puny adventurer!")
            return False

    def get_defeated(self):
        """
        for defeatimg
        """
        return self.defeated

class Friend(Character):
    """
    class Friend that takes arguments from class Character
    for defining your friend during game
    """
    def __init__(self, name, description):
        super().__init__(name, description)

class Item:
    """
    class Item for difining an item
    """
    def __init__(self, name):
        self.name = name
        self.description = None

    def set_description(self, description):
        """
        for description
        """
        self.description = description

    def describe(self):
        """
        method for decribing an item in game
        """
        print(f"The [{self.name}] is here - {self.description}")

    def get_name(self):
        """
        fo getting a name
        """
        return self.name

