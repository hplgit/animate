#!/bin/sh

sudo apt-get update

sudo apt-get -y install autoconf automake build-essential git \
     libass-dev libfaac-dev libgpac-dev libmp3lame-dev \
     libsdl1.2-dev libtheora-dev libtool libva-dev \
     libvdpau-dev libvorbis-dev libvpx-dev libx11-dev \
     libxext-dev libxfixes-dev pkg-config texi2html yasm zlib1g-dev
# sudo apt-get -y install libopus-dev  # not found (in 12.04)

mkdir ffmpeg_build
cd ffmpeg_build
dir=`pwd`
# x264
git clone --depth 1 git://git.videolan.org/x264.git
cd x264
./configure --prefix="$dir" --enable-static --disable-asm
make
make install
#make distclean
cd ..

# fdk-aac
git clone --depth 1 git://github.com/mstorsjo/fdk-aac.git
cd fdk-aac
autoreconf -fiv
sh ./configure --prefix="$dir" --disable-shared
make
make install
#make distclean
cd ..

# ffmpeg
#git clone --depth 1 git://source.ffmpeg.org/ffmpeg
cd ffmpeg
./configure --prefix="$dir" --extra-cflags="-I$dir/include" \
   --extra-ldflags="-L$dir/lib" --bindir="$dir/bin" --enable-gpl \
   --enable-libass --enable-libfaac --enable-libfdk-aac \
   --enable-libmp3lame --enable-libopus --enable-libtheora \
   --enable-libvorbis --enable-libvpx --enable-libx264 \
   --enable-nonfree --enable-x11grab
make
make install
#make distclean \
#hash -r source ~/.profile
