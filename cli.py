"""My Backup - Command Line Interface

Backup a group of directories from a base location using an external program
(C) 2015 António Manuel Dias

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
"""

__version__ = '3.1'
__date__ = '2023-12-14'
__license__ ='GNU General Public License version 3'
__author__ = 'António Manuel Dias <ammdias@gmail.com>'


import sys
import os
import webbrowser
from core import *
from mybkp_text import *


def cli_run(args):
    """Run the program from the command line."""
    # options for displaying general information
    if args.version:
        prt_exit(f'{NAME} {__version__}')

    if args.copyright:
        prt_exit(f'{NAME} {__version__}\n\n{SHORT_COPYRIGHT}\n\n{COPYRIGHT}')

    if args.warranty:
        prt_exit(f'{NAME} {__version__}\n\n{SHORT_COPYRIGHT}\n\n{WARRANTY}')

    if args.uninstall:
        from UNINSTALL import uninstall
        uninstall()

    if args.manual:
        webbrowser.open_new(os.path.join(sys.path[0], 'MANUAL.html'))
        prt_exit(MANUAL)

    if args.include_destination_directories:
        prt_exit(WARNING_IDD, 1)
 
    # get configuration file path
    config_file = find_config_file(args.config)
    if not config_file:
        prt_exit(CONFIG_NOT_FOUND, 1)

    # options for manipulating config file
    if args.print_config:
        print(CONFIG_AT.format(config_file))
        prt_exit(open(config_file, 'r').read())

    if args.edit_config:
        edit_config(config_file)
        prt_exit('')

    # parse configuration file and build backup object
    try:
        valid_profiles = Profiles(config_file)
    except Exception as e:
        prt_exit(PARSING_EXCEPTION.format(e))

    # option to list valid profiles
    if args.list_profiles:
        list_profiles(valid_profiles.profiles)
        return

    # perform intended backup/restore operation
    backup(valid_profiles, args.profiles or ('default',),
           restore=args.restore, dryrun=args.no_act,
           bkpdir=args.backup_directory)


def list_profiles(profiles):
    """List valid configuration profiles."""
    for p in profiles:
        if type(profiles[p]) == list:
            print(f"{p}: {', '.join(profiles[p])}")
        else:
            print(p)


def edit_config(config_file):
    """Edit the configuration file with default editor."""
    if 'VISUAL' in os.environ:
        editor = os.environ['VISUAL']
    elif 'EDITOR' in os.environ:
        editor = os.environ['EDITOR']
    else:
        prt_exit(EDITOR_NOT_FOUND, 1)

    try:
        if subprocess.run((editor, config_file)).returncode:
            prt_exit(EDITOR_FAILED, 1)
    except Exception as e:
        prt_exit(EDITOR_EXCEPTION.format(e), 1)
    except:
        prt_exit(EDITOR_EXCEPTION_UNK, 1)


def backup(valid_profiles, profiles, restore, dryrun, bkpdir):
    """Perform backup on each profile."""
    try:
        for setup in valid_profiles.process_profiles(profiles, restore, bkpdir):
            print(PROFILE_SETUP.format(setup['profile'],
                                       setup['source'], setup['destination'],
                                       ', '.join(setup['directories']),
                                       ', '.join(setup['options'])))
            if not yesno(PROCEED):
                continue
            print()
    
            for dirsetup in process_directories(setup):
                if dryrun:
                    print(f"{' '.join(setup['command'])} "
                          f"\"{dirsetup['source']}\" \"{dirsetup['destination']}\"")
                else:
                    print(PROCESS_DIR.format(dirsetup['directory']))
                    exec_command(setup['command'],
                                 dirsetup['source'], dirsetup['destination'])
                    print()

    except ProfileNotFoundError as e:
        prt_exit(PROFILE_NOT_FOUND.format(e), 1)
    except NestedDirectoriesError:
        prt_exit(NESTED_DIR_EXCEPTION)
    except CommandError:
        prt_exit(CMD_ERROR)


def yesno(question):
    """Gets yes or no answer."""
    while True:
        ans = input(question).strip().lower()
        if ans in YES:
            return True
        if ans in NO:
            return False


def prt_exit(msg='', exit_code=0): 
    """Print message and exit."""
    print(msg, file=sys.stderr if exit_code else sys.stdout)
    sys.exit(exit_code)


