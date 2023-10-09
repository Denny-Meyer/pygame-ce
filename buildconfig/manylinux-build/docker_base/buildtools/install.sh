#!/bin/bash

# This file installs tools (cmake and meson) needed to build dependencies

set -e -x

cd $(dirname `readlink -f "$0"`)

# The latest cmake doesn't easily compile from source on centos 5
# So cmake is installed with pip
# This way we save compile time, reduce maintenance+scripting efforts and also 
# get the right binaries of the latest cmake version that will work on centos 5
# and above (the pip cmake package provides manylinux1 i686/x86_64 and 
# manylinux2014 i686/x86_64/aarch64 wheels)

if [[ "$OSTYPE" == "linux-gnu"* ]]; then
    export PG_LINUX_EXTRA_FLAGS="--user"
fi

# pin versions for stability (remember to keep updated)
python3 -m pip install $PG_LINUX_EXTRA_FLAGS cmake==3.27.6 meson==1.2.2 ninja==1.11.1

if [[ "$OSTYPE" == "linux-gnu"* ]]; then
    cp /root/.local/bin/* /usr/bin
fi
