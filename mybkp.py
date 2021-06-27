#!/usr/bin/env python3

"""My Backup

Backup a group of directories from a base location using an external program
(C) 2015-2021 António Manuel Dias

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.

Changes:
    3.0: Code refactoring
    2.6: Removed creation destination directories because it was unsafe.
         Added confirmation step before starting backup process.
    2.5: Verify that source and destination directory are different
         Create destination directory if not exists
    2.4: Changed installation scripts.
         Changed README and MANUAL accordingly.
    2.3: Removed PDF documents. Added HTML manual and option to show it.
  2.2.1: Corrected bug that prevented an 'ok' to be shown after correctly
           parsing a composite profile.
    2.2: Added option to edit the configuration file.
    2.1: Added option to list backup profiles.
         Added option to display configuration file.
         Composite profiles can now only be composed of simple profiles,
           thus preventing 'infinite loop' profiles.
    2.0: Complete rewrite in Python.
         Configuration with possible multiple profiles in separate file.
"""

__version__ = '3.0'
__date__ = '2021-06-25'
__license__ ='GNU General Public License version 3'
__author__ = 'António Manuel Dias <ammdias@gmail.com>'


import sys
import argparse
from cli import cli_run, prt_exit
from mybkp_text import *


def parse_arguments():
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(description=f'{NAME} {__version__}: {DESCR}')

    parser.add_argument('profiles', type=str, nargs='*', help=ARG_PROFILES)

    parser.add_argument('-c', '--config', type=str, default='', help=ARG_CONFIG)

    parser.add_argument('-b', '--backup-directory', help=ARG_BACKUP_DIRECTORY)

    parser.add_argument('-e', '--edit-config', action='store_true', help=ARG_EDIT_CONFIG)

    parser.add_argument('-i', '--include_destination_directories', action='store_true',
                        help=ARG_IDD_DEPRECATED)

    parser.add_argument('-l', '--list-profiles', action='store_true', help=ARG_LIST_PROFILES)

    parser.add_argument('-n', '--no-act', action='store_true', help=ARG_NO_ACT)

    parser.add_argument('-p', '--print-config', action='store_true', help=ARG_PRINT_CONFIG)

    parser.add_argument('-r', '--restore', action='store_true', help=ARG_RESTORE)

    parser.add_argument('--copyright', action='store_true', help=ARG_COPYRIGHT)

    parser.add_argument('--warranty', action='store_true', help=ARG_WARRANTY)

    parser.add_argument('--manual', action='store_true', help=ARG_MANUAL)

    parser.add_argument('--version', action='store_true', help=ARG_VERSION)

    return parser.parse_args()

#------------------------------------------------------------------------------
# Program entry point

if __name__ == '__main__':
    try:
        args = parse_arguments()
        cli_run(args)
    except KeyboardInterrupt:
        prt_exit(EXIT_EXCEPTION, 1)
    except Exception as e:
        prt_exit(UNK_EXCEPTION.format(e), 1)
