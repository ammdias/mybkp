MY BACKUP README
================
version 3.1

Copyright (C) 2015 António Manuel Dias

contact: ammdias@gmail.com

website: [AMMDIAS GitHub](https://github.com/ammdias/mybkp)

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the 
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see http://www.gnu.org/licenses/ .


ABOUT THE PROGRAM
=================

This program makes easy the backup of a group of directories to another
location or remote directory, with the help of an external utility like
`rsync` or `cp`.  It depends on Python 3.


INSTALLATION AND BASIC USAGE
============================

The following instructions describe the installation process for basic usage
in a Linux environment.  For more advanced instructions, including MS Windows
usage, please refer to the user manual in the file "MANUAL.md" or "MANUAL.html".

1. Open a terminal in the directory where the program was uncompressed and run
   the installation script with Python 3:

       $ python3 INSTALL.py

   You will be prompted for the installation directory --- i.e. the directory
   under which the folder containing all the application files will be placed
   --- and for the start link directory --- i.e. the directory where the
   symbolic link for the program will be created.

   The default directories will install the program for the current user only
   and are suited for single-user systems.  If you want to keep these
   settings, just press ENTER when prompted.  The program will be installed in
   the directory `$HOME/.local/lib/MyBkp` and the symbolic link
   `$HOME/.local/bin/mybkp` will be created.  On most Linux systems the
   `$HOME/.local/bin` directory will be inserted in the execution PATH, if it
   exists. If it doesn't, you will have to add it manually.

   If a previous installation exists on the selected directory, you will be
   asked if you want to overwrite it.  Answer "`yes`" (or just "`y`") if that
   is the case or "`no`" ("`n`") if not.

2. Test that the installation was successful with the command:

       $ mybkp --help

   (you should be presented with the program's help page)

3. Read the MANUAL.  You can open it in a web browser with the command:

       $ mybkp --manual
