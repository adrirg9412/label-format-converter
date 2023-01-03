#!/usr/bin/env python3 
# -*- coding: utf-8 -*- 

import os
from shutil import rmtree
import sys
from converter import LabelConverter
import argparse

def argument_parser():
    parser = argparse.ArgumentParser(
                    prog = 'Label Format Converter',
                    description = 'Script to convert from some format labels to YOLO format.')
    parser.add_argument('-f', '--format',
                        choices=['cvat', 'coco', 'pascal'],
                        help='Which format do you want to convert to YOLO?')
    return parser.parse_args()


def main(args):

    l = LabelConverter()

    try:
        classes_dict = l.get_classes(os.path.join(os.getcwd(), 'res', 'classes.json'))
    except OSError as err:
        print(f"{err}", file=sys.stderr)
        return

    opt = args.format

    if os.path.exists(os.path.join(os.getcwd(), 'labels', 'yolo')):
            rmtree(os.path.join(os.getcwd(), 'labels', 'yolo'))

    if opt == 'cvat':
        l.cvat_to_yolo('annotations.xml', classes_dict)
    elif opt == 'pascal':
        l.pascal_to_yolo('Annotations', classes_dict)
    elif opt == 'coco':
        l.coco_to_yolo('instances_default.json', classes_dict)
    else:
        pass

if __name__ == "__main__":
    args = argument_parser()
    main(args)