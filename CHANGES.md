My Backup
=========

(C) 2015 António Manuel Dias

Changes list:

    * 3.1  New install system.
           Added uninstall option.
           Updated README and MANUAL.

    * 3.0: Code refactoring

    * 2.6: Removed creation destination directories because it was unsafe.
           Added confirmation step before starting backup process.

    * 2.5: Verify that source and destination directory are different
           Create destination directory if not exists

    * 2.4: Changed installation scripts.
           Changed README and MANUAL accordingly.

    * 2.3: Removed PDF documents. Added HTML manual and option to show it.

    * 2.2.1: Corrected bug that prevented an 'ok' to be shown after correctly
             parsing a composite profile.

    * 2.2: Added option to edit the configuration file.

    * 2.1: Added option to list backup profiles.
           Added option to display configuration file.
           Composite profiles can now only be composed of simple profiles,
           thus preventing 'infinite loop' profiles.

    * 2.0: Complete rewrite in Python.
           Configuration with possible multiple profiles in separate file.
    
    * 1.0: Original bash script.
