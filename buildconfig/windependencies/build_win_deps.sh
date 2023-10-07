# This uses manylinux build scripts to build dependencies on windows.

set -e -x

# The below three lines convert something like D:\path\goes\here to /d/path/goes/here
export BASE_DIR=$(echo "$GITHUB_WORKSPACE" | tr '[:upper:]' '[:lower:]')
export BASE_DIR="${BASE_DIR//\\//}"  # //\\// replaces all \ with / in the variable
export BASE_DIR="${BASE_DIR//:/}"  # remove colon from drive part

export WIN_PREFIX_PATH="$BASE_DIR/pygame_win_deps_$WIN_ARCH"

export PKG_CONFIG_PATH="$WIN_PREFIX_PATH/lib/pkgconfig:$PKG_CONFIG_PATH"

mkdir $WIN_PREFIX_PATH

# for great speed.
export MAKEFLAGS="-j 2"

# for scripts using ./configure
export CC="gcc"
export CXX="g++"

# With this we
# 1) Force install prefix to $WIN_PREFIX_PATH
# 2) use lib directory (and not lib64)
# 3) make release binaries
# 4) build shared libraries
# 5) make cmake use gcc/g++/make
export PG_BASE_CMAKE_FLAGS="-DCMAKE_INSTALL_PREFIX=$WIN_PREFIX_PATH \
    -DCMAKE_INSTALL_LIBDIR:PATH=lib \
    -DCMAKE_BUILD_TYPE=Release \
    -DBUILD_SHARED_LIBS=true \
    -DCMAKE_C_COMPILER=$CC -DCMAKE_CXX_COMPILER=$CXX -DCMAKE_MAKE_PROGRAM=make"

export CMAKE_GENERATOR="MSYS Makefiles"

export ARCHS_CONFIG_FLAG="--prefix=$WIN_PREFIX_PATH"

cd ../manylinux-build/docker_base

# Now start installing dependencies
# ---------------------------------

mkdir -p ${WIN_PREFIX_PATH}/usr/local/man/man1

# sdl_image deps
bash zlib-ng/build-zlib-ng.sh
bash libpng/build-png.sh # depends on zlib
bash libjpegturbo/build-jpeg-turbo.sh
bash libtiff/build-tiff.sh
bash libwebp/build-webp.sh

# freetype (also sdl_ttf dep)
bash freetype/build-freetype.sh

# sdl_mixer deps
bash libmodplug/build-libmodplug.sh
bash ogg/build-ogg.sh
bash flac/build-flac.sh
bash mpg123/build-mpg123.sh
bash opus/build-opus.sh # needs libogg (which is a container format)

# installs sdl2 by itself (fluidsynth can use it)
bash sdl_libs/build-sdl2.sh

# fluidsynth (for sdl_mixer)
bash glib/build-glib.sh # depends on gettext
bash sndfile/build-sndfile.sh
bash fluidsynth/build-fluidsynth.sh

# build sdl_image, sdl_ttf and sdl_mixer
bash sdl_libs/build-sdl2-libs.sh

# for pygame.midi
bash portmidi/build-portmidi.sh
