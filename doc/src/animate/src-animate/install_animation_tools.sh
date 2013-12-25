#!/bin/bash
set -x  # make sure each command is printed in the terminal

function apt_install {
  sudo apt-get -y install $1
  if [ $? -ne 0 ]; then
    echo "could not install $1 - abort"
    exit 1
  fi
}

sudo apt-get update --fix-missing

# Animations: avconv and ffmpeg (ffmpeg is no longer in Debian)
apt_install libav-tools
apt_install ffmpeg
apt_install libavcodec-extra-53
apt_install libx264-dev
#apt_install x264
#apt_install h264enc

# Animations: players
apt_install mplayer
apt_install gnome-mplayer
apt_install mencoder
apt_install totem
apt_install totem-plugins
apt_install totem-mozilla
apt_install vlc
apt_install browser-plugin-vlc
apt_install gxine
apt_install python-pyxine
apt_install xine-plugin
apt_install libxine2-dev
apt_install libxine2-all-plugins
apt_install gxine-plugin
apt_install libxine2-ffmpeg
apt_install swfdec-gnome
apt_install flashplugin-installer
