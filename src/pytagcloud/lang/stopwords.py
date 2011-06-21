# -*- coding: utf-8 -*-
import os

ACTIVE_LISTS = 'english russian'.split()


def get_stop_words():
    stop_words = set()
    stop_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'stop')
    for root, dirs, files in os.walk(stop_dir):
        for file in files:
            if not file in ACTIVE_LISTS:
                continue
            stop_file = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'stop/', file), 'r')
            for stop_word in stop_file:
                stop_words.add(stop_word.strip().lower())
            stop_file.close()
    return stop_words
