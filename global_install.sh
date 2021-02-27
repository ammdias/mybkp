#!/usr/bin/env bash

if ! [ -x "$(command -v python3)" ]; then
    echo '"python3" command not found.' >&2
    echo 'Please ensure that Python version 3 is installed and try again.' >&2
    exit 1
fi

chmod +x mybkp.py

DIR="`dirname \"$0\"`"
DIR="`( cd \"$DIR\" && pwd )`"
PROG="`basename \"$DIR\"`"
BIN="/usr/local/bin"
LIB="/usr/local/lib"

mkdir -p "$BIN" "$LIB"
cp -r "$DIR" "$LIB"

ln -sf "$LIB/$PROG/mybkp.py" "$BIN/mybkp"
