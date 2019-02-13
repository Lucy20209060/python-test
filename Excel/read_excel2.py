#!/usr/bin/python
# -*- coding: UTF-8 -*-
import xlrd
from xlutils import copy

def getBGColor(book, sheet, row, col):
    xfx = sheet.cell_xf_index(row, col)
    xf = book.xf_list[xfx]
    bgx = xf.background.pattern_colour_index
    pattern_colour = book.colour_map[bgx]

    #Actually, despite the name, the background colour is not the background colour.
    #background_colour_index = xf.background.background_colour_index
    #background_colour = book.colour_map[background_colour_index]

    return pattern_colour

book = xlrd.open_workbook('/Users/lc/Desktop/test.xls')
sheet = book.sheets()[1]
getBGColor(book, sheet, 0, 0)