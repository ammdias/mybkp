"""My Backup - Nuclear classes and functions for My Backup program

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
import os.path
import subprocess
from configparser import ConfigParser, ExtendedInterpolation
from mybkp_text import PROFILE_NOT_FOUND


DEFAULT_CONFIG_FILES = (
    os.path.expanduser(os.path.join('~', '.mybkp_profiles')),
    os.path.expanduser(os.path.join('~', '.config', 'mybkp_profiles'))
)


def find_config_file(config_file):
    """Return configuration file path."""
    config_files = DEFAULT_CONFIG_FILES
    # read install log to check original config file path
    try:
        for i in open(os.path.join(sys.path[0], 'install.log')).readlines():
            ptype, sep, path = i.strip().partition(':')
            if '' in (ptype, sep, path):
                break                     # invalid log, ignore
            if ptype == 'config_file':
                config_files = (path, *config_files)
                break
    except:
        pass                              # error reading log, ignore

    for i in (config_file,) if config_file else config_files:
        if os.path.lexists(i):
            return i

    return None


def process_directories(setup):
    """Loop over directories on a setup configuration,
       processing each one."""
    for d in setup['directories']:
        src, dest = (os.path.join(setup['source'], d, ''), # '' ensures source is a directory
                     os.path.join(setup['destination'], d)
                     if 'include_destination_directories' in setup['options']
                     else setup['destination'])

        if dest.startswith(src):
            raise NestedDirectoriesError()

        yield {
            'directory': d,
            'source': src,
            'destination': dest
        }


def exec_command(command, source, destination):
    """Execute command on source and destination directories."""
    if subprocess.run((*command, source, destination)).returncode:
        raise CommandError()


class Profiles:
    """Dictionary of backup profiles."""

    def __init__(self, config_file):
        """Dictionary of backup profiles.
           config_file: path to the My Backup configuration file.
        """
        config_parser = ConfigParser(interpolation=ExtendedInterpolation())
        config_parser.read(config_file)

        self.profiles = {}
        comp_profiles = []
        base_opts = set(('command', 'base', 'backup', 'directories'))
        comp_opts = base_opts | set(('options',))
        for p in config_parser.sections():
            profile_opts = set(config_parser[p])
            if profile_opts == base_opts:
                self.profiles[p] = config_parser[p]
                self.profiles[p]['options'] = '' 
            elif profile_opts == comp_opts:
                self.profiles[p] = config_parser[p]
            elif 'profiles' in profile_opts:
                comp_profiles.append(p)

        for p in comp_profiles:
            if len(config_parser[p]) == 1:
                c = []
                for pp in map(str.strip, config_parser[p]['profiles'].split(',')):
                    if pp in self.profiles:
                        c.append(pp)
                if c:
                    self.profiles[p] = c


    def process_profiles(self, profiles, restore, bkpdir):
        """Loop over profiles yielding a setup configuration for each one."""
        for profile in profiles:
            p = self.profiles.get(profile, None)
            if not p:
                raise ProfileNotFoundError(profile)

            if type(p) == list:
                profiles += p
                continue

            command = p['command'].split()
            src, dest = p['base'], p['backup']
            directories = list(map(str.strip, p['directories'].split(',')))
            options = list(map(str.strip, p['options'].split(',')))

            if bkpdir:
                dest = os.path.join(dest, bkpdir)

            if restore:
                src, dest = dest, src

            yield {
                'profile': profile,
                'command': command,
                'source': src,
                'destination': dest,
                'directories': directories,
                'options': options
            }


class ProfileNotFoundError(Exception):
    """Raised by an operation on a non-existing profile."""

class NestedDirectoriesError(Exception):
    """Raised when destination directory is inside source directory."""

class CommandError(Exception):
    """Raised when processing command returns non-zero."""

