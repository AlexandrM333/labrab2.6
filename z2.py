#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':

    dict1 = {
            1: 'ball',
            2: 'bird',
            3: 'three',
            4: 'mouse',
            5: 'cat',
            6: 'dog',
            7: 'blink',
        }

    dict_items = dict1.items()
    new_dict = {}

    for key, value in dict_items:
        new_dict.setdefault(value, key)

    print(new_dict)
