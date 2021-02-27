#!/usr/bin/env python3
#-*- coding: utf-8 -*-

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

__version__ = '2.3'
__date__ = '2021-02-27'
__license__ ='GNU General Public License version 3'
__author__ = 'António Manuel Dias <ammdias@gmail.com>'


import sys
import os.path
import argparse
import subprocess
import webbrowser
from configparser import ConfigParser, ExtendedInterpolation
from mybkp_text import *


DEFAULT_CONFIG_FILES = (
    os.path.expanduser(os.path.join('~', '.mybkp_profiles')),
    os.path.expanduser(os.path.join('~', '.config', 'mybkp_profiles'))
)


def _run():
    '''Main function.'''
    args = parse_cli_arguments()

    if args.list_profiles:
        list_profiles(args.config)
    elif args.print_config:
        print_config(args.config)
    elif args.edit_config:
        edit_config(args.config)
    elif args.copyright:
        print(NAME, __version__, '\n')
        print(SHORT_COPYRIGHT, '\n')
        _quit(COPYRIGHT)
    elif args.warranty:
        print(NAME, __version__, '\n')
        print(SHORT_COPYRIGHT, '\n')
        _quit(WARRANTY)
    elif args.manual:
        webbrowser.open_new(os.path.join(sys.path[0], 'MANUAL.html'))
        _quit(MANUAL)
    elif args.version:
        _quit(f"{NAME} {__version__}")
    else:
        profiles = args.profile or ("default",)
        config = get_config(profiles=profiles, config_option=args.config)
        if not config:
            _quit("Nothing to do: no valid profile found.")
        for i in config:
            print(f"\nProcessing profile: {i}")
            backup(config[i], restore=args.restore, dryrun=args.no_act,
                   incdirs=args.include_destination_directories,
                   bkpdir=args.backup_directory)


def list_profiles(config_option=None):
    '''List valid configuration profiles.'''
    profiles = valid_profiles(config_option)
    for p in profiles:
        if type(profiles[p]) == list:
            print(f"{p}: {', '.join(profiles[p])}")
        else:
            print(p)


def print_config(config_option=None):
    '''Print configuration file.'''
    print(open(config_file(config_option), 'r').read())


def edit_config(config_option=None):
    '''Edit the configuration file with default editor.'''
    if 'VISUAL' in os.environ:
        editor = os.environ['VISUAL']
    elif 'EDITOR' in os.environ:
        editor = os.environ['EDITOR']
    else:
        _quit("No default editor is configured on your system.")

    try:
        if subprocess.run((editor, config_file(config_option))).returncode:
            _quit("Editor returned with non-zero status.")
    except Exception as e:
        _quit(f"Exception ocurred while editing the configuration file:\n-->{e}")
    except:
        _quit("Unknown exception ocurred while editing the configuration file.")
    print()


def backup(config, restore=False, dryrun=False, incdirs=False, bkpdir=None):
    '''Perform the backup/restore process.'''
    try:
        command = config['command'].split()
        src, dest = config['base'], config['backup']
        directories = map(str.strip, config['directories'].split(','))
    except Exception as e:
        _quit(f"Exception occurred while parsing profile values:\n--> {e}")

    if bkpdir:
        dest = os.path.join(dest, bkpdir)

    if restore:
        action = "Restoring"
        src, dest = dest, src
    else:
        action = "Backing up"

    for i in directories:
        s,d = (os.path.join(src, i, ''),     # '' ensures source is a directory
               os.path.join(dest, i) if incdirs else dest)
        if dryrun:
            print(f'{config["command"]} "{s}" "{d}"')
        else:
            print(f'{action} directory {i} ...')
            try:
                if subprocess.run((*command, s, d)).returncode:
                    _quit("Profile command exited with non-zero status.")
            except Exception as e:
                _quit(f'Exception occured while running the backup command:\n--> {e}')
            except:
                _quit('Unknown exception occurred while running the backup command.')
            print()


def parse_cli_arguments():
    '''Parse command line arguments.'''
    parser = argparse.ArgumentParser(description=f"{NAME} {__version__}: "
                                                  "Backup a group of directories.")

    parser.add_argument("profile", type=str, nargs='*',
                        help="name of the backup profile to use.")

    parser.add_argument("-c", "--config", type=str, default='',
                        help="path to the profiles configuration file.")

    parser.add_argument("-b", "--backup_directory",
                        help="add this directory to the base backup directory.")

    parser.add_argument("-e", "--edit_config", action="store_true",
                        help="edit the configuration file using the system's"
                             " default editor and exit.")

    parser.add_argument("-i", "--include_destination_directories",
                        action="store_true",
                        help="add directory names to the destination argument "
                             "of the command (as required by the rsync program).")

    parser.add_argument("-l", "--list_profiles", action="store_true",
                        help="list valid backup profiles in configuration file and exit.")

    parser.add_argument("-n", "--no_act", action="store_true",
                        help="show what files to backup, "
                             "without actually performing the action.")

    parser.add_argument("-p", "--print_config", action="store_true",
                        help="show configuration file and exit.")

    parser.add_argument("-r", "--restore", action="store_true",
                        help="restore directories from backup.")

    parser.add_argument("--copyright", action="store_true",
                        help='show copyright information and exit.')

    parser.add_argument("--warranty", action="store_true",
                        help= 'show warranty information and exit.')

    parser.add_argument("--manual", action="store_true",
                        help= 'display the manual in a web browser window and exit.')

    parser.add_argument("--version", action="store_true",
                        help='show version information and exit.')

    return parser.parse_args()


def get_config(profiles, config_option=None):
    '''Parse configuration file.'''
    vp = valid_profiles(config_option)
    config = {}
    for profile in profiles:
        print(f"Parsing profile: {profile}...", end=' ')
        if profile not in vp:
            print("invalid profile.")
            continue

        if type(vp[profile]) == list:
            profiles += vp[profile]
        else:
            config[profile] = vp[profile]
        print("ok.")

    return config


def valid_profiles(config_option):
    '''Parse configuration file and return valid profiles dictionary.'''
    try:
        config_parser = ConfigParser(interpolation=ExtendedInterpolation())
        config_parser.read(config_file(config_option))
    except Exception as e:
        _quit(f"Exception occurred while reading the configuration file:\n--> {e}")

    profiles = {}
    comp_profiles = []
    options = set(('command', 'base', 'backup', 'directories'))
    for p in config_parser.sections():
        profile_opts = set(config_parser[p])
        if profile_opts == options:
            profiles[p] = config_parser[p]
        elif 'profiles' in profile_opts:
            comp_profiles.append(p)

    for p in comp_profiles:
        if len(config_parser[p]) == 1:
            c = []
            for pp in map(str.strip, config_parser[p]['profiles'].split(',')):
                if pp in profiles:
                    c.append(pp)
            if c:
                profiles[p] = c

    return profiles


def config_file(config_option):
    """Return configuration file name."""
    for i in (config_option,) if config_option else DEFAULT_CONFIG_FILES:
        if os.path.exists(i):
            return i

    _quit("Configuration file not found.\n"
          "Please provide the correct path to this file as an option\n"
          "to the program or use the default locations to place it.\n"
          "See the program's manual for more information on this subject.")


def _error(msg):
    """Print error message."""
    print(msg, file=sys.stderr)


def _quit(msg=''): 
    '''Print message and exit.'''
    _error(msg)
    sys.exit(1)


if __name__ == '__main__':
    _run()

