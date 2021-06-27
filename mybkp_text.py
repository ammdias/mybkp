"""My Backup (text constants)

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
"""

__version__ = '3.0'
__date__ = '2021-06-25'
__license__ ='GNU General Public License version 3'
__author__ = 'António Manuel Dias <ammdias@gmail.com>'


ARG_PROFILES = 'name of the backup profile(s) to execute.'
ARG_CONFIG = 'path to the profiles configuration file.'
ARG_BACKUP_DIRECTORY = 'add this directory to the base backup directory.'
ARG_EDIT_CONFIG = "edit the configuration file using the system's default editor and exit."
ARG_IDD_DEPRECATED = 'This option has been deprecated and should not be used.'
ARG_LIST_PROFILES = 'list valid backup profiles in configuration file and exit.'
ARG_NO_ACT = 'show what files to backup, without actually performing the action.'
ARG_PRINT_CONFIG = 'show configuration file and exit.'
ARG_RESTORE = 'restore directories from backup.'
ARG_COPYRIGHT = 'show copyright information and exit.'
ARG_WARRANTY = 'show warranty information and exit.'
ARG_MANUAL = 'display the manual in a web browser window and exit.'
ARG_VERSION = 'show version information and exit.'

NAME = "My Backup"
DESCR = "Backup a group of directories."

SHORT_COPYRIGHT = """My Backup
(C) 2021 António Manuel Dias
<https://ammdias.duckdns.org/downloads>

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>."""

COPYRIGHT = """From the Preamble of the GNU General Public License:
        
The GNU General Public License is a free, copyleft license for
software and other kinds of works.

The licenses for most software and other practical works are designed
to take away your freedom to share and change the works.  By contrast,
the GNU General Public License is intended to guarantee your freedom to
share and change all versions of a program--to make sure it remains free
software for all its users.  We, the Free Software Foundation, use the
GNU General Public License for most of our software; it applies also to
any other work released this way by its authors.  You can apply it to
your programs, too.

When we speak of free software, we are referring to freedom, not
price.  Our General Public Licenses are designed to make sure that you
have the freedom to distribute copies of free software (and charge for
them if you wish), that you receive source code or can get it if you
want it, that you can change the software or use pieces of it in new
free programs, and that you know you can do these things.

To protect your rights, we need to prevent others from denying you
these rights or asking you to surrender the rights.  Therefore, you have
certain responsibilities if you distribute copies of the software, or if
you modify it: responsibilities to respect the freedom of others.

For example, if you distribute copies of such a program, whether
gratis or for a fee, you must pass on to the recipients the same
freedoms that you received.  You must make sure that they, too, receive
or can get the source code.  And you must show them these terms so they
know their rights.

See the file 'gpl.txt' on the program's directory for more details.
If it's missing please refer to http://www.gnu.org/licenses/gpl.txt
"""

WARRANTY = """From the GNU General Public License:
    
15. Disclaimer of Warranty.

THERE IS NO WARRANTY FOR THE PROGRAM, TO THE EXTENT PERMITTED BY
APPLICABLE LAW.  EXCEPT WHEN OTHERWISE STATED IN WRITING THE
COPYRIGHT HOLDERS AND/OR OTHER PARTIES PROVIDE THE PROGRAM "AS IS"
WITHOUT WARRANTY OF ANY KIND, EITHER EXPRESSED OR IMPLIED, INCLUDING,
BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND
FITNESS FOR A PARTICULAR PURPOSE.  THE ENTIRE RISK AS TO THE QUALITY
AND PERFORMANCE OF THE PROGRAM IS WITH YOU.  SHOULD THE PROGRAM PROVE
DEFECTIVE, YOU ASSUME THE COST OF ALL NECESSARY SERVICING, REPAIR OR
CORRECTION.

16. Limitation of Liability.

IN NO EVENT UNLESS REQUIRED BY APPLICABLE LAW OR AGREED TO IN WRITING
WILL ANY COPYRIGHT HOLDER, OR ANY OTHER PARTY WHO MODIFIES AND/OR
CONVEYS THE PROGRAM AS PERMITTED ABOVE, BE LIABLE TO YOU FOR DAMAGES,
INCLUDING ANY GENERAL, SPECIAL, INCIDENTAL OR CONSEQUENTIAL DAMAGES
ARISING OUT OF THE USE OR INABILITY TO USE THE PROGRAM (INCLUDING BUT
NOT LIMITED TO LOSS OF DATA OR DATA BEING RENDERED INACCURATE OR LOSSES
SUSTAINED BY YOU OR THIRD PARTIES OR A FAILURE OF THE PROGRAM TO
OPERATE WITH ANY OTHER PROGRAMS), EVEN IF SUCH HOLDER OR OTHER PARTY
HAS BEEN ADVISED OF THE POSSIBILITY OF SUCH DAMAGES.
"""

MANUAL = """The program's manual should open in a new web browser window.
If not, please read the manual in text format (actually *Markdown*) in
the program's installation directory.
"""

WARNING_IDD = """
WARNING: the -i / --include_destination_directories option is
no longer valid.  Instead, it has been substituted by the
"include_destination_directories" option in the "options" argument of each
profile.  Please, read the "Configuration file syntax > Available options"
section of the Manual for more information.
"""

CONFIG_AT = "Configuration file at: {}\n"

PROFILE_SETUP = """\nProcessing profile: {}
    From: {}
    To: {}
    Directories: {}
    Options: {}
"""
PROCEED = "Proceed with this operation (y/n)? "
YES = ('y', 'yes')
NO = ('n', 'no')

PROCESS_DIR = "Processing directory {} ..."

CONFIG_NOT_FOUND = """Configuration file not found.
Please provide the correct path to this file as an option
to the program or use the default locations to place it.
See the program's manual for more information on this subject.
"""

EXIT_EXCEPTION = "\nProcess terminated by user."
UNK_EXCEPTION = "\nUnknown error ocurred:\n{}"

EDITOR_NOT_FOUND = "No default editor is configured on your system."
EDITOR_FAILED = "Editor returned with non-zero status."
EDITOR_EXCEPTION = "Exception ocurred while editing the configuration file:\n-->{}"
EDITOR_EXCEPTION_UNK = "Unknown exception ocurred while editing the configuration file."

PROFILE_NOT_FOUND = "Profile not found: {}"
PARSING_EXCEPTION = "Exception occurred while reading the configuration file:\n--> {}"
CONFIG_EXCEPTION = "Exception ocurred when processing profile configuration:\n--> {}"

NESTED_DIR_EXCEPTION = "Error: destination directory inside source directory."
CMD_ERROR = "Profile command exited with non-zero status."

