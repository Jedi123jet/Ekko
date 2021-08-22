# macros.py contains the SavedFiles class, which is used
#   to maintain a directory of files with saved macro inputs

import os
import player
import record

DEFAULT_LOG = "action_log.txt"


class SavedFiles:
    DIRECTORY_NAME = "Macros"  # name of directory to save files in
    files = ['' for x in range(0, 1)]  # list of file names
    current_idx = 0  # current index of objects
    current_size = 1  # current maximum number of files

    def __init__(self):
        try:
            os.mkdir(self.DIRECTORY_NAME)
        except FileExistsError:
            for filename in os.listdir(self.DIRECTORY_NAME):
                self.files[self.current_idx] = filename.replace(".txt", "")
                self.current_idx += 1
                if self.current_idx == self.current_size:
                    self.files.append('')
                    self.current_size += 1
            self.current_idx = 0

    def get_current_idx(self):
        return self.current_idx

    def set_current_idx(self, idx):
        self.current_idx = idx

    def get_current_size(self):
        return self.current_size

    def set_current_size(self, size):
        self.current_size = size

    # get_file_data returns a tuple containing the current file's information.
    #   * returns data of form (file number, file name)
    #   * get_file_data()[0] = file number
    #   * get_file_data()[1] = file name
    def get_file_data(self):
        return (self.current_idx + 1, self.files[self.current_idx])

    # get_current_file returns the current file location
    def get_current_file(self):
        if self.files[self.current_idx] == '': return
        return self.DIRECTORY_NAME + '\\' + self.files[self.current_idx] + ".txt"

    # set_current_file sets the current file to have name filename
    def set_current_file(self, filename):
        try:
            if self.files[self.current_idx] == '':
                open(self.DIRECTORY_NAME + '/' + filename + ".txt", "x")
            else:
                os.rename(self.get_current_file(),
                          self.DIRECTORY_NAME + "/" + filename + ".txt")
            self.files[self.current_idx] = filename
        except FileExistsError:
            pass

    # to_prev_file sets the current file to the previous file
    #   * if the current file is the first one, we instead loop to the end
    def to_prev_file(self):
        if self.current_idx == 0:
            self.current_idx = self.current_size - 1
        else:
            self.current_idx -= 1

    # to_next_file sets the current file to the next file
    #   * if the current file is the last one, we instead loop to the front
    def to_next_file(self):
        if self.current_idx == self.current_size - 1:
            self.current_idx = 0
        else:
            self.current_idx += 1

    # to_idx sets the current file to the one specified by index idx
    #   * idx starts from 0, so recording #1 corresponds to idx 0
    def to_idx(self, idx):
        if 0 <= int(idx) and int(idx) < self.current_size:
            self.current_idx = int(idx)
        else:
            raise ValueError("bad index")

    # new_file produces a new file with name filename, and
    #   changes the current file as such:
    #   * if current file is empty, do not change
    #   * else, chooses first available empty file
    #   * if no empty files, creates new file
    #  returns new index
    def new_file(self, filename="Macro"):
        if self.files[self.current_idx] == '':
            pass
        else:
            all_full = True
            for i in range(0, len(self.files)):
                if filename == self.files[i]:
                    self.to_idx(i)
                    self.set_current_file(filename)
                    return self.current_idx
            for i in range(0, len(self.files)):
                if self.files[i] == '':
                    all_full = False
                    self.to_idx(i)
                    break
            if all_full:
                self.files.append('')
                self.current_size += 1
                self.to_idx(self.current_size - 1)
        self.set_current_file(filename)
        return self.current_idx

    # delete_file deletes the current file, if it exists
    def delete_file(self):
        if self.files[self.current_idx] != '':
            os.remove(self.get_current_file())
        self.files[self.current_idx] = ''

    # play_recording plays the current file using
    #   the Player object, plyr
    def play_recording(self, plyr):
        if self.files[self.current_idx] != '':
            plyr.play(self.get_current_file())

    def log_to_macros(self, filename):
        self.new_file(filename)
        open(self.get_current_file(), 'w').close()
        with open(DEFAULT_LOG, 'r') as infile, open(self.get_current_file(), 'a') as outfile:
            for line in infile:
                outfile.write(line)
        return self.current_idx