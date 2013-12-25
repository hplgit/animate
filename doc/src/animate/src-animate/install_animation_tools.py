#!/usr/bin/env python

import commands, sys

def system(cmd):
    """Run system command cmd."""
    failure, output = commands.getstatusoutput(cmd)
    if failure:
       print 'Command\n  %s\nfailed.' % cmd
       print output
       sys.exit(1)

system('sudo apt-get update --fix-missing')

# Animations: avconv and ffmpeg (ffmpeg is no longer in Debian)
system('sudo apt-get -y install libav-tools')
system('sudo apt-get -y install ffmpeg')
system('sudo apt-get -y install libavcodec-extra-53')
system('sudo apt-get -y install libx264-dev')
#system('sudo apt-get -y install x264 h264enc')

# Animations: players
system('sudo apt-get -y install mplayer')
system('sudo apt-get -y install gnome-mplayer')
system('sudo apt-get -y install mencoder')
system('sudo apt-get -y install totem')
system('sudo apt-get -y install totem-plugins')
system('sudo apt-get -y install totem-mozilla')
system('sudo apt-get -y install vlc')
system('sudo apt-get -y install browser-plugin-vlc')
system('sudo apt-get -y install gxine')
system('sudo apt-get -y install python-pyxine')
system('sudo apt-get -y install xine-plugin')
system('sudo apt-get -y install libxine2-dev')
system('sudo apt-get -y install libxine2-all-plugins')
system('sudo apt-get -y install gxine-plugin')
system('sudo apt-get -y install libxine2-ffmpeg')
system('sudo apt-get -y install swfdec-gnome')
system('sudo apt-get -y install flashplugin-installer')
