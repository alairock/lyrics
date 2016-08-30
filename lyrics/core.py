from . import lastfm
import os
import time


def clear():
    os.system('clear')


def main():
    lfm = lastfm.LastFM()
    count = 0
    try:
        while True:
            if lfm.song_has_changed():
                clear()
                lfm.print_info(count)
            count += 1
            time.sleep(2)
    except KeyboardInterrupt:
        pass






