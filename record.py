from pynput import mouse
from pynput import keyboard
from time import perf_counter


class Timer:
    def __init__(self):
        self.start_time = 0
        self.stop_time = 0

    def start(self):
        self.start_time = perf_counter()
        return self.start_time

    def stop(self):
        if not self.start_time:
            # Tried to stop a self.timer that hasn't started
            return 0
        self.stop_time = perf_counter()
        elapsed = self.stop_time - self.start_time
        self.start_time = 0
        return elapsed


class Recorder:
    log_file = "action_log.txt"

    def __init__(self):
        self.keyboard_listener = keyboard.Listener(
            on_press=self.on_press,
            on_release=self.on_release)
        self.mouse_listener = mouse.Listener(
            on_move=self.on_move,
            on_click=self.on_click,
            on_scroll=self.on_scroll)
        self.timer = Timer()

    def on_move(self, x, y):
        with open(self.log_file, 'a') as f:
            f.write(f'Wait {self.timer.stop()}\n')
            self.timer.start()
            f.write(f'mMove {x} {y}\n')

    def on_click(self, x, y, button, pressed):
        with open(self.log_file, 'a') as f:
            if button == mouse.Button.left:
                if pressed:
                    f.write(f'Wait {self.timer.stop()}\n')
                    self.timer.start()
                    f.write(f'mPress {x} {y} {button}\n')
                else:
                    f.write(f'Wait {self.timer.stop()}\n')
                    self.timer.start()
                    f.write(f'mRelease {x} {y} {button}\n')
            elif button == mouse.Button.right:
                if pressed:
                    f.write(f'Wait {self.timer.stop()}\n')
                    self.timer.start()
                    f.write(f'mPress {x} {y} {button}\n')
                else:
                    f.write(f'Wait {self.timer.stop()}\n')
                    self.timer.start()
                    f.write(f'mRelease {x} {y} {button}\n')

    def on_scroll(self, x, y, dx, dy):
        with open(self.log_file, 'a') as f:
            f.write(f'Wait {self.timer.stop()}\n')
            self.timer.start()
            f.write(f'Scroll {x} {y} {dx} {dy}\n')

    def on_press(self, key):
        if hasattr(key, 'char'):
            with open(self.log_file, 'a') as f:
                f.write(f'Wait {self.timer.stop()}\n')
                self.timer.start()
                f.write('kPress {0}\n'.format(key.char))
        else:
            with open(self.log_file, 'a') as f:
                f.write(f'Wait {self.timer.stop()}\n')
                self.timer.start()
                f.write('kPress {0}\n'.format(key))

    def on_release(self, key):
        if key == keyboard.Key.esc:
            # Stop listener
            return False

        if hasattr(key, 'char'):
            with open(self.log_file, 'a') as f:
                f.write(f'Wait {self.timer.stop()}\n')
                self.timer.start()
                f.write('kRelease {0}\n'.format(key.char))
        else:
            with open(self.log_file, 'a') as f:
                f.write(f'Wait {self.timer.stop()}\n')
                self.timer.start()
                f.write('kRelease {0}\n'.format(key))

    def record(self):
        # Clear log file
        open(self.log_file, 'w').close()

        # Start threads
        self.mouse_listener.start()
        self.keyboard_listener.start()

        # End threads
        self.keyboard_listener.join()
        self.mouse_listener.stop()

        # Reset threads
        self.__init__()

        return True