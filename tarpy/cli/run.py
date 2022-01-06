''' CLI Parser

Module of tarpy.
Usage:
    tarpy [ROOT] [TARGET] -m {'w', 'e'} [--exclude_file] [--compression]

'''

import argparse
import textwrap
from typing import Any
from tarpy.tarhandler import Tarpy
from tarpy.logger import LOGGER, CONSOLE_HANDLER
from tarpy.config import OPTIONS

def cliparser() -> Any:
    ''' CLI Parser

    Function takes parameters like defined below and
    returns the args.
    '''
    parser = argparse.ArgumentParser(
            description = 'Different TAR Archive operations.',
            epilog = textwrap.dedent('''\
                Important Notes:
                    - a mode "-m" has always to be set.
                    - Edit the Config File to use the
                      "use_settings" - option.
                '''),
            formatter_class=argparse.RawTextHelpFormatter,
            )
    parser.add_argument(
            'ROOT',
            type=str,
            nargs='?',
            default=None,
            help='''
            The (starting) directory to archive respectively 
            the file to extract.
            If giving a Path, avoid relative paths and always
            try to give the absolute path to not force any
            side effects.
            '''
            )
    parser.add_argument(
            'TARGET',
            type=str,
            nargs='?',
            default=None,
            help='The path where archive will be written to.'
            )
    parser.add_argument(
            '-m',
            choices=['w', 'e'],
            help = 'Which Operation to run.'
            )

    parser.add_argument(
            '-ex-f',
            '--exclude-file',
            metavar='PATH',
            help='File with exclusions defined. Please try to specify the full path.'
            )

    parser.add_argument(
            '-c',
            '--compression',
            choices=['gz', 'bz2', 'xz'],
            help='''
            The compression method.
            gz  -   Gzip
            bz2 -   bzip2
            xz  -   lzma'''
            )

    parser.add_argument(
            '-v',
            '--verbose',
            help='Be Verbose.',
            action='store_true'
            )

    parser.add_argument(
            '--use_settings',
            help='Use own Settings.',
            action='store_true',
            )

    return parser

def cli() -> Any:
    ''' Core function of CLI
    '''
    args = cliparser().parse_args()

    # If no options are given, print the help.
    # If there is no "-m" and no "--use_settings",
    # there is not enough operations to start the
    # tarpy process.
    if not args.__dict__['m'] and not args.__dict__['use_settings']:
        cliparser().print_help()

    # Make sure User does not want to use own settings.
    if not args.use_settings:
        root = args.ROOT
        target = args.TARGET
        # Default Variables.
        exclude_file = args.exclude_file
        compression = args.compression
        mode = args.m

    else:
        ...

    if args.verbose:
        LOGGER.addHandler(CONSOLE_HANDLER)

    handler = Tarpy(
            mode,
            root = root,
            target = target,
            exclude_file = exclude_file,
            compression = compression,
            )
    LOGGER.info('Initialized Tarpy.')
    return handler()
