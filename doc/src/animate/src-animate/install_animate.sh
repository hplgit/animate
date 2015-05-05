#!/bin/bash
# Automatically generated script by
# vagrantbox/doc/src/vagrant/src-vagrant/deb2sh.py
# where vagrantbox is the directory arising from
# git clone git@github.com:hplgit/vagrantbox.git

# The script is based on packages listed in debpkg_animate.txt.

set -x  # make sure each command is printed in the terminal

function apt_install {
  sudo apt-get -y install $1
  if [ $? -ne 0 ]; then
    echo "could not install $1 - abort"
    exit 1
  fi
}

function pip_install {
  sudo pip install --upgrade "$@"
  if [ $? -ne 0 ]; then
    echo "could not install $p - abort"
    exit 1
  fi
}

sudo apt-get update --fix-missing

apt_install ffmpeg
apt_install libav-tools
apt_install libavcodec-extra-56
apt_install libx264-dev

apt_install mplayer
apt_install gnome-mplayer
apt_install totem
apt_install totem-plugins
apt_install totem-mozilla
apt_install vlc
apt_install browser-plugin-vlc
apt_install gxine
apt_install xine-plugin
apt_install libxine2-dev
apt_install libxine2-all-plugins
apt_install libxine2-ffmpeg
apt_install swfdec-gnome
apt_install flashplugin-installer
echo "Everything is successfully installed!"
