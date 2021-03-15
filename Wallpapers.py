from math import ceil


class WinDoor:
    """Class for creating windows and doors."""

    def __init__(self, w, h, name="unknown"):
        self.width = w
        self.height = h
        self.name = name
        self.square = w * h

    def __repr__(self):
        return f'{self.name}: {self.width}x{self.height}'


class Room:
    """Class for creating rooms."""

    def __init__(self, w, l, h):
        self.width = w
        self.length = l
        self.height = h
        self.wd = []

    def find_full_square(self):
        """Func to finding full square of room (without windows and doors)."""
        return 2 * self.height * (self.width + self.length)

    def add_WD(self, w, h, name='unknown'):
        """Func to creating class objects WinDoor and adding this objects in var wd (defined in __init__)."""
        self.wd.append(WinDoor(w, h, name))

    def find_work_square(self):
        """Func to finding square need to hang wallpaper."""
        new_square = self.find_full_square()
        for i in self.wd:
            new_square -= i.square
        return new_square

    def find_number_of_rolls(self, l, w):
        """Func to finding number of wallpaper rolls required for wallpapering."""
        square_one_roll = l * w
        return ceil(self.find_work_square() / square_one_roll)


def interface_for_user():
    """Func to taking info from user and give result how much wallpapers rolls user needs"""

    print("Hi! First you must to give main information about your room.\n"
          "Please, enter next sizes:")
    w, l, h = float(input('Width: ')), float(input('Length: ')), float(input('Height: '))
    user_room = Room(w, l, h)
    print(f'Full square of your room without windows and doors: {round(user_room.find_full_square(), 2)} m2')

    user_action = input("Please, write 'YES' if you want to add places which doesn't need to be wallpapered or 'NO' "
                        "if you don't want: ").upper()
    if user_action == "YES":
        print("Next you must to give sizes of places (for example windows or doors) which doesn't need to be "
              "wallpapered\n"
              "Please, enter next sizes:")
        command_user = 'next'
        while command_user != 'NO':
            w, h, name = float(input('Width: ')), float(input('Height: ')), input('Name of places (not necessarily): ')
            user_room.add_WD(w, h, name)
            command_user = input("Write 'NEXT' if you want to add other places, or 'NO' if you have finished: ").upper()

    print(f'Work square of your room for wallpapering: {round(user_room.find_work_square(), 2)} m2')
    print('At the end, please, enter length and width of one wallpaper roll:')
    l, w = float(input('Length: ')), float(input('Width: '))
    print(f'To hang wallpaper your room you need {user_room.find_number_of_rolls(l, w)} wallpaper rolls. '
          f'Thank you, good bye!')


interface_for_user()
