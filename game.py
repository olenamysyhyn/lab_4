"""
Module contains classes for the game "Блукачка по Львову"
"""
class Street:
    """
    class Street for Lviv streets
    """
    def __init__(self, name):
        self.name = name
        self.description = None
        self.linked_streets = {}
        self.character = None
        self.item = None

    def set_description(self, description):
        """
        Methods sets the description of the street
        """
        self.description = description

    def get_description(self):
        """
        return the description of the exact street
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

    def link_street(self, room_to_link, direction):
        """
        method links the direction to another street
        """
        self.linked_streets[direction] = room_to_link

    def get_details(self):
        """
        method for details of the street
        """
        print(f"Ви знаходитесь на вулиці {self.name}.")
        print(self.get_description())
        for direction, street in self.linked_streets.items():
            print(f"Вулиця {street.get_name()} знаходитися, як йти на {direction}.")
        if self.character:
            print(f"Ви можете бачити {self.character.get_name()} тут.")
        if self.item:
            print(f"Також є {self.item.name} тут.")

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
        if direction in self.linked_streets:
            return self.linked_streets[direction]
        print('Цей шлях не є коректним')
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
        print(f"{self.name} тут!!!")
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
            print(f"[{self.name} говорить]: {self.conversation}")
        else:
            print(f"{self.name} не бажає розмовляти.")

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
            print(f"Ви боретесь з {self.name} маючи {item}.")
            self.defeated += 1
            return True
        else:
            print(f"{self.name} б'є Вас!")
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
        print(f"Предмет {self.name}: {self.description}")

    def get_name(self):
        """
        fo getting a name
        """
        return self.name
