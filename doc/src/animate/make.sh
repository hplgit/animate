#!/bin/sh
rsync="rsync -rtDvz -u -e ssh -b --exclude '*~' --exclude '*.sh' --suffix=.rsync~ --delete --force "

doconce format html video --html_style=bloodish
$rsync fig-animate mov-animate video.html ../../pub/
