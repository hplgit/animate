#!/bin/sh
src=../src-animate/testfiles
movie=movie1
prog=ffmpeg

# must have run ../src-animate/session.sh

for ext in ".mp4 .webm .ogg .flv .html"; do
cp $src/${movie}_${prog}.${ext} demo.${ext}
done

cp -r $src/frames .
cp $src/${movie}.gif demo.gif
