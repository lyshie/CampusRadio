#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import re
import pafy


def get_youtube_token(url):
    # https://www.youtube.com/watch?v=bu7nU9Mhpyo
    m = re.search(r'\?v=([\w\-]{11})$', url)
    if m:
        return m.group(1)

    # https://youtu.be/bu7nU9Mhpyo
    m = re.search(r'\/([\w\-]{11})$', url)
    if m:
        return m.group(1)

    # bu7nU9Mhpyo
    m = re.search(r'([\w\-]{11})$', url)
    if m:
        return m.group(1)


def get_audio_path():
    # "/home/lyshie/sources/git/CampusRadio" / "audio"
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), "audio")


def main():
    token = get_youtube_token(sys.argv[1])

    # download audio only
    v = pafy.new(token)
    s = v.getbestaudio(preftype="m4a")
    print("Title => {title}".format(title=v.title))
    filename = s.download(filepath=get_audio_path())

if __name__ == '__main__':
    main()
