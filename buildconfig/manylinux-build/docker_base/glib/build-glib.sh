#!/bin/bash
set -e -x

cd $(dirname `readlink -f "$0"`)

GLIB_BASE_VER=2.74
GLIB_FULL_VER=${GLIB_BASE_VER}.7
GLIB=glib-${GLIB_FULL_VER}

curl -sL --retry 10 https://download.gnome.org/sources/glib/${GLIB_BASE_VER}/${GLIB}.tar.xz > ${GLIB}.tar.xz
sha512sum -c glib.sha512

unxz ${GLIB}.tar.xz
tar xf ${GLIB}.tar
cd $GLIB

if [[ "$MAC_ARCH" == "arm64" ]]; then
    # pass a 'cache' file while cross compiling to arm64 for glib. This is
    # needed for glib to determine some info about the target architecture
    export GLIB_COMPILE_EXTRA_FLAGS="--cache-file=../macos_arm64.cache"
fi

CFLAGS=-Wno-error ./configure $ARCHS_CONFIG_FLAG --with-pcre=internal $GLIB_COMPILE_EXTRA_FLAGS --disable-libmount --disable-dbus
CLFAGS=-Wno-error=declaration-after-statement make
make install

if [[ "$OSTYPE" == "darwin"* ]]; then
    # Install to mac deps cache dir as well
    make install DESTDIR=${MACDEP_CACHE_PREFIX_PATH}
fi
