# Shell session for various movie making commands
cd testfiles
frames=frames
movie=movie1
rm -rf ${movie}*  # clean up

# ffmpeg and avconv
programs="ffmpeg avconv"
for prog in $programs; do
$prog -r 12 -i $frames/frame_%04d.png -c:v libx264   ${movie}_$prog.mp4
$prog -r 12 -i $frames/frame_%04d.png -c:v libvpx    ${movie}_$prog.webm
$prog -r 12 -i $frames/frame_%04d.png -c:v libtheora ${movie}_$prog.ogg
$prog -r 12 -i $frames/frame_%04d.png -c:v flv       ${movie}_$prog.flv
$prog -r 12 -i $frames/frame_%04d.png                ${movie}_$prog.avi
$prog       -i $frames/frame_%04d.png -c:v mpeg4     ${movie}_$prog.mpeg
done

# javascript code
python ../html_player.py $frames/frame_0*.png > ${movie}.html

# convert (use just a subset of the frames on small machines, otherwise
# the file takes a long time to produce and becomes very big)
subset_of_files=`/bin/ls $frames/frame_00[1-4]*.png`
#convert -delay 8 $subset_of_files $movie.gif

# mencoder...

