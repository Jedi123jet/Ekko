# player.py contains functions to assist in repeating mouse/keyboard
#   events as read from a file.
# * see sample_annotated.txt for file formatting details

from pynput import mouse
from pynput import keyboard
from pynput.mouse import Button
from pynput.keyboard import Key
from time import sleep


class Player:
    mouse_ctrl = mouse.Controller()
    keyboard_ctrl = keyboard.Controller()

    # file_to_list(filename) returns a list based on the file, filename:
    #   * each item is a tuple representing an input event
    def file_to_list(self, filename):
        file = open(filename, 'r')
        lines = file.readlines()
        count = 0

        for line in lines:
            lines[count] = lines[count].rstrip()
            lines[count] = tuple(lines[count].split(" "))
            count += 1

        return lines

    # play(filename) repeats the mouse/keyboard events occuring
    #   in the file, filename
    def play(self, filename):

        lines = Player.file_to_list(self, filename)

        def move(x, y):
            Player.mouse_ctrl.position = (int(x), int(y))

        for line in lines:
            cmd = line[0]
            if cmd == 'mMove':
                move(line[1], line[2])
            elif cmd == 'Wait':
                sleep(float(line[1]))
            elif cmd == 'mPress':
                move(line[1], line[2])
                Player.mouse_ctrl.press(eval(line[3]))
            elif cmd == 'mRelease':
                move(line[1], line[2])
                Player.mouse_ctrl.release(eval(line[3]))
            elif cmd == 'Scroll':
                move(line[1], line[2])
                Player.mouse_ctrl.scroll(int(line[3]), int(line[4]))
            elif cmd == 'kPress':
                if len(line[1]) == 1:
                    Player.keyboard_ctrl.press(line[1])
                else:
                    Player.keyboard_ctrl.press(eval(line[1]))
            elif cmd == 'kRelease':
                if len(line[1]) == 1:
                    Player.keyboard_ctrl.release(line[1])
                else:
                    Player.keyboard_ctrl.release(eval(line[1]))
            else:
                raise ValueError('File has invalid formatting')
