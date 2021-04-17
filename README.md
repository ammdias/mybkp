MY BACKUP README
================
version 2.4

Copyright (C) 2021 António Manuel Dias

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
along with this program.  If not, see http://www.gnu.org/licenses/.


Changes history:

* 2.4: Changed installation scripts.
       Changed README and MANUAL accordingly.
* 2.3: Corrected bug that prevented manual from being displayed.
* 2.2.1: Corrected bug that prevented an 'ok' to be shown after correctly
             parsing a composite profile.
* 2.2: Added option to edit the configuration file
* 2.1: Added option to list backup profiles
       Added option to display configuration file
       Composite profiles can now only be composed of simple profiles,
           thus preventing 'infinite loop' profiles
* 2.0: Complete rewrite in Python.
       Configuration with possible multiple profiles in a separate file.
* 1.0: Original bash script.


ABOUT THE PROGRAM
=================

This program makes easy the backup of a group of directories to another
location or remote directory, with the help of an external utility like
`rsync` or `cp`.  It depends on Python 3.

The following instructions are for Linux systems.  If you intend to use the
program on another system, please refer to the included MANUAL.


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

     If you want to install the program for all the users of the system, you
     should change the directories accordingly, e.g. `/usr/local/lib` for the
     installation directory and `/usr/local/bin` for the start link.  Of
     course, you will need to run the installation script with administration
     privileges:

         $ sudo python3 INSTALL.py

     If a previous installation exists on the selected directory, you will be
     asked if you want to overwrite it.  Answer "`yes`" (or just "`y`") if that
     is the case or "`no`"/"`n`" if not.

2. Test that the installation was successful with the command:

       $ mybkp --help

   (you should be presented with the program's help page)

3. Read the MANUAL.  You can open it in a web browser from the program with the
   command:

       $ mybkp --manual


