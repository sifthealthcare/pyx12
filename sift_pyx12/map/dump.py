#! /usr/bin/env python

import os.path
import sys

import sift_pyx12.error_handler
import sift_pyx12.map_if
from sift_pyx12.params import params
import sift_pyx12.segment


def donode(node):
    print((node.get_path()))
    for child in node.children:
        if child.is_loop() or child.is_segment():
            donode(child)

param = params()
param.set('map_path', os.path.expanduser('~/src/sift_pyx12/map/'))
map = sift_pyx12.map_if.load_map_file(sys.argv[1], param)
donode(map)
