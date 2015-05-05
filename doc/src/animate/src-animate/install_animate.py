#!/usr/bin/env python
# Automatically generated script by
# vagrantbox/doc/src/vagrant/src-vagrant/deb2sh.py
# where vagrantbox is the directory arising from
# git clone git@github.com:hplgit/vagrantbox.git

# The script is based on packages listed in debpkg_animate.txt.

logfile = 'tmp_output.log'  # store all output of all operating system commands
f = open(logfile, 'w'); f.close()  # touch logfile so it can be appended

import subprocess, sys

def system(cmd):
    """Run system command cmd."""
    print cmd
    try:
        output = subprocess.check_output(cmd, shell=True,
                                         stderr=subprocess.STDOUT)
    except subprocess.CalledProcessError as e:
        print 'Command\n  %s\nfailed.' % cmd
        print 'Return code:', e.returncode
        print e.output
        sys.exit(1)
    print output
    f = open(logfile, 'a'); f.write(output); f.close()

system('sudo apt-get update --fix-missing')
system('sudo apt-get -y install ffmpeg')
system('sudo apt-get -y install libav-tools')
system('sudo apt-get -y install libavcodec-extra-56')
system('sudo apt-get -y install libx264-dev')

system('sudo apt-get -y install mplayer')
system('sudo apt-get -y install gnome-mplayer')
system('sudo apt-get -y install totem')
system('sudo apt-get -y install totem-plugins')
system('sudo apt-get -y install totem-mozilla')
system('sudo apt-get -y install vlc')
system('sudo apt-get -y install browser-plugin-vlc')
system('sudo apt-get -y install gxine')
system('sudo apt-get -y install xine-plugin')
system('sudo apt-get -y install libxine2-dev')
system('sudo apt-get -y install libxine2-all-plugins')
system('sudo apt-get -y install libxine2-ffmpeg')
system('sudo apt-get -y install swfdec-gnome')
system('sudo apt-get -y install flashplugin-installer')
print 'Everything is successfully installed!'
