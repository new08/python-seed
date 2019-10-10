#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import optparse
import sys


def execute(argv=None, settings=None):
    if argv is None:
        argv = sys.argv

    parser = optparse.OptionParser(formatter=optparse.TitledHelpFormatter(), \
                                   conflict_handler='resolve')
    # parser.add_option('-L', '-l', type='string', help='log level: [ERROR, INFO, None]', default='None')

    (opts, args) = parser.parse_args(args=argv[1:])
    # print(opts)
    # print('parser' + parser.)

    sys.exit(0)
