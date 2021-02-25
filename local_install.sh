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
BIN="$HOME/.local/bin"
LIB="$HOME/.local/lib"
CFG="$HOME/.config"

mkdir -p "$BIN" "$LIB" "$CFG"
cp -r "$DIR" "$LIB"

ln -sf "$LIB/$PROG/mybkp.py" "$BIN/mybkp"
if [ ! -f "$CFG/mybkp_profiles" ]; then
    cp "$LIB/$PROG/mybkp_profiles" "$CFG/mybkp_profiles"
fi
