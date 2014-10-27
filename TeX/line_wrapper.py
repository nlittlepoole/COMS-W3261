#!/usr/bin/env python3
'''A script that can be run to wrap all lines in a file to 80 characters or
less.

Author: Alexander Roth
Date:   2014-10-21
'''
import sys
import textwrap

def main(filename):
    line_buff = read_in_file(filename)
    format_buff = format_new_lines(line_buff)
    write_to_file(filename, format_buff)
    

def read_in_file(filename):
    input_file = open(filename, 'r')
    line_buff = input_file.readlines()
    input_file.close()
    return line_buff


def format_new_lines(line_buff):
    dirty_buff = []
    for line in line_buff:
        if line == '\n':
            dirty_buff.append('')
        else:
            dirty_buff.extend(textwrap.wrap(line, width=80))
    output_buff = []
    for line in dirty_buff:
        output_buff.append(line + '\n')
    return output_buff


def write_to_file(filename, line_buff):
    output_file = open(filename, 'w')
    for i in line_buff:
        output_file.write(i)
    output_file.close()


def print_arguments():
    print('python3 line_wrapper <filename>')
    sys.exit(1)


if __name__ == '__main__':
    if len(sys.argv) == 2:
        main(sys.argv[1])
    else:
        print_arguments()
