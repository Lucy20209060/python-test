#!/usr/bin/python
# -*- coding: utf-8 -*-
import json
# with open('test.txt', 'w') as file_obj:
#     file_obj.write('I Love You\n')
#     file_obj.write('I Love You\n')

file_path = 'num.json'
with open(file_path) as file_obj:
    number = json.load(file_obj)

print(number)