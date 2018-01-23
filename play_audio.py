#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import re
import argparse
from random import shuffle
import multiprocessing
from playsound import playsound
#import pyglet


class Argument(object):

    def __init__(self):
        super(Argument, self).__init__()
        self.parser = argparse.ArgumentParser()
        self.parser.add_argument('--random', '-r', action='store_true')
        self.parser.add_argument('--wait', '-w', default=0, type=int)
        self.args = self.parser.parse_args()


def get_audio_path():
    # "/home/lyshie/sources/git/CampusRadio" / "audio"
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), "audio")


def get_audio_files():
    p = get_audio_path()
    return [os.path.join(p, f) for f in os.listdir(p) if os.path.isfile(os.path.join(p, f))]


def play_audio(random=False):
    audio_files = get_audio_files()

    if random:
        shuffle(audio_files)
    else:
        audio_files.sort()

    for f in audio_files:
        try:
            playsound(f)
        except:
            pass


def main():
    argument = Argument()

    # Timed out a process
    # https://stackoverflow.com/questions/47712093/timeout-for-multiprocessing
    process = multiprocessing.Process(
        target=play_audio, args=(argument.args.random, ))
    process.daemon = True
    process.start()

    process.join(argument.args.wait)
    if process.is_alive():
        process.terminate()


if __name__ == '__main__':
    main()
